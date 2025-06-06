import json
import os

FILE = "data/tasks.json"

def load_tasks():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump([], f)
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)
