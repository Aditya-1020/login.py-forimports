import csv
import getpass

def login_prompt():
    print("Pick an option")
    print("[A] - LOGIN")
    print("[B] - NEW USER")
    
    choice = input("Enter your choice (A/B): ").strip().upper()
    
    if choice == 'A':
        # Call the login function
        login()
    elif choice == 'B':
        # Call the new user registration function
        create_new_user()
    else:
        print("Invalid choice. Please select either 'A' or 'B'.")

def login():
    print("Welcome back!!")
    user_name = input("Enter your username: ").strip()
    input_password = getpass.getpass("Enter your password: ").strip()

    csv_file = "login_data.csv"
    fieldnames = ["Username", "Password"]

    # Add your login logic here
    # Check if the username and input_password combination is correct
    if is_username_valid(csv_file, user_name, input_password):
        print("Login successful!")
    else:
        print("Login failed. Invalid username or password.")

def create_new_user():
    print("Welcome! Let's create your account")
    user_name = input("Enter username: ")
    password = getpass.getpass("Enter a new password: ")

    csv_file = "login_data.csv"
    fieldnames = ["Username", "Password"]

    if not is_username_duplicate(csv_file, user_name):
        with open(csv_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Use a single dictionary to store both username and password
            writer.writerow({"Username": user_name, "Password": password})

        print(f"User '{user_name}' and the password have been added to the CSV file.")
    else:
        print(f"Username '{user_name}' already exists. Please choose a different username.")

def is_username_duplicate(csv_file, username):
    try:
        with open(csv_file, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["Username"] == username:
                    return True
    except FileNotFoundError:
        return False

def is_username_valid(csv_file, username, input_password):
    try:
        with open(csv_file, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["Username"] == username and row["Password"] == input_password:
                    return True
    except FileNotFoundError:
        return False

# Call the login_prompt() function to initiate the login prompt
login_prompt()
