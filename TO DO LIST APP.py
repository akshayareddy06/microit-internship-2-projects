# Define the main function to run the to-do list app
def todo_app():
    tasks = []  # This list will store all the tasks as dictionaries

    # Function to print all tasks in a user-friendly way
    def display_tasks():
        if not tasks:  # If task list is empty
            print("No tasks available.")
            return
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks, start=1):  # Loop through tasks with numbering
            status = "✅" if task["completed"] else "NOT COMPLETED"  # Show checkmark if completed
            print(f"{i}. [{status}] {task['title']} | Category: {task['category']} | Priority: {task['priority']}")

    # Welcome message
    print("📋 Welcome to the TO-DO LIST APP")

    # Start the loop for user interaction
    while True:
        # Menu options
        print("\nChoose an action:")
        print("1 - Add Task")
        print("2 - Edit Task")
        print("3 - Mark Task as Complete")
        print("4 - Delete Task")
        print("5 - View Tasks")
        print("6 - Exit")

        # Input choice from user
        try:
            choice = int(input("Enter your choice (1-6): "))  # Convert input to integer
        except ValueError:
            print("Please enter a valid number.")  # Handle non-integer inputs
            continue  # Go back to menu

        # Option 1 - Add a new task
        if choice == 1:
            title = input("Enter task title: ")  # Ask for task name
            category = input("Enter category (e.g., Work, Personal, Study): ")  # Task category
            priority = input("Enter priority (High/Medium/Low): ")  # Task priority

            # Create task dictionary with required fields
            task = {
                "title": title,
                "category": category,
                "priority": priority,
                "completed": False  # Initially not completed
            }

            tasks.append(task)  # Add task to the list
            print(f"Task '{title}' added successfully.")  # Confirm addition

        # Option 2 - Edit an existing task
        elif choice == 2:
            display_tasks()  # Show all tasks
            try:
                task_num = int(input("Enter task number to edit: "))  # Ask user which task to edit
                if 1 <= task_num <= len(tasks):  # Valid number check
                    new_title = input("Enter new title: ")  # Get new values
                    new_category = input("Enter new category: ")
                    new_priority = input("Enter new priority: ")
                    # Update values in the selected task
                    tasks[task_num - 1]["title"] = new_title
                    tasks[task_num - 1]["category"] = new_category
                    tasks[task_num - 1]["priority"] = new_priority
                    print("Task updated successfully.")  # Confirm update
                else:
                    print("Invalid task number.")  # Handle wrong input
            except ValueError:
                print("Please enter a valid number.")  # Non-integer error

        # Option 3 - Mark task as complete
        elif choice == 3:
            display_tasks()  # Show all tasks
            try:
                task_num = int(input("Enter task number to mark as complete: "))  # Get number
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True  # Set completed to True
                    print("Task marked as complete.")  # Confirm
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        # Option 4 - Delete a task
        elif choice == 4:
            display_tasks()  # Show all tasks
            try:
                task_num = int(input("Enter task number to delete: "))  # Get number
                if 1 <= task_num <= len(tasks):
                    deleted = tasks.pop(task_num - 1)  # Remove task from list
                    print(f"Task '{deleted['title']}' deleted.")  # Confirm deletion
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        # Option 5 - View all tasks
        elif choice == 5:
            display_tasks()  # Just call the display function

        # Option 6 - Exit the app
        elif choice == 6:
            print("Exiting To-Do List. Have a productive day!")  # Goodbye message
            break  # End the loop and program

        # Handle invalid choices
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

# Call the function to run the app
todo_app()
#ALL THE WORKING PRINCIPLES ARE EXPLAINED CLEARLY ABOVE WITH ##########
# I FEEL I HAVE EXPLAINED EVERYTHING#
