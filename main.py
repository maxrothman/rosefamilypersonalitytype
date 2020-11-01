import json
from pathlib import Path

# inventory each file in question folder and create function which calls each question

scores = []

question_path = Path('questions/')
question_count = len(list(question_path.iterdir()))
for path in sorted(question_path.iterdir()):
    with open(path) as f:
        question_data = json.loads(f.read())
    print(question_data["question"])
    # could use an ARRAY of objects instead
    number = 1
    answers = list(question_data["answers"].keys())
    for answer in answers:
        print(str(number) + ". " + answer)
        number = number+1
    prompt = "Input answer number: "
    while True:
        choice = input(prompt)
        prompt = "Quit fucking around, gosh. "
        try:
            choice = int(choice)
        except ValueError:
            continue
        if 0 < choice < len(question_data["answers"]) + 1:
            break
    answer_str = answers[choice-1]
    scores.append(question_data["answers"][answer_str])
score_total = {
        "lovability": 0,
        "selfishness": 0,
        "lovable selfishness": 0,
        "entrepeneurship": 0,
        "modesty": 0,
        "entitlement": 0,
        "wit": 0,
        }
for index in range(len(scores)):
    for key, value in scores[index].items():
        score_total[key] = score_total[key] + value
for stat, value in score_total.items():
    # what the fuck is going on here; why does score_total[stat] output it's value
    score_cotal[stat] = round(value / questionCount)
character_path = Path("characters/")
character_scores = []
character_number = 0
for char_file in character_path.iterdir():
    with open(char_file) as f:
        character_data = json.loads(f.read())
    character_scores.append(dict(name = character_data["name"]))
    character_scores[character_number].update(total = 0)
    character_scores[character_number].update(user = True)
    # for each character, you are compared, and given a closeness score
    for key, value in character_data.items():
        if type(value) is str:
            continue
        else:
            character_scores[character_number][key] = abs(value - score_total[key])
    character_scores[character_number]["total"] = character_scores[character_number]["total"] + character_scores[character_number][key]
    character_number = character_number+1
score_total.update(dict(totalTotal = 0))
# calculate total of totals to perform percentage calculation
for each in character_scores:
    score_total["totalTotal"] = score_total["totalTotal"] + abs(10 - each["total"])
finalPercentages = {}
# assign percentage from each 1-10 score
for each in character_scores:
    percentage = str(round((10 - each["total"]) / score_total["totalTotal"] * 100))
    each["percentage"] = percentage
personality_type = str("")
for each in sorted(character_scores, key = lambda i: i["percentage"],reverse=True):
    personality_type = personality_type + each["name"][0]
print("Mazel tov, Max! Your Rose Family Personality Type is " + personality_type + "!")
print("You are:")
for each in sorted(character_scores, key = lambda i: i["percentage"],reverse=True):
    print(each["percentage"] + '% ' + each["name"] + " Rose")

# sometimes the percentages AND PERSONALITY TYPE are out of order! "DJAM" seems likely

