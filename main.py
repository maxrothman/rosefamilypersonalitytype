import json
from pathlib import Path

# inventory each file in question folder and create function which calls each question

scores = []

questionPath = Path('questions/')
questionCount = len(list(questionPath.iterdir()))
for path in sorted(questionPath.iterdir()):
    with open(path) as f:
        questionData = json.loads(f.read())
    print(questionData["question"])
    # could use an ARRAY of objects instead
    number = 1
    answers = list(questionData["answers"].keys())
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
        if 0 < choice < len(questionData["answers"]) + 1:
            break
answerStr = answers[choice-1]
scores.append(questionData["answers"][answerStr])
scoreTotal = {
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
        scoreTotal[key] = scoreTotal[key] + value
for stat, value in scoreTotal.items():
    # what the fuck is going on here; why does scoreTotal[stat] output it's value
    scoreTotal[stat] = round(value / questionCount)
characterPath = Path("characters/")
for charFile in characterPath.iterdir():
    with open(charFile) as f:
        characterData = json.loads(f.read())
    # for each character file create score for that character based on calculations
    tempName = str("score" + characterData["name"])
    exec("%s = %d" % (tempName,0))
    # for key, value in characterData.items():
        # print(str(characterData["name"] + "score"))
