# Define the correct password
correct_password = "dragon123"

# Ask the user to enter the password
user_password = input("Enter the password: ")

# Check if the password is correct
if user_password == correct_password:
    print("Access Granted!")
else:
    print("Access Denied!")