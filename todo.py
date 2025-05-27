import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    else:
        print("No tasks found. Starting with an empty task list.")
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}.{task[title]}[{status}]")


def add_task(tasks, title):
    tasks.append({"title": title, "completed": False})
    print(f"Addded task: {title}")


def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index][completed] = True
        print(f"Marked as completed: {tasks[index]['title']}")
    else:
        print("Task number is not valid nigga")


def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted task: {removed['title']}")
    else:
        print("Task number is not valid")
