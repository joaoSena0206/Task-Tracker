import json


def getLastId():
    tasks = open("tasks.json")
    id = 0

    # Gets biggest id from the tasks
    try:
        tasksDict = json.load(tasks)
        id = tasksDict[len(tasksDict) - 1]["id"] + 1
    except:
        id = 1
    finally:
        tasks.close()

    return id

def createTask(description, status, createdAt, updatedAt):
    tasks = open("tasks.json")
    fileRead = tasks.read()
    tasksList = []
    task = {
            "id": getLastId(),
            "description": description,
            "status": status,
            "createdAt": createdAt,
            "updatedAt": updatedAt
        }

    # Checks if any task exists to prevent error
    if len(fileRead) != 0:
        tasksList = json.loads(fileRead)

    # Adds task to JSON
    tasks = open("tasks.json", "w")

    tasksList.append(task)
    tasks.write(json.dumps(tasksList))

    tasks.close()


createTask("Teste", "done", "2024-12-25", "2024-12-25")