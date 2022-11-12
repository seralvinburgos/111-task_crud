from flask import Flask, request
from app.database import task

app = Flask(__name__)


@app.get("/tasks")
def get_all_tasks():
    out = {}
    response = task.scan()
    out["tasks"] = response
    return out


@app.get("/tasks/<int:pk>")
def get_one_task(pk):
    out = {}
    response = task.select_by_id(pk)
    out["task"] = response[0]
    return out


@app.post("/tasks")
def create_task():
    out = {"status": "ok"}
    task_data = request.json
    task.insert(task_data)
    return out, 201


@app.put("/tasks/<int:pk>")
def update_task(pk):
    task_data = request.json
    task.update(pk, task_data)
    return "", 204


@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete(pk)
    return "", 204
