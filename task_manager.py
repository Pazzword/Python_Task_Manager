# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.


#=====importing libraries===========
import source

#   Constants for horizontal line separators
# As the code contains extensive use of horizontal lines, 
#        they are define in both py files
borderXS = "-" * 40
border = "-" * 60
borderXL = "-" * 68


# Create tasks.txt if it doesn't exist
if not source.os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass
# Read task data from tasks.txt
with open("tasks.txt", 'r') as task_file:
    # Split the file content into lines and filter out empty lines
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# New list to store task dictionaries
task_list = []

# Loop through each task string and convert it into a dictionary
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = source.datetime.strptime(task_components[3], source.DATETIME_FORMAT)
    curr_t['assigned_date'] = source.datetime.strptime(task_components[4], source.DATETIME_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    # Now 'append' the current task dictionary to the task_list
    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not source.os.path.exists("user.txt"):
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

# This is the variable to track the login status
logged_in = False

# Continue the login process until a user successfully logs in
while not logged_in:
    # Define admin credentials
    admin_user = "admin"
    admin_password = "password"

    # Ask user to enter username and password
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")

    # Check if the entered credentials match the admin credentials
    if curr_user == admin_user and curr_pass == admin_password:
        print("✅ Admin Login Successful!")
        logged_in = True

    # Check if the entered username exists in the username_password dictionary
    if curr_user not in username_password.keys():
        # Message to the user that the user does not exist
        print("❌ User does not exist")
        # If user doesn't exist, prompt for credentials again
        continue

    # Check if the entered password matches the stored password
    elif username_password[curr_user] != curr_pass:
        print("❌ Wrong password")
        # If password is incorrect, ask for password again
        continue
     # If both credential matched display success message
    else:
        print("✅ Login Successful!")
        logged_in = True

# ===Main Menu Section===
while logged_in:
        # Check if the current user is the admin to provide additional options
        if curr_user == admin_user:
            # Display the main menu options for the admin
            menu = input(f'''
                         MAIN MENU
            Select one of the following Options below:
            {borderXS}
            🔐 r  -  Registering a user
            📥 a  -  Adding a task
            🔎 va -  View all tasks
            🗓  vm -  View my task
            📈 gr -  Generate reports
            📊 ds -  Display statistics
            ❌ e  -  Exit
            {borderXS}
            : ''').lower()
        else:
            # Display the main menu options for regular users
            menu = input(f'''
                        MAIN MENU
            Select one of the following Options below:
            {borderXS}            
            🔐 r  -  Registering a user
            📥 a  -  Adding a task
            🔎 va -  View all tasks
            🗓  vm -  View my task
            📊 ds -  Display statistics
            ❌ e  -  Exit
            {borderXS}
            : ''').lower()

        # Check the user's menu choice and perform corresponding actions
        # Call functions from the 'source' module to handle user's choice             
        if menu == 'r':
            source.reg_user(username_password)
        
        elif menu == 'a':
            source.add_task(username_password, task_list)
      
        elif menu == 'va':
            source.view_all(task_list)

        
        elif menu == 'vm':
            source.view_mine(task_list, curr_user, logged_in)

        elif menu == 'gr' and curr_user == admin_user:
            source.generate_reports(task_list, username_password)
            print(f"\t{borderXL}")
            print("\n\t\t✅ Report generated Successfully!")
            print("\t  This report is now available under Display Statistics - 'ds'\n")
            print(f"\t{borderXL}")

        elif menu == 'ds' and curr_user == admin_user:
            source.generate_reports(task_list, username_password)
            source.display_statistics(curr_user, admin_user)
            print("\t✅ These reports are available on your local computer\n")
            print(f"\t{borderXL}")
                    
        elif menu == 'ds' and curr_user: 
            print(f"\t{borderXL}")
            print(f"\t\t❌ Sorry. But this option is for the admin access only.")
            print(f"\t{borderXL}")

        # Exit the program if the user chooses to exit
        elif menu == 'e':
            print('\n\t\t\t\t👋 Goodbye!!!👋\n\n\n ')
            exit()

        # Display an error message for unrecognized menu options
        else:
            print(f"\t{borderXL}")
            print("\t\t❌ This menu option is not recognised. Please Try again")
            print(f"\t{borderXL}")
