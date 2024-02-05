#===Importing necessary libraries===
import os
from datetime import datetime, date

# Defining constant variables
DATETIME_FORMAT = "%Y-%m-%d"
# Horizontal lines will be used for better visual separation
borderXS = "-" * 40
border = "-" * 60
borderXL = "-" * 68


# ===This function is responsible for registering a new user===
def reg_user(username_password):
    # Start an infinite loop to repeatedly prompt the user for a new username
    while True:
        print(f"\t{borderXL}")
        new_username = input("\t\t🟡 New Username: ")
    
        # Check if the username already exists
        if new_username in username_password:
            print(f"\t{borderXL}")
            print("\t❌ Username already exists. Please choose a different username.")
            print("\t   Or enter 'e' to return to the Main Menu")
        elif new_username == 'e':
            # If the user enters 'e', return from the function (exit the registration process)
            return  # Return to the Main Menu without making any changes
        else:
            # If the username is unique and 'e' is not entered, break out of the loop
            break

    # Prompt the user to enter a new password and confirm it
    new_password = input("\t\t🟡 New Password: ")
    confirm_password = input("\t\t🟡 Confirm Password: ")

    # Check if the entered password and confirmation match
    # If passwords matched, display a success message
    if new_password == confirm_password:
        print(f"\t{borderXL}")
        print("\n\t\t✅ New user added successfully!")
        print(f"\t{borderXL}")
        # Add the new user to the 'user' dictionary
        username_password[new_username] = new_password

        # Write all user data to the file
        with open("user.txt", "a") as out_file:
            out_file.write(f"\n{new_username};{new_password}")
    else:
        # If passwords do not match, display an error message
        print("\n\t\t❌ Password confirmation failed. User not added.")

# ===This function is responsible for adding a new task===
def add_task(username_password, task_list):
        # Ask the user for the name of the person assigned to the task        
        print(f"\t{borderXL}")
        task_username = input("\t\t🟡 Name of person assigned to task: ")

        # Check if the assigned username exists 
        if task_username not in username_password.keys():
            print(f"\t{borderXL}")
            print("\t\t❌ User does not exist. Please enter a valid username")
            # If not, call add_task to allow the user to re-enter the assigned username
            return add_task(username_password, task_list)

        # Ask the user for the title of the task    
        print(f"\t{borderXL}")
        task_title = input("\t\t🟡 Title of Task: ")

        # Ask the user for the description of the task
        print(f"\t{borderXL}")
        task_description = input("\t\t🟡 Description of Task: ")

        # Infinite loop to prompt the user to enter correct date format
        # Prompt the user for the due date
        while True:
            try:
                print(f"\t{borderXL}")
                task_due_date = input("\t\t🟡 Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_FORMAT)
                break
            # Error handling message
            except ValueError:
                print(f"\t{borderXL}")
                print("\n\t❌ Invalid datetime format. Please use the format specified\n")
        
        # Then get the current date.
        curr_date = date.today()
        # Create a new task dictionary with the provided information
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }
        # Append the new task to the task list
        task_list.append(new_task)

        # Write the updated task list to the "tasks.txt" file
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

        # Display success message 
        print(f"\t{borderXL}")
        print("\t\t✅ Task successfully added.")
        print(f"\t{borderXL}")

# ===This function is responsible for viewing all tasks===
def view_all(task_list):
        # Since the code already creates tasks.txt file at the beginning,
        # Error handling in case of tasks.txt is empty 
        if os.path.getsize("tasks.txt") == 0:
                print(f"\t{borderXL}")
                print("\t⭕️ There are no tasks to display")
                print(f"\t{borderXL}")
        else:
            # Iterate through each task in the task_list
            for t in task_list:
                # Create a user-friendly representation of the task information
                disp_str = f"📍Task: \t{t['title']}\n"
                disp_str += f"\t\tAssigned to: \t{t['username']}\n"
                disp_str += f"\t\tDate Assigned: \t{t['assigned_date'].strftime(DATETIME_FORMAT)}\n"
                disp_str += f"\t\tDue Date: \t{t['due_date'].strftime(DATETIME_FORMAT)}\n"
                disp_str += f"\t\tDescription: \n\t\t{t['description']}\n"
                # Display the status based on completion
                # For more coherent look I've chosen to use 'Completed'/'Pending' instead of 'Yes'/'No'
                disp_str += f"\t\tStatus: \t{'✅ Completed' if t['completed'] else '❗️ Pending'}\n"
                print(f"\t{borderXL}")
                # Print the formatted task information
                print(f"\t\t{disp_str}")

# ===This function is responsible for displaying users' tasks only===
def display_tasks(user_tasks):
    # Iterate through each task in the user_tasks list
    for i, t in enumerate(user_tasks, start=1):
        # Create a user-friendly representation of the task information
        disp_str = f"\t{borderXL}\n"
        disp_str += f"📍TASK {i}:\n" # Task number placed on the side for easy read
        disp_str += f"\t\tTitle: \t\t {t['title']}\n"
        disp_str += f"\t\tAssigned to: \t {t['username']}\n"
        disp_str += f"\t\tDate Assigned: \t {t['assigned_date'].strftime(DATETIME_FORMAT)}\n"
        disp_str += f"\t\tDue Date: \t {t['due_date'].strftime(DATETIME_FORMAT)}\n"
        disp_str += f"\t\tDescription: \t {t['description']}\n"

        # Determine the completion status and include in the string
        completion_status = "✅ Completed" if t['completed'] else "❗️ Pending"  # Updated this line
        disp_str += f"\n\t\tStatus: \t {completion_status}\n"
        disp_str += f"\t{borderXL}\n"

        # Print the formatted task information
        print(disp_str)

# ===This function is responsible for displaying tasks, 
# and allow various operations on them===
def view_mine(task_list, curr_user, logged_in):
    user_tasks = [t for t in task_list if t['username'] == curr_user]

    # Check if the user has any tasks
    if not user_tasks:
                print(f"\t{borderXL}")
                print("\t❌ There are no tasks assigned to you")
                print(f"\t{borderXL}")
    else:
        # Initialize selected_task outside the loop
        selected_task = None  
        while True:
            # Use display function inside the loop. 
            # (This is because after editing and deleting 
            # tasks the user need to be able to see tasks again.)
            display_tasks(user_tasks) 
             
            # Prompt user to select the task from the list or -1 to exit
            if logged_in and curr_user:
                print(f"\t{borderXL}")
                print("\n\t🔰 Enter the number of the task to select")
                selected_task_number = input("\t   or enter -1 to return to the Main Menu: ")
                print(f"\n\t{borderXL}")
                try:
                    selected_task_number = int(selected_task_number)
                    # If user entered - 1, exit to Main Menu
                    if selected_task_number == -1:
                        return
                    
                    # Check if the selected task number is valid
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

                        # Handle operations related to the selected task
                        # Task View Menu created for easy representation
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
                            # Perform operations based on user input
                            if operation == 'c':
                                selected_task['completed'] = True
                                # Function to save tasks
                                save_tasks_to_file(task_list)  
                                print(f"\t{borderXL}")
                                print("\n\t\t✅ Task marked as 'Completed'.\n")
                                print(f"\t{borderXL}")
                                break
                            # If the task is not 'Completed', the user can edit the task
                            elif operation == 'e' and not selected_task.get('completed', False):
                                # Function to update tasks
                                update_task(selected_task, task_list)
                            elif operation == 'e' and selected_task.get('completed', True):
                                print(f"\t{borderXL}")
                                print("\n\t❌ You cannot edit tasks that has been marked as 'Completed'\n")
                                print(f"\t{borderXL}")
                            elif operation == 'd':
                                # Function to delete tasks
                                delete_task(task_list, selected_task)
                                print(f"\t{borderXL}")
                                print("\n\t\t\t❌ This task DELETED\n")
                                # Message to user to refresh the page to see updated tasks
                                print("\n\t🟢 Your task list will refresh when you return to the Main Menu\n")
                                print(f"\t{borderXL}")
                                break
                            # User can go back and select another task by entering 's'
                            elif operation == 's':
                                break
                            # Return to the Main Menu
                            elif operation =='b':
                                return
                            # In all other case display error message to user
                            else:
                                print(f"\t{borderXL}")
                                print("\n\t\t❌ Sorry but this option does not exist.")
                                print("\n\t\t\tPlease enter correct option\n")
                                print(f"\t{borderXL}")
                    # Message to user if task number does not exist        
                    else:
                        print("\n\t\t❌ Sorry but this task does not exist.")
                        print("\n\t\t❌ Please enter a correct task number.")
                        print(f"\n\t{borderXL}")
                        # After printing the message, continue to the next iteration
                        
                # ValueError message in case letters were entered instead of digits  
                except ValueError:
                    print("\n\t\t❌ Sorry, but you need to enter a valid number only.\n")
                    print(f"\t{borderXL}")

# ===This function is responsible for saving tasks after performing changes===
def save_tasks_to_file(tasks):
    # Open the tasks.txt file in write mode
    with open("tasks.txt", "w") as task_file:
        # New str variable as an empty list to store task information
        task_list_to_write = []
        for t in tasks:
            # Convert task attributes to a new string
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_FORMAT),
                t['assigned_date'].strftime(DATETIME_FORMAT),
                # Convert Boolean to "Yes" or "No" in a tasks.txt
                # Note: It will be displayed as 'Pending/Completed' in 'ds'
                "Yes" if t['completed'] else "No"                                     
            ]
            # Join both string together
            task_list_to_write.append(";".join(str_attrs))
        # Write the formatted task information to the tasks.txt file
        task_file.write("\n".join(task_list_to_write))

# ===This function is responsible for editing tasks===
def update_task(selected_task, task_list):
    try:
        print(f"\t{borderXL}")
        # Prompt the user to enter a new title for the task
        new_title = input(f"\t\t🟡 Enter a new title for the task: ")
        # Update the task title
        selected_task['title'] = new_title

        # Ask the user if they want to update the due date
        print(f"\t{borderXL}")
        update_due_date = input("\t\t🟡 Do you want to update the due date? (y/n): ").lower()
        
        # If the user entered 'y' - enter a loop to handle date input
        if update_due_date == 'y':
            while True:
                print(f"\t{borderXL}")
                new_due_date_str = input("\t\t🟡 Enter a new Due Date (YYYY-MM-DD): ")
                
                # Convert the input string to a datetime object with the specified format
                try:
                    new_due_date = datetime.strptime(new_due_date_str, DATETIME_FORMAT)
                    # Update the task due date as before
                    selected_task['due_date'] = new_due_date
                    # Exit the loop if the date is entered correctly
                    break
                    
                # Repeat the loop if the date is entered incorrectly
                except ValueError:
                    print(f"\t{borderXL}")
                    print("\n\t\t❌ Date format not recognised. Please enter correct Due Date.\n")
                    
        # Exit the loop if the user chooses not to update the date
        elif update_due_date == 'n':
            pass  # Exit the loop if the user chooses not to update the date

        # Handle the case where the user enters an invalid response
        else:
            print(f"\t{borderXL}")
            print("\n\t\t❌ Invalid input. Please enter 'y' or 'n'.\n")
            return update_task(selected_task, task_list)

        # Prompt the user to update the completion status of the task
        print(f"\t{borderXL}")
        mark_completed = input("\t\t🟡 Mark the task as completed? (y/n): ").lower()
        # Update status
        selected_task['completed'] = mark_completed == 'y' or mark_completed == 'yes'

        # Save the updated task_list to the file
        save_tasks_to_file(task_list)

        # Display a success message to the user
        print(f"\t{borderXL}\n")
        print("\n\t\t✅ Your task updated successfully.\n")

    # Error handling where user enters anything other than numbers
    except ValueError:
        print(f"\t{borderXL}")
        print("\n\t\t❌ Invalid input. Please enter numerical value only.\n")

# ===This function is responsible for deleting tasks===
def delete_task(task_list, selected_task):
    # Remove the selected task from the task_list
    task_list.remove(selected_task)
    # Write the updated task_list to the tasks.txt
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []

        # Convert each task in the task_list
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
        # Write each task to a new line in the file
        task_file.write("\n".join(task_list_to_write))
    
# ===This function generates reports based on the tasks.txt and users.txt information===
def generate_reports(task_list, username_password):
    # Get unique usernames from tasks
    unique_usernames = set(task['username'] for task in task_list)

    # Calculate various task-related statistics as below
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task.get('completed', False))
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in task_list if not task.get('completed', False) and task['due_date'] < datetime.now())

    # Calculate task completion percentages
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    overdue_percentage = (overdue_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    
    # Write to user_overview.txt in a user-friendly manner
    with open('user_overview.txt', 'w') as user_file:
        user_file.write(f"\t{borderXL}\n")
        user_file.write(f"\t\t\t📉 User Overview 📉 \n\n")
        total_users = len(username_password)
        user_file.write(f"\t\t📙 Total Users:\t\t{total_users} Users\n") 
        user_file.write(f"\t\t📗 Tasks per User:\n\n")
        for username in unique_usernames:
            tasks_count = len([task for task in task_list if task['username'] == username])
            user_file.write(f"\t\t\t🎎 {username}:\t{tasks_count} tasks\n\n")

    # Write to task_overview.txt in a user-friendly manner
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

# ===This function is responsible for displaying statistics===
def display_statistics(curr_user, admin_user):
    # Check if the current user is an admin
    if curr_user == admin_user:
        # Generate reports if the files do not exist
        if not os.path.exists('user_overview.txt') or not os.path.exists('task_overview.txt'):
            generate_reports(admin_user, curr_user)
            
        # Display the contents of user_overview.txt
        with open('user_overview.txt', 'r') as user_file:
            print(user_file.read())

        # Display the contents of task_overview.txt
        with open('task_overview.txt', 'r') as task_file:
            print(task_file.read())
