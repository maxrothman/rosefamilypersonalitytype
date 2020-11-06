import json
from pathlib import Path

def prompt_user(prompt, choices, error_prompt=None):
    """
    Prints a set of choices, then prompts the user to pick one

    prompt: the string to prompt the user with
    error_prompt: an optional alternate prompt to use if the user selects an invalid choice
    choices: a dict of {selector: text}, where the selectors are what the user types into the prompt
        and the texts are the texts of the options
    
    returns: a valid choice
    """
    if error_prompt is None:
        error_prompt = prompt

    for selector, text in choices.items():
        print(f"{selector}. {text}")

    # If the answer was invalid, loop until they give a valid one
    while True:
        choice = input(prompt)
        try:
            if choice in choices:
                break
            else:
                prompt = error_prompt
        except ValueError:
            continue
    
    return choice


def load_json_files(path):
    """
    Load all the JSON files in the specified path

    path: a Path object to look for JSON files in
    returns: dict mapping file names to the JSON-deserialized contents of the files
    """
    results = {}
    for file in path.iterdir():
        with open(file) as f:
            results[file.name] = json.load(f)
    return results


scores = []

# Get the list of questions
questions = load_json_files(Path('questions'))
characters = list(load_json_files(Path('characters')).values())

for _, question_data in sorted(questions.items(), key=lambda kv: kv[0]):
    # Ask the user the question
    answer2score = question_data["answers"]
    choice2answer = dict([(str(k), v) for k, v in enumerate(answer2score.keys(), start=1)])
    print(question_data["question"])
    choice = prompt_user(
        prompt="Input answer number: ",
        choices=choice2answer,
        error_prompt="Quit fucking around, gosh. ",
    )

    # A valid answer has been selected, log the scores
    scores.append(answer2score[choice2answer[choice]])

# Total the scores
score_avg = {
    "lovability": 0,
    "selfishness": 0,
    "lovable selfishness": 0,
    "entrepeneurship": 0,
    "modesty": 0,
    "entitlement": 0,
    "wit": 0,
}
for score in scores:
    for key, value in score.items():
        score_avg[key] += value

# Average the scores
for stat, value in score_avg.items():
    score_avg[stat] = round(value / len(questions))

# Accumulate differences between each character and the user
character_diffs = []
for character_data in characters:
    character_diff = {
        'name': character_data['name'],
        'total': 0,
    }

    # for each character, you are compared, and given a closeness score
    # We only end up using the name and total keys, but mo data is mo better
    for key, value in score_avg.items():
        diff = abs(character_data[key] - value)
        character_diff[key] = diff
        character_diff['total'] += diff

    character_diffs.append(character_diff)

# If we break the user down into each character, what percent does each character make them up?
# Or, what percent of the total differences does each character's diff from the user make up?
total_diff = sum(char_diff['total'] for char_diff in character_diffs)
user_character_percentages = {
    char_diff['name']: char_diff['total'] / total_diff
    for char_diff in character_diffs
}

# Print the user's results
# Users get a personality type made up of the first letters of each
# character's name, ordered by similarity
personality_type = ''.join(
    char_diff['name'][0]
    for char_diff in sorted(character_diffs, key=lambda i: i["total"], reverse=True)
)
print(f"Mazel tov! Your Rose Family Personality Type is {personality_type} !")
print("You are:")
for name, percent in sorted(user_character_percentages.items(), key=lambda kv: kv[1], reverse=True):
    print(f"{round(percent * 100)}% {name} Rose")
