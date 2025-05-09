def task():
    tasks = []
    print("-" * 30)
    print("------Welcome to To-do list-------")

    total_task = int(input("Enter your total task you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter your task {i} = ")
        tasks.append({"task": task_name, "done": False})

    print("\nToday's Tasks:")
    for idx, task in enumerate(tasks,1):
        status = "✓" if task["done"] else "✗"
        print(f"{idx}. [{status}] {task['task']}")

    while True:
        operation = int(input("\nWhat do you want to do?\n" "1 - Add\n" "2 - Update\n" "3 - Delete\n" "4 - View\n" "5 - Exit\n" "6 - Mark task as done\n" "Choose an option: "))

        if operation == 1:
            new_task = input("Enter your new task = ")  # FIXED
            tasks.append({"task": new_task, "done": False})
            print("Task has been added successfully.")

        elif operation == 2:
            update_val = input("Enter the task name you want to update: ")
            found = False
            for task in tasks:
                if task["task"] == update_val:
                    update_new_val = input("Enter the new task: ")
                    task["task"] = update_new_val
                    print(f"Task updated to: {update_new_val}")
                    found = True
                    break
            if not found:
                print("Task not found.")

        elif operation == 3:
            del_task = input("Enter the task to delete: ")
            found = False
            for task in tasks:
                if task["task"] == del_task:
                    tasks.remove(task)
                    print("Task has been removed.")
                    found = True
                    break
                if not found:
                  print("Task not found.")

        elif operation == 4:
            print("\nYour Current Tasks:")
            for idx, task in enumerate(tasks, 1):
                status = "✓" if task["done"] else "✗"
                print(f"{idx}. [{status}] {task['task']}")

        elif operation == 5:
             print("Goodbye! Your to-do list session has ended.")
             break
        elif operation == 6:
            done_task_name = input("Enter the task you completed: ")
            found = False
            for task in tasks:
                if task["task"] == done_task_name:
                    task["done"] = True
                    print(f"'{done_task_name}' marked as done. ✅")
                    found = True
                    break
            if not found:
                print("Task not found.")
        else:
            print("Invalid option. Please choose a number from 1 to 5.")    


task()
