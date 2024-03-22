# Task Manager Application

## Overview

This Task Manager application allows users to register, log in, add tasks, view tasks, and perform various administrative functions. The application is designed with a command-line interface and utilizes a file-based system for storing user data and task information.

## Usage Instructions

1. Ensure that you open both 'python' files in the same folder in VS Code.

2. To access admin rights, use the following credentials:
   - Username: admin
   - Password: password

3. Text files will be automatically created when the user runs the code.

## File Structure

- **`task_manager.py`**: The main file containing the application code.
- **`source.py`**: A module containing functions for user registration, task management, and report generation.

## Automatically created files

- **`tasks.txt`**: Text file storing task data.
- **`user.txt`**: Text file storing user credentials.

## Constants

- **`borderXS`**: Small horizontal line separator of 40 characters.
- **`border`**: Medium horizontal line separator of 60 characters.
- **`borderXL`**: Large horizontal line separator of 68 characters.

## Task Data Initialization

1. If `tasks.txt` does not exist, it is created with a default structure.
2. Task data is read from `tasks.txt`, and a list of task dictionaries (`task_list`) is created.

## User Data Initialization

1. If `user.txt` does not exist, it is created with a default admin account.
2. User data is read from `user.txt`, and a dictionary (`username_password`) is created to store user credentials.

## Login Section

- Users are prompted to enter their username and password.
- Admin credentials are predefined (admin:password).
- The login process continues until successful authentication.

## Main Menu Section

- The main menu is displayed based on user roles (admin or regular user).
- Users can choose from various options, each corresponding to specific actions in the application.

## Menu Options

1. **Register User (`r`)**: Allows user registration. Admin-only option.

2. **Add Task (`a`)**: Allows users to add tasks.

3. **View All Tasks (`va`)**: Displays all tasks.

4. **View My Tasks (`vm`)**: Displays tasks assigned to the logged-in user.

5. **Generate Reports (`gr`)**: Admin-only option to generate reports.

6. **Display Statistics (`ds`)**: Admin-only option to display statistics.

7. **Exit (`e`)**: Exits the application.

## Important Notes

- Admin credentials: admin:password
- Open the entire folder in VS Code for correct file access.
