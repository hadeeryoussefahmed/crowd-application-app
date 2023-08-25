import re
import json
from prettytable import PrettyTable

# Define function for creating a project
def validate_title():
    while True:
        print(" Enter your title: ")
        title = input()
        if not (title.isspace()) or (title.isalpha()):
           print("valid title")
           return title
        else:
            print("invalid title")   

def validate_details():
    while True:
        print(" Enter your details: ")
        details = input()
        if not (details.isspace()) or (details.isalpha()):
           print("valid details")
           return details
        else:
            print("invalid details")   

def validate_total_target():
    while True:
        print(" Enter your total_target: ")
        total_target = input()
        if not (total_target.isspace()) or (total_target.isalpha()):
           print("valid total_target")
           return total_target
        else:
            print("invalid total_target")   

def  validate_start_date():
    regex = r"\d{4}-\d{2}-\d{2}"
    start_date = input("What is your start_date")
    while True:
        if re.fullmatch(regex, start_date):
            return start_date
        else:
            start_date = input("Invalid start_date, What is your start_date ? ")

def  validate_end_date():
    regex = r"\d{4}-\d{2}-\d{2}"
    end_date = input("What is your end_date")
    while True:
        if re.fullmatch(regex, end_date):
            return end_date
        else:
            end_date = input("Invalid end_date, What is your end_date ? ")

file_path_projects_data = "projects_data.txt"
#
#
def create_project(email,name):
    try:
        title = validate_title()
        details = validate_details()
        total_target = validate_total_target()
        start_date = validate_start_date()
        end_date = validate_end_date()

        #create dictionary
        new_projects_data = {
            "email": email,
            "name": name,
            "title": title,
            "details": details,
            "total_target": total_target,
            "start_date": start_date,
            "end_date": end_date
        }

        # Open the file in write mode and save the dictionary as JSON
        with open(file_path_projects_data, 'a') as json_file:
            json.dump(new_projects_data, json_file)
            json_file.write('\n')

        print(f"\n=== Registered successfully ===\n")

    except Exception as e:
        print(f"\n=== Registered Failed {e}  ===\n")

# Define function for viewing a project
def view_project(file_path_projects_data):
    # Read the file line by line and parse each line as JSON
        data = []
        with open(file_path_projects_data, 'r') as file:
            for line in file:
                try:
                    dictionary = json.loads(line.strip())
                    data.append(dictionary)
                except json.JSONDecodeError:
                    print(f"Error parsing line: {line}")

        # Create a PrettyTable
        table = PrettyTable()
        columns = ["name", "title", "details", "total_target", "start_date", "end_date"]
        if data:
            if columns:
                # Filter columns based on the specified list
                valid_columns = [col for col in columns if col in data[0]]
                if valid_columns:
                    # Add table headers
                    table.field_names = valid_columns
                    # Add rows to the table
                    for dictionary in data:
                        table.add_row([dictionary[col] for col in valid_columns])

                    # Print the table
                    print(table)
                else:
                    print("No valid columns specified.")
            else:
                # Add table headers
                table.field_names = data[0].keys()
                # Add rows to the table
                for dictionary in data:
                    table.add_row(dictionary.values())

                # Print the table
                print(table)
        else:
            print("No data found in the file.")
            
# Define function for viewing a project
def  search_dates(file_path_projects_data,value):
    with open(file_path_projects_data, "r") as json_file:
        for line in json_file:
            data = json.loads(line)
            if data.get("start_date") == value:
                print(data)

def delete_project(title, email,file_path_projects_data ):
    lines_to_keep = []
    with open(file_path_projects_data, 'r') as file:
        for line in file:
            entry = json.loads(line) 
            if entry.get("title") != title or entry.get("email") != email:
                lines_to_keep.append(line)
    
    with open(file_path_projects_data, 'w') as file:
        file.writelines(lines_to_keep)

def edit_project(filename, key, value_to_edit, new_value):
    updated_data = []

    with open(filename, 'r') as file:
        for line in file:
            entry = json.loads(line)
            if key in entry and entry[key] == value_to_edit:
                entry[key] = new_value
            updated_data.append(entry)

    with open(filename, 'w') as file:
        for entry in updated_data:
            json.dump(entry, file)
            file.write('\n')
        



