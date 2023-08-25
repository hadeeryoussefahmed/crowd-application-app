"""
main menu function
"""

import Registration
import login
from projectOperation import validate_title

from projectOperation import create_project,view_project,search_dates,delete_project,edit_project

# check our data file exist
file_path_projects_data = "projects_data.txt"
with open(file_path_projects_data, "a") as f:
    pass

# check our data file exist
file_path_users_data = "users_data.txt"
with open(file_path_users_data, "a") as f:
    pass

## it seems impossible until it's done  ##
session_user = None
# start main menu execute 
while True:
    while True:
        print("Enter Your Option Number: ")
        print("1) Login")
        print("2) Register")
        print("3) Exit")
        user_input = int(input())
        if user_input > 0 and user_input <= 3:
            break
        else:
            print("Wrong Input")
    
    if user_input == 1:
        session_user = login.userLogin()
        if session_user is not None:
            break
        else:
            print("Error NO User with this data")
            continue

    elif user_input == 2:
        Registration.registration()
    elif user_input == 3:
        print("****good bye********")
        exit()
    else:
        print("Wrong input choose from the menu options")


while True:
    while True:
        # Display the main menu and prompt the user for their choice
        print("\n------------------- Main Menu ---------------------\n")
        print("1. Create a project")
        print("2. View all projects")
        print("3. edit a project")
        print("4. delete a project")
        print("5. Search for a project by date")
        print("6. Quit")
        choice_input = int(input("Enter the number of your choice: "))
        if choice_input > 0 and choice_input <= 6:
            break
        else:
            print("Wrong input choose from the menu options")

    choice = choice_input
    if choice == 1:
        create_project(session_user["email"],session_user["first_name"])
    elif choice == 2:
        view_project(file_path_projects_data)                
    elif choice == 3:
        print("Enter which attribute you want to edit")
        key_to_edit = input()
        print("Enter your value for "+ key_to_edit)
        value_to_find = input()
        print("Enter your new value")
        new_value = input()

        edit_project(file_path_projects_data, key_to_edit, value_to_find, new_value)

    elif choice == 4:
        print("Enter Your Project Name")
        delete_project_title = validate_title()
        delete_project(delete_project_title, session_user["email"],file_path_projects_data )
    elif choice == 5:
        print("Enter Your date")
        date_input=input()
        search_dates(file_path_projects_data,date_input)
        
    elif choice == 6:
        print("...goodbye..")
        exit()
