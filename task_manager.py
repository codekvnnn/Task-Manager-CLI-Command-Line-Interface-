import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for index, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{index + 1}. {status} {task['task']}")

def complete_task(task_number):
    tasks = load_tasks()
    tasks[task_number - 1]["completed"] = True
    save_tasks(tasks)

def delete_task(task_number):
    tasks = load_tasks()
    tasks.pop(task_number - 1)
    save_tasks(tasks)

if __name__ == "__main__":
    while True:
        print("\nTask Manager CLI")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark as completed: "))
            complete_task(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            break
