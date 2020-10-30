import json
from pathlib import Path

# inventory each file in question folder and create function which calls each question

questionPath = (Path('questions/'))
questionCount = len(list(questionPath.iterdir()))
for path in sorted(questionPath.iterdir()):
    with open(path) as f:
        questionData = json.loads(f.read())
        print(questionData["question"])
        # could use an ARRAY of objects instead
        number = 1
        for answer in questionData["answers"].keys():
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

# prepend each answer option with letter in alphabetical order, and print
