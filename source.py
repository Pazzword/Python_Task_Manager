import os
from datetime import datetime, date
DATETIME_FORMAT = "%Y-%m-%d"
borderXS = "-" * 40
border = "-" * 60
borderXL = "-" * 68


def reg_user(username_password):
    while True:
        print(f"\t{borderXL}")
        new_username = input("\t\tNew Username: ")
    
        # Check if the username already exists
        if new_username in username_password:
            print(f"\t{borderXL}")
            print("\t❌ Username already exists. Please choose a different username.")
            print("\t   Or enter 'e' to return to the Main Menu")
        elif new_username == 'e':
            return # Return the updated dictionary (Count)
        else:
            break

    new_password = input("\t\tNew Password: ")
    confirm_password = input("\t\tConfirm Password: ")

    if new_password == confirm_password:
        print(f"\t{borderXL}")
        print("\n\t\t✅ New user added successfully!")
        print(f"\t{borderXL}")
        username_password[new_username] = new_password

        # Write all user data to the file
        with open("user.txt", "a") as out_file:
            out_file.write(f"\n{new_username};{new_password}")
    else:
        print("\n\t\t❌ Password confirmation failed. User not added.")

def add_task(username_password, task_list):        
        print(f"\t{borderXL}")
        task_username = input("\t\t🟡 Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print(f"\t{borderXL}")
            print("\t\t❌ User does not exist. Please enter a valid username")
            return add_task(username_password, task_list)
            
        print(f"\t{borderXL}")
        task_title = input("\t\t🟡 Title of Task: ")
        print(f"\t{borderXL}")
        task_description = input("\t\t🟡 Description of Task: ")
        while True:
            try:
                print(f"\t{borderXL}")
                task_due_date = input("\t\t🟡 Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_FORMAT)
                break

            except ValueError:
                print(f"\t{borderXL}")
                print("\n\t❌ Invalid datetime format. Please use the format specified\n")
        
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
                    t['due_date'].strftime(DATETIME_FORMAT),
                    t['assigned_date'].strftime(DATETIME_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print(f"\t{borderXL}")
        print("\t\t✅ Task successfully added.")
        print(f"\t{borderXL}")

def view_all(task_list):
        if os.path.getsize("tasks.txt") == 0:
                print(f"\t{borderXL}")
                print("\t⭕️ There are no tasks to display")
                print(f"\t{borderXL}")
        else:
            for t in task_list:
                disp_str = f"📍Task: \t{t['title']}\n"
                disp_str += f"\t\tAssigned to: \t{t['username']}\n"
                disp_str += f"\t\tDate Assigned: \t{t['assigned_date'].strftime(DATETIME_FORMAT)}\n"
                disp_str += f"\t\tDue Date: \t{t['due_date'].strftime(DATETIME_FORMAT)}\n"
                disp_str += f"\t\tDescription: \n\t\t{t['description']}\n"
                disp_str += f"\t\tStatus: \t{'✅ Completed' if t['completed'] else '❗️ Pending'}\n"
                print(f"\t{borderXL}")
                print(f"\t\t{disp_str}")

def display_tasks(user_tasks):
    for i, t in enumerate(user_tasks, start=1):
        disp_str = f"\t{borderXL}\n"
        disp_str += f"📍TASK {i}:\n"
        disp_str += f"\t\tTitle: \t\t {t['title']}\n"
        disp_str += f"\t\tAssigned to: \t {t['username']}\n"
        disp_str += f"\t\tDate Assigned: \t {t['assigned_date'].strftime(DATETIME_FORMAT)}\n"
        disp_str += f"\t\tDue Date: \t {t['due_date'].strftime(DATETIME_FORMAT)}\n"
        disp_str += f"\t\tDescription: \t {t['description']}\n"
        completion_status = "✅ Completed" if t['completed'] else "❗️ Pending"  # Updated this line
        disp_str += f"\n\t\tStatus: \t {completion_status}\n"
        disp_str += f"\t{borderXL}\n"

        print(disp_str)

def view_mine(task_list, curr_user, logged_in):
    if os.path.getsize("tasks.txt") == 0:
                print(f"\t{borderXL}")
                print("\t⭕️ There are no tasks to display")
                print(f"\t{borderXL}")
    else:
        user_tasks = [t for t in task_list if t['username'] == curr_user]
        selected_task = None  # Initialize selected_task outside the loop
        while True:
            display_tasks(user_tasks) # This could be placed above the loop. However after editing and deleting tasks the user won't be able to see task list again. 
            if logged_in and curr_user:
                print(f"\t{borderXL}")
                print("\n\t🔰 Enter the number of the task to select")
                selected_task_number = input("\t   or enter -1 to return to the main menu:   ")
                print(f"\n\t{borderXL}")
                try:
                    selected_task_number = int(selected_task_number)
                    if selected_task_number == -1:
                        return
                    
                    if 1 <= selected_task_number <= len(user_tasks):
                        selected_task = user_tasks[selected_task_number - 1]
                        print(f"\t{borderXL}")
                        print(f"\t\t🟢 SELECTED TASK {selected_task_number}:\n")
                        print(f"\t\tTitle: \t\t {selected_task['title']}")
                        print(f"\t\tAssigned to: \t {selected_task['username']}")
                        print(f"\t\tDate Assigned: \t {selected_task['assigned_date'].strftime(DATETIME_FORMAT)}")
                        print(f"\t\tDue Date: \t {selected_task['due_date'].strftime(DATETIME_FORMAT)}")
                        print(f"\t\tTask Description: \n\t\t {selected_task['description']}")
                        print(f"\t\tCompleted: \t { 'Completed' if selected_task['completed'] else 'Pending' }")
                        print(f"\t{borderXL}")

                        while True:
                            operation = input(f'''
            {borderXS}
                    TASK VIEW MENU
            Select one of the following Options below:
            {borderXS}
            ✅ c -    Mark the task as completed
            🖌  e -    Edit the task
            ❌ d -    Delete the task
            📤 s -    Select another task

            ❎ Or enter 'b' to return to the Main Menu"
            {borderXS}
            : ''').lower()

                            if operation == 'c':
                                selected_task['completed'] = True
                                save_tasks_to_file(task_list)  # Pass the entire task_list
                                print()
                                print(f"\t{borderXL}")
                                print("\n\t\t✅ Task marked as 'Completed'.\n")
                                print(f"\t{borderXL}")
                                break
                            elif operation == 'e' and not selected_task.get('completed', False):
                                # Placeholder code for editing the task
                                update_task(selected_task, task_list)
                            elif operation == 'e' and selected_task.get('completed', True):
                                print(f"\t{borderXL}")
                                print("\n\t❌ You cannot edit tasks that has been marked as 'Completed'\n")
                                print(f"\t{borderXL}")
                            elif operation == 'd':
                                delete_task(task_list, selected_task)
                                break
                            elif operation == 's':
                                break
                            elif operation =='b':
                                return
                            else:
                                print(f"\t{borderXL}")
                                print("\n\t\t❌ Sorry but this option does not exist.")
                                print("\n\t\t\tPlease enter correct option\n")
                                print(f"\t{borderXL}")
                                # After printing the message, continue to the next iteration
                                
                    else:
                        print("\n\t\t❌ Sorry but this task does not exist.")
                        print("\n\t\t❌ Please enter a correct task number.")
                        print(f"\n\t{borderXL}")
                        # After printing the message, continue to the next iteration
                        

                except ValueError:
                    print("\n\t\t❌ Incorrect input. Please enter a valid number.\n")
                    print(f"\t{borderXL}")

def save_tasks_to_file(tasks):
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in tasks:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_FORMAT),
                t['assigned_date'].strftime(DATETIME_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))

def update_task(selected_task, task_list):
    try:
        print(f"\t{borderXL}")
        new_title = input(f"\t\t🟡 Enter a new title for the task: ")
        selected_task['title'] = new_title

        print(f"\t{borderXL}")
        update_due_date = input("\t\t🟡 Do you want to update the due date? (y/n): ").lower()
        

        if update_due_date == 'y':
            while True:
                print(f"\t{borderXL}")
                new_due_date_str = input("\t\t🟡 Enter a new Due Date (YYYY-MM-DD): ")
                

                try:
                    new_due_date = datetime.strptime(new_due_date_str, DATETIME_FORMAT)
                    selected_task['due_date'] = new_due_date
                    break  # Exit the loop if the date is entered correctly

                except ValueError:
                    print(f"\t{borderXL}")
                    print("\n\t\t❌ Invalid date format. Please enter correct Due Date.\n")
                    

        elif update_due_date == 'n':
            pass  # Exit the loop if the user chooses not to update the date

        else:
            print(f"\t{borderXL}")
            print("\n\t\t❌ Invalid input. Please enter 'y' or 'n'.\n")
            return update_task(selected_task, task_list)

        # Update the completion status
        print(f"\t{borderXL}")
        mark_completed = input("\t\t🟡 Mark the task as completed? (y/n): ").lower()
        selected_task['completed'] = mark_completed == 'y' or mark_completed == 'yes'

        # Save the updated task_list to the file
        save_tasks_to_file(task_list)

        print(f"\t{borderXL}\n")
        print("\n\t\t✅ Your task updated successfully.\n")

    except ValueError:
        print(f"\t{borderXL}")
        print("\n\t\t❌ Invalid input. Please enter numerical value only.\n")

def delete_task(task_list, selected_task):
    task_list.remove(selected_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_FORMAT),
                t['assigned_date'].strftime(DATETIME_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
        print(f"\t{borderXL}")
        print("\n\t\t\t❌ This task DELETED\n")
        print("\n\t🟢 Your task list will refresh when you return to the Main Menu\n")
    return True
    
def generate_reports(task_list, username_password):

    unique_usernames = set(task['username'] for task in task_list)
    user_count = len(unique_usernames)

    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task.get('completed', False))
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in task_list if not task.get('completed', False) and task['due_date'] < datetime.now())

    # Calculate percentages
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    overdue_percentage = (overdue_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    # Extract unique usernames from tasks
    unique_usernames = set(task['username'] for task in task_list)
    

    print(f"\t{borderXL}")
    print("\n\t\t✅ Report generated Successfully!")
    print("\t  This report is now available under Display Statistics - 'ds'\n")
    print(f"\t{borderXL}")


    # Write to user_overview.txt
    with open('user_overview.txt', 'w') as user_file:
        user_file.write(f"\t{borderXL}\n")
        user_file.write(f"\t\t\t📉 User Overview 📉 \n\n")
        total_users = len(username_password)
        user_file.write(f"\t\t📙 Total Users:\t\t{total_users} Users\n") 
        user_file.write(f"\t\t📗 Tasks per User:\n\n")
        for username in unique_usernames:
            tasks_count = len([task for task in task_list if task['username'] == username])
            user_file.write(f"\t\t\t🎎 {username}:\t{tasks_count} tasks\n\n")

    # Write to task_overview.txt
    with open('task_overview.txt', 'w') as task_file:
        task_file.write(f"\t{borderXL}\n")
        task_file.write(f"\t\t\t📈 Task Overview 📈\n\n")
        task_file.write(f"\t\t✅ Total Tasks:\t\t\t{total_tasks}\n")
        task_file.write(f"\t\t✅ Completed Tasks:\t\t{completed_tasks}\n")
        task_file.write(f"\t\t❌ Uncompleted Tasks:\t\t{uncompleted_tasks}\n")
        task_file.write(f"\t\t❌ Overdue Tasks:\t\t{overdue_tasks}\n")
        task_file.write(f"\t\t❌ Incomplete Percentage:\t{incomplete_percentage:.2f}%\n")
        task_file.write(f"\t\t❌ Overdue Percentage:\t\t{overdue_percentage:.2f}%\n")
        task_file.write(f"\t{borderXL}\n")

def display_statistics(curr_user, admin_user):
    while True:
        if curr_user == admin_user:
            # Check if the reports exist, if not generate them
            if not os.path.exists('user_overview.txt') or not os.path.exists('task_overview.txt'):
                print(f"\t{borderXL}")
                print("\n\t\t⭕️ There is no statistics to display.")
                print(f"\t\t  Please go to 'gr' to create new report.\n")
                print(f"\t{borderXL}")
                break

            # Display the contents of user_overview.txt
            with open('user_overview.txt', 'r') as user_file:
                print(user_file.read())

            # Display the contents of task_overview.txt
            with open('task_overview.txt', 'r') as task_file:
                print(task_file.read())
            break