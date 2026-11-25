def todo_list():
    tasks = []

    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            title = input("Enter task name: ")
            tasks.append({"title": title, "done": False})
            print("Task added successfully!")

        elif choice == '2':
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\n--- YOUR TASKS ---")
                for idx, task in enumerate(tasks, start=1):
                    status = "Done" if task["done"] else "Pending"
                    print(f"{idx}. {task['title']} [{status}]")

        elif choice == '3':
            if not tasks:
                print("No tasks available to update.")
            else:
                try:
                    num = int(input("Enter task number to update: "))
                    if 1 <= num <= len(tasks):
                        new_title = input("Enter new task name: ")
                        tasks[num - 1]["title"] = new_title
                        print("Task updated successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '4':
            if not tasks:
                print("No tasks available.")
            else:
                try:
                    num = int(input("Enter task number to mark as completed: "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["done"] = True
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '5':
            if not tasks:
                print("No tasks available to delete.")
            else:
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Deleted task: {removed['title']}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    todo_list()