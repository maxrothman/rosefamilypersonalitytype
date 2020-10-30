import json
from pathlib import Path

# inventory each file in question folder and create function which calls each question

scores = []

questionPath = (Path('questions/'))
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
        if 0 < choice < len(questionData["answers"]):
            break
    answerStr = answers[choice-1]
    scores.append(questionData["answers"][answerStr])


