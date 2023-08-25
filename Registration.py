import re
import json

def validate_first_Name():
    while True:
        print(" Enter your First Name: ")
        first_Name = input()
        if not (first_Name.isspace()) or (first_Name.isalpha()):
           print("valid name")
           return first_Name
           
        else:
            print("invalid name")   

def validate_last_Name():
    while True:
        print(" Enter your last Name: ")
        last_Name = input()
        if not (last_Name.isspace()) or (last_Name.isalpha()):
           print("valid name")
           return last_Name
           
        else:
            print("invalid name")

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
    email = input("What is your Email ")
    while True:
        if re.fullmatch(regex, email):
            return email
        else:
            email = input("Invalid Email, What is your Email ? ")

def  validate_phone():
    regex = r'01[0-9]{9}$'  
    phone = input("What is your phone? ")
    while True:
        if re.fullmatch(regex, phone):
            return phone
        else:
            phone = input("Invalid phone, What is your phone ? ")

file_path_users_data = "users_data.txt"
def registration():
    print("\n============== Register Form ===============\n")
    try:
        first_name = validate_first_Name()
        last_name = validate_last_Name()
        password = validate_password()
        email = validate_email()
        phone = validate_phone()

        #create dictionary
        new_user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "password": password,
            "email": email,
            "phone": phone
        }
        # Open the file in write mode and save the dictionary as JSON
        with open(file_path_users_data, 'a') as json_file:
            json.dump(new_user_data, json_file)
            json_file.write('\n')

        print(f"\n=== Registered successfully ===\n")

    except Exception as e:
        print(f"\n=== Registered Failed {e}  ===\n")





