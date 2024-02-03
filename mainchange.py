# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import source

borderXS = "-" * 40
border = "-" * 60
borderXL = "-" * 68


# Create tasks.txt if it doesn't exist
if not source.os.path.exists("tasks.txt"):
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
    curr_t['due_date'] = source.datetime.strptime(task_components[3], source.DATETIME_FORMAT)
    curr_t['assigned_date'] = source.datetime.strptime(task_components[4], source.DATETIME_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

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

while True:   
    if logged_in:
        if curr_user == admin_user:
            
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

        elif menu == 'ds' and curr_user == admin_user:
            source.display_statistics(curr_user, admin_user)
                    
        elif menu == 'ds' and curr_user: 
            print(f"\t{borderXL}")
            print(f"\t\t❌ Sorry. But this option is for the admin access only.")
            print(f"\t{borderXL}")

        elif menu == 'e':
            print('\n\t\t\t\t👋 Goodbye!!!👋\n\n\n ')
            exit()

        else:
            print(f"\t{borderXL}")
            print("\t\t❌ This menu option is not recognised. Please Try again")
            print(f"\t{borderXL}")