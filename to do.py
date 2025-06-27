import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})

def show_tasks(tasks):
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else "✗"
        print(f"{i+1}. [{status}] {t['task']}")

def mark_done(tasks):
    show_tasks(tasks)
    i = int(input("Enter task number to mark done: ")) - 1
    if 0 <= i < len(tasks):
        tasks[i]["done"] = True

def delete_task(tasks):
    show_tasks(tasks)
    i = int(input("Enter task number to delete: ")) - 1
    if 0 <= i < len(tasks):
        tasks.pop(i)

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Mark Done\n4. Delete Task\n5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break

if __name__ == "__main__":
    main()
