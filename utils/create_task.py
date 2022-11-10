import requests

URL = "http://127.0.0.1:5000/tasks"

def create_task(title, subtitle, body):
    task_data = {
        "title": title,
        "subtitle": subtitle,
        "body": body
    }
    response = requests.post(URL, json=task_data)
    if response.status_code == 201:
        print("Operation successful!")
    else:
        print("Something went wrong while trying to create task.")



if __name__ == "__main__":
    print("Create a new task by filling out the fields below.")
    title = input("Title: ")
    subtitle = input("Subtitle: ")
    body = input("Body: ")
    create_task(title, subtitle, body)

