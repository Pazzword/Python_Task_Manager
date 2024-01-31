# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"
border = "-" * 60
borderXL = "-" * 68


# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    # Define admin credentials
    admin_user = "admin"
    admin_password = "password"
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")

    if curr_user == admin_user and curr_pass == admin_password:
        print("✅ Admin Login Successful!")
    # Add admin-specific logic here if needed
        logged_in = True

    if curr_user not in username_password.keys():
        print("❌ User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("❌ Wrong password")
        continue
    else:
        print("✅ Login Successful!")
        logged_in = True

def reg_user():
    while True:
        print(f"\t{borderXL}")
        new_username = input("\t\tNew Username: ")

        # Check if the username already exists
        if new_username in username_password:
            print(f"\t{borderXL}")
            print("\t\t❌ Username already exists. Please choose a different username.")
            print("\t\t   Or enter 'e' to return to the Main Menu")
            print(f"\t{borderXL}")
        elif new_username == 'e':
            return
        else:
            break

    new_password = input("\t\tNew Password: ")
    confirm_password = input("\t\tConfirm Password: ")

    if new_password == confirm_password:
        print("\n\t\t✅ New user added successfully!")
        username_password[new_username] = new_password

        # Write all user data to the file
        with open("user.txt", "a") as out_file:
            out_file.write(f"\n{new_username};{new_password}")
    else:
        print("\t\t❌ Password confirmation failed. User not added.")

def add_task():        
        print(f"\t{borderXL}")
        task_username = input("\t\tName of person assigned to task: ")
        if task_username not in username_password.keys():
            print(f"\t{borderXL}")
            print("\t\t❌ User does not exist. Please enter a valid username")
            return add_task()
            
        print(f"\t{borderXL}")
        task_title = input("\t\tTitle of Task: ")
        print(f"\t{borderXL}")
        task_description = input("\t\tDescription of Task: ")
        while True:
            try:
                print(f"\t{borderXL}")
                task_due_date = input("\t\tDue date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print(f"\t{borderXL}")
                print("\t❌ Invalid datetime format. Please use the format specified")
                print(f"\t{borderXL}")
        
        # Then get the current date.
        curr_date = date.today()
        ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.'''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print(f"\t{borderXL}")
        print("\t\t✅ Task successfully added.")
        print(f"\t{borderXL}")

def view_all():
        for t in task_list:
            
            disp_str = f"Task: \t\t{t['title']}\n"
            disp_str += f"\t\tAssigned to: \t{t['username']}\n"
            disp_str += f"\t\tDate Assigned: \t{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"\t\tDue Date: \t{t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"\t\tDescription: \n\t\t{t['description']}\n"
            disp_str += f"\t\tStatus: \t{'Completed' if t['completed'] else 'Pending'}\n"
            print(f"\t\t{border}")
            print(f"\t\t{disp_str}")

def display_tasks(user_tasks):
    for i, t in enumerate(user_tasks, start=1):
        border = "-" * 60
        disp_str = f"\t\t{border}\n"
        disp_str += f"📍TASK {i}:\n"
        disp_str += f"\t\tTitle: \t\t {t['title']}\n"
        disp_str += f"\t\tAssigned to: \t {t['username']}\n"
        disp_str += f"\t\tDate Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"\t\tDue Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"\t\tDescription: {t['description']}\n"
        completion_status = "✅ Completed" if t['completed'] else "❗️ Pending"  # Updated this line
        disp_str += f"\n\t\tStatus: \t {completion_status}\n"
        disp_str += f"\t\t{border}\n"

        print(disp_str)

def view_mine():
    user_tasks = [t for t in task_list if t['username'] == curr_user]

    display_tasks(user_tasks) #

    while True:
        if logged_in and curr_user:
            print("\t\t🟢 Enter the number of the task to select")
            selected_task_number = input("\t\t  (or -1 to return to the main menu): ")
            print(f"\t\t{border}")
            try:
                selected_task_number = int(selected_task_number)

                if selected_task_number == -1:
                    return

                if 1 <= selected_task_number <= len(user_tasks):
                    selected_task = user_tasks[selected_task_number - 1]
                    print(border)
                    print(f"Selected Task {selected_task_number}:\n")
                    print(f"Title: \t\t {selected_task['title']}")
                    print(f"Assigned to: \t {selected_task['username']}")
                    print(f"Date Assigned: \t {selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
                    print(f"Due Date: \t {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
                    print(f"Task Description: \n {selected_task['description']}")
                    print(f"Completed: \t { 'Completed' if selected_task['completed'] else 'Pending' }")
                    print(border)

                    operation = input(f'''
            {border}
                    TASK VIEW MENU
            Select one of the following Options below:
            {border}
            ✅ c -  Mark the task as completed
            🖌  e -  Edit the task
            ❌ d -  Delete the task

            Or press 'Enter' to return to "View my tasks"
            {border}
            : ''').lower()

                    if operation == 'c':
                        selected_task['completed'] = True
                        save_tasks_to_file(task_list)  # Pass the entire task_list
                        print()
                        print(f"\t{borderXL}")
                        print("\t\t✅ Task marked as completed.")
                        print(f"\t{borderXL}")
                        break
                    elif operation == 'e' and not selected_task.get('completed', False):
                        # Placeholder code for editing the task
                        update_task(selected_task)
                    elif operation == 'd':
                        # Placeholder code for deleting the task
                        print("\t\t❌ Deleting task...")
                    else:
                        print("\nSorry but this option does not exist.")
                else:
                    print("\t\t❌ Sorry but this number does not exist.")
                    print("\t\t❌ Please enter a correct number.")
                    print(f"\t\t{border}")
            except ValueError:
                print("\t\t❌ Invalid input. Please enter a valid number.")
                print(f"\t\t{border}")
        else:
            print("\nSorry but this option does not exist.")




def save_tasks_to_file(tasks):
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in tasks:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))





def update_task(selected_task):
    try:
        new_title = input(f"\t\tEnter a new title for the task: ")
        selected_task['title'] = new_title

        update_due_date = input("\t\tDo you want to update the due date? (y/n): ").lower()

        if update_due_date == 'y':
            new_due_date_str = input("\t\tEnter a new Due Date (YYYY-MM-DD): ")
            new_due_date = datetime.strptime(new_due_date_str, DATETIME_STRING_FORMAT)
            selected_task['due_date'] = new_due_date

        # Update the completion status
        mark_completed = input("\t\tMark the task as completed? (y/n): ").lower()
        selected_task['completed'] = mark_completed == 'y' or mark_completed == 'yes'

        # Save the updated task_list to the file
        save_tasks_to_file(task_list)

        print("\t\t✅ Your task updated successfully.")

    except ValueError:
        print("\t\t❌ Invalid input. Please enter a valid value.")


def delete_task():
    while True:
        try:
            task_num = int(input("Enter the number of the task to delete: "))
            deleted_task = task_list.pop(task_num - 1)
        except (ValueError, IndexError):
            print("Invalid task number. Please enter a valid number.")
            return

        print(f"Task {task_num} deleted successfully.")
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))

def generate_reports():
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task.get('completed', False))
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in task_list if not task.get('completed', False) and task['due_date'] < datetime.now())

    # Calculate percentages
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    overdue_percentage = (overdue_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    # Extract unique usernames from tasks
    unique_usernames = set(task['username'] for task in task_list)
    print(f"\t\t{border}")
    print("\t\t✅ Report generated Successfully!")
    print("\t\t   This report is now available under Display Statistics - 'ds'")
    print(f"\t\t{border}")
    print(f'''
                        📉 USER OVERVIEW:
                {border}
                📙 Total Users: \t\t{len(unique_usernames)}''')
    for username in unique_usernames:
        tasks_count = len([task for task in task_list if task['username'] == username])
        print(f"\t\t🧸 {username} tasks:\t{tasks_count}")

    print(f'''\n
                        📈 TASK OVERVIEW:
                {border}
                ✅  Total Tasks:\t\t\t{total_tasks}
                ✅  Completed Tasks:\t\t{completed_tasks}
                ❌ Uncompleted Tasks:\t\t{uncompleted_tasks}
                ❌ Overdue Tasks:\t\t\t{overdue_tasks}
                ❌ Incomplete Percentage:\t\t{incomplete_percentage:.2f}%
                ❌ Overdue Percentage:\t\t{overdue_percentage:.2f}%
    ''')

    # Write to user_overview.txt
    with open('user_overview.txt', 'w') as user_file:
        user_file.write(f"\t{border}\n")
        user_file.write(f"\t\t\t📉 User Overview\n\n")
        user_file.write(f"\t\t📙 Total Users:\t{len(unique_usernames)}\n")
        user_file.write(f"\t\t📗 Tasks per User:\n")
        for username in unique_usernames:
            tasks_count = len([task for task in task_list if task['username'] == username])
            user_file.write(f"\t\t\t🧸 {username}:\t{tasks_count} tasks\n")
        user_file.write(f"\t{border}")

    # Write to task_overview.txt
    with open('task_overview.txt', 'w') as task_file:
        task_file.write(f"\t\t\t📈 Task Overview\n\n")
        task_file.write(f"\t\t✅ Total Tasks: {total_tasks}\n")
        task_file.write(f"\t\t✅ Completed Tasks: {completed_tasks}\n")
        task_file.write(f"\t\t❌ Uncompleted Tasks: {uncompleted_tasks}\n")
        task_file.write(f"\t\t❌ Overdue Tasks: {overdue_tasks}\n")
        task_file.write(f"\t\t❌ Incomplete Percentage: {incomplete_percentage:.2f}%\n")
        task_file.write(f"\t\t❌ Overdue Percentage: {overdue_percentage:.2f}%\n")

def display_statistics():
    while True:
        if curr_user == admin_user:
            # Check if the reports exist, if not generate them
            if not os.path.exists('user_overview.txt') or not os.path.exists('task_overview.txt'):
                generate_reports()

            # Display the contents of user_overview.txt
            with open('user_overview.txt', 'r') as user_file:
                print(user_file.read())

            # Display the contents of task_overview.txt
            with open('task_overview.txt', 'r') as task_file:
                print(task_file.read())
            break



while True:   
    if logged_in:
        if curr_user == admin_user:
            
            menu = input(f'''
                         MAIN MENU
            Select one of the following Options below:
            {border}
            🔐 r  -  Registering a user
            📥 a  -  Adding a task
            🔎 va -  View all tasks
            🗓  vm -  View my task
            📈 gr -  Generate reports
            📊 ds -  Display statistics
            ❌ e  -  Exit
            {border}
            : ''').lower()
        else:
            menu = input(f'''
                        MAIN MENU
            Select one of the following Options below:
            {border}            
            🔐 r  -  Registering a user
            📥 a  -  Adding a task
            🔎 va -  View all tasks
            🗓  vm -  View my task
            📊 ds -  Display statistics
            ❌ e  -  Exit
            {border}
            : ''').lower()

        if menu == 'r':
            reg_user()
        
        elif menu == 'a':
            add_task()
      
        elif menu == 'va':
            view_all()
        
        elif menu == 'vm':
            view_mine()

        elif menu == 'gr' and curr_user == admin_user:
            generate_reports()

        elif menu == 'ds' and curr_user == admin_user:
            display_statistics()
                    
        elif menu == 'ds' and curr_user: 
            print(f"\t{borderXL}")
            print(f"\t\t❌ Sorry. But this option is for the admin access only.")
            print(f"\t{borderXL}")

        elif menu == 'e':
            print('\t\t\t👋 Goodbye!!!👋 ')
            exit()

        else:
            print(f"\t{borderXL}")
            print("\t\t❌ This menu option is not recognised. Please Try again")
            print(f"\t{borderXL}")
    else:
        print("-----------------------------------")
        print("Error: No user information available")
        print("-----------------------------------")
