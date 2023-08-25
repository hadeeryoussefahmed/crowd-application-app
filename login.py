import json
import re

def validate_password():
    password = input("Enter your password : ")
    con_password = input("Enter your Confirm password : ")

    if (len(password) > 6 and len(password) < 20 and password == con_password):
        print("pass is valid")
        return password
    else:
        print("pass is not Valid ") 

def  validate_email():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = input("What is your EMAIL ? ")
    while True:
        if re.fullmatch(regex, email):
            return email
        else:
            email = input("Invalid EMAIL, What is your EMAIL ? ")

def userLogin():
    try:
        # Specify the file path
        file_path_users_data = "users_data.txt"

        # Read data row by row and search for a record by key
        def search_record_by_key(search_key, search_value):
            with open(file_path_users_data, 'r') as json_file:
                for line in json_file:
                    data = json.loads(line)  # Load each line as a JSON dictionary
                    if search_key in data and data[search_key] == search_value:
                        return data
            return None  # Return None if not found
        
        user_email = validate_email()
        user_password = validate_password()

        # search
        key_to_search = "email"
        value_to_search = user_email
        found_record = search_record_by_key(key_to_search, value_to_search)

        if found_record:
            if found_record["password"]== user_password:
                print("Success login welcome " + found_record["first_name"])
                return found_record
        else:
            print("Error logging in")

    except Exception as e:
        print(f"Failed to Open the file its not exist. {e}")