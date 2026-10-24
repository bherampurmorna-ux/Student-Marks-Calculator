print("===== To-Do List =====")

tasks = []  # each task is stored as [task_name, is_done]

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter task: ")
        tasks.append([name, False])
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                status = "Done" if tasks[i][1] else "Pending"
                print(f"{i + 1}. {tasks[i][0]} [{status}]")

    elif choice == "3":
        number = int(input("Enter task number to mark done: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1][1] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-5.")