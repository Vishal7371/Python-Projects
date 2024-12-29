# Task List
tasks = []

# Display Menu
def show_menu():
    print("\nTO-DO List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

# Add Task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")
    print(f"DEBUG: Current tasks = {tasks}")  # Debugging print

# View Tasks
def view_tasks():
    print(f"DEBUG: Function view_tasks() called. Current tasks = {tasks}")  # Debugging print
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Delete Task
def delete_task():
    if not tasks:
        print("\nNo tasks to delete.")
        return
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted successfully!")
            print(f"DEBUG: Current tasks after deletion = {tasks}")  # Debugging print
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

# Main Function
def main():
    print("DEBUG: Program started.")  # Debugging print
    while True:
        show_menu()
        try:
            choice = input("Enter your choice (1-4): ")
            print(f"DEBUG: User entered choice = {choice}")  # Debugging print
            choice = int(choice)
            if choice == 1:
                view_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("Goodbye!")
                print(f"DEBUG: Exiting program. Final tasks = {tasks}")  # Debugging print
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Run the Program
if __name__ == "__main__":
    main()
