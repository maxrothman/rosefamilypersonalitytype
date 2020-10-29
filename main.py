import json

with open("questions/question1.json") as f:
    questiondata = json.loads(f.read())
    print(questiondata["question"])
