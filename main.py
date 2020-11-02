import json
from pathlib import Path

scores = []

# Get the list of questions
question_files = list(Path('questions/').iterdir())
question_count = len(question_files)

for path in sorted(question_files):
    # Read in the question
    with open(path) as f:
        question_data = json.load(f)

    # Ask the user the question
    print(question_data["question"])
    answers = list(question_data["answers"].keys())
    for i, answer in enumerate(answers, start=1):
        print(f"{i}. {answer}")

    prompt = "Input answer number: "
    # If the answer was invalid, loop until they give a valid one
    while True:
        choice = input(prompt)
        prompt = "Quit fucking around, gosh. "
        try:
            choice = int(choice)
        except ValueError:
            continue
        if 0 < choice <= len(question_data["answers"]):
            break
    
    # A valid answer has been selected, log the scores
    answer_str = answers[choice-1]
    scores.append(question_data["answers"][answer_str])

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
    score_avg[stat] = round(value / question_count)

# Accumulate differences between each character and the user
character_path = Path("characters/")
character_diffs = []
for char_file in character_path.iterdir():
    with open(char_file) as f:
        character_data = json.load(f)

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
print(f"Mazel tov, Max! Your Rose Family Personality Type is {personality_type} !")
print("You are:")
for name, percent in sorted(user_character_percentages.items(), key=lambda kv: kv[1], reverse=True):
    print(f"{round(percent * 100)}% {name} Rose")
