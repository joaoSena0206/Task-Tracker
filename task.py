import json


def pegarUltimoId():
    tasks = open("tasks.json")
    id = 0

    # Pega o maior id das tasks
    try:
        tasksDict = json.load(tasks)
        id = tasksDict[len(tasksDict) - 1]["id"] + 1
    except:
        id = 1
    finally:
        tasks.close()

    return id

def criarTask(description, status, createdAt, updatedAt):
    tasks = open("tasks.json")
    fileRead = tasks.read()
    tasksList = []
    task = {
            "id": pegarUltimoId(),
            "description": description,
            "status": status,
            "createdAt": createdAt,
            "updatedAt": updatedAt
        }

    # Checa se existe alguma task para prevenir erro
    if len(fileRead) != 0:
        tasksList = json.loads(fileRead)

    # Adiciona a task ao arquivo json
    tasks = open("tasks.json", "w")

    tasksList.append(task)
    tasks.write(json.dumps(tasksList))

    tasks.close()


criarTask("Teste", "done", "2024-12-25", "2024-12-25")