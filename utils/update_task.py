import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def update_task(pk, title, subtitle, body):
    task_dictionary = {
        "title": title,
        "subtitle": subtitle,
        "body": body
    }

    url = "%s/%s" % (BASE_URL, pk)
    response = requests.put(url, json=task_dictionary)
    if response.status_code == 204:
        print("Update successful.")
    else:
        print("Something went wrong while updating.")


if __name__ == "__main__":
    task_id = input("Target task id: ")
    title = input("New title: ")
    subtitle = input("New subtitle: ")
    body = input("New task body: ")
    update_task(task_id, title, subtitle, body)