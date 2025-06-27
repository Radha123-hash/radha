# to_do_list.py

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully!")

def update_task():
    view_tasks()
    task_no = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_no < len(tasks):
        new_task = input("Enter the new task description: ")
        tasks[task_no] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_no = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks.pop(task_no)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
