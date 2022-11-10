import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def delete_task(pk):
    task_dictionary = {
        "id": task_id
    }

    url = "%s/%s" % (BASE_URL, pk)
    response = requests.put(url, json=task_dictionary)
    if response.status_code == 204:
        print("Task Deleted")
    else:
        print("Something went wrong while trying to delete.")


if __name__ == "__main__":
    task_id = input("Target task id: ")
    delete_task(task_id)
