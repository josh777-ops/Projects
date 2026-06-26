from datetime import datetime

def load_users():
    users = {}
    with open("user.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(", ")
            users[username] = password
    return users


def login(users):
    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == password:
            print("Login successful!\n")
            return username
        else:
            print("Invalid username or password. Try again.\n")

def reg_user(users):
    while True:
        new_username = input("Enter new username: ")

        if new_username in users:
            print("Username already exists. Choose another.\n")
            continue

        new_password = input("Enter new password: ")
        confirm_password = input("Confirm password: ")

        if new_password != confirm_password:
            print("Passwords do not match!\n")
            continue

        with open("user.txt", "a") as file:
            file.write(f"\n{new_username}, {new_password}")

        users[new_username] = new_password
        print("User registered successfully!\n")
        break

def add_task(users):
    assigned_user = input("Assign task to: ")

    if assigned_user not in users:
        print("User does not exist.\n")
        return
    
    title = input("Task title: ")
    description = input("Task description: ")
    due_date = input("Due date (e.g. 20 Mar 2026): ")

    current_date = datetime.today().strftime("%d %b %Y")

    with open("tasks.txt", "a") as file:
        file.write(f"\n{assigned_user}, {title}, {description}, "
                   f"{current_date}, {due_date}, No")
        
    print("Task added successfully!\n")

def view_all():
    with open("tasks.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            task = line.split(", ")

            if len(task) != 6:
                continue

            print_task(task)
            
def view_mine(current_user):
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    user_tasks = []

    for i, line in enumerate(tasks):
        task = line.strip().split(", ")
        if task[0] == current_user:
            print(f"\nTask Number: {i}")
            print_task(task)
            user_tasks.append(i)

    if not user_tasks:
        print("You have no tasks assigned.\n")
        return

    task_choice = input("Enter task number to edit OR -1 to return: ")

    if task_choice == "-1":
        return

    try:
        task_choice = int(task_choice)

        if task_choice not in user_tasks:
            print("Invalid task number.\n")
            return

        selected_task = tasks[task_choice].strip().split(", ")

        if selected_task[5] == "Yes":
            print("Completed tasks cannot be edited.\n")
            return

        action = input("Enter 'c' to mark complete or 'e' to edit: ")

        if action == "c":
            selected_task[5] = "Yes"

        elif action == "e":
            new_user = input("Enter new username (leave blank to keep same): ")
            new_due = input("Enter new due date (leave blank to keep same): ")

            if new_user:
                selected_task[0] = new_user
            if new_due:
                selected_task[4] = new_due

        tasks[task_choice] = ", ".join(selected_task) + "\n"

        with open("tasks.txt", "w") as file:
            file.writelines(tasks)

        print("Task updated successfully!\n")

    except ValueError:
        print("Please enter a valid number.\n")

def view_completed():
    with open("tasks.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            task = line.split(", ")

            if len(task) != 6:
                continue

            if task[5] == "Yes":
                print_task(task)

def generate_reports(users):
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    total_tasks = len(tasks)
    completed = 0
    overdue = 0
    today = datetime.today()

    for line in tasks:
        task = line.strip().split(", ")

        if task[5] == "Yes":
            completed += 1

        due_date = datetime.strptime(task[4], "%d %b %Y")

        if task[5] == "No" and due_date < today:
            overdue += 1

    incomplete = total_tasks - completed

    with open("task_overview.txt", "w") as file:
        file.write(f"Total tasks: {total_tasks}\n")
        file.write(f"Completed tasks: {completed}\n")
        file.write(f"Incomplete tasks: {incomplete}\n")
        file.write(f"Overdue tasks: {overdue}\n")

    with open("user_overview.txt", "w") as file:
        file.write(f"Total users: {len(users)}\n")
        file.write(f"Total tasks: {total_tasks}\n\n")

        for user in users:
            user_task_count = 0
            user_completed = 0

            for line in tasks:
                task = line.strip().split(", ")
                if task[0] == user:
                    user_task_count += 1
                    if task[5] == "Yes":
                        user_completed += 1

            file.write(f"{user}: {user_task_count} tasks assigned\n")

    print("Reports generated successfully!\n")

def delete_task():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    for i, line in enumerate(tasks):
        line = line.strip()
        if not line:
            continue

        task = line.split(", ")
        if len(task) != 6:
            continue

        print(f"{i}. {task[1]} (Assigned to {task[0]})")

    try:
        task_number = int(input("Enter task number to delete: "))

        if 0 <= task_number < len(tasks):
            tasks.pop(task_number)

            with open("tasks.txt", "w") as file:
                file.writelines(tasks)

            print("Task deleted successfully!\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Enter a valid number.\n")


def display_statistics(users):
    try:
        with open("task_overview.txt", "r") as file:
            print("\nTask Overview\n")
            print(file.read())

        with open("user_overview.txt", "r") as file:
            print("User Overview\n")
            print(file.read())

    except FileNotFoundError:
        print("Reports not found. Generating now...\n")
        generate_reports(users)
        display_statistics(users)

def print_task(task):
    print(f"""
-----------------------------------------------
Assigned to:      {task[0]}
Title:            {task[1]}
Description:      {task[2]}
Date Assigned:    {task[3]}
Due Date:         {task[4]}
Completed:        {task[5]}
-----------------------------------------------
""")

users = load_users()
current_user = login(users)

while True:

    if current_user == "admin":
        menu = input("""
Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete a task
gr - generate reports
ds - display statistics
e - exit
: """).lower()
    else:
        menu = input("""
Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: """).lower()

    if menu == 'r' and current_user == "admin":
        reg_user(users)

    elif menu == 'a':
        add_task(users)

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine(current_user)

    elif menu == 'vc' and current_user == "admin":
        view_completed()

    elif menu == 'del' and current_user == "admin":
        delete_task()

    elif menu == 'gr' and current_user == "admin":
        generate_reports(users)

    elif menu == 'ds' and current_user == "admin":
        display_statistics(users)

    elif menu == 'e':
        print("Goodbye!")
        break

    else:
        print("Invalid option.\n")



