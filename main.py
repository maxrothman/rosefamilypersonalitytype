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
characterScores = []
characterNumber = 0
for charFile in characterPath.iterdir():
    with open(charFile) as f:
        characterData = json.loads(f.read())
    characterScores.append(dict(name = characterData["name"]))
    characterScores[characterNumber].update(total = 0)
    characterScores[characterNumber].update(user = True)
    # for each character, you are compared, and given a closeness score
    for key, value in characterData.items():
        if type(value) is str:
            continue
        else:
            characterScores[characterNumber][key] = abs(value - scoreTotal[key])
    characterScores[characterNumber]["total"] = characterScores[characterNumber]["total"] + characterScores[characterNumber][key]
    characterNumber = characterNumber+1
scoreTotal.update(dict(totalTotal = 0))
# calculate total of totals to perform percentage calculation
for each in characterScores:
    scoreTotal["totalTotal"] = scoreTotal["totalTotal"] + abs(10 - each["total"])
finalPercentages = {}
# assign percentage from each 1-10 score
for each in characterScores:
    percentage = str(round((10 - each["total"]) / scoreTotal["totalTotal"] * 100))
    each["percentage"] = percentage
personalityType = str("")
for each in sorted(characterScores, key = lambda i: i["percentage"],reverse=True):
    personalityType = personalityType + each["name"][0]
print("Mazel tov, Max! Your Rose Family Personality Type is " + personalityType + "!")
print("You are:")
for each in sorted(characterScores, key = lambda i: i["percentage"],reverse=True):
    print("%" + each["percentage"] + " " + each["name"])

# sometimes the percentages AND PERSONALITY TYPE are out of order! "DJAM" seems likely

