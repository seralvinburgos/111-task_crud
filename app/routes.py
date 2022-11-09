from flask import Flask
from app.database import task

app = Flask(__name__)


@app.get("/tasks")
def get_all_tasks():
    out = {}
    response = task.scan()
    out["tasks"] = response
    return out