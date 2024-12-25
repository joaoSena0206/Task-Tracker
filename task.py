import json


def getLastId():
    id = 0

    # Gets biggest id from the tasks
    try:
        tasks = json.loads(open("tasks.json").read())
        id = tasks[len(tasks) - 1]["id"]
    except:
        id = 1

    return id

def createTask(id, description, status, createdAt, updatedAt):



