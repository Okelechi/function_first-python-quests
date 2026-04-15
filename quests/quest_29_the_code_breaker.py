# quest_29.py
# Using a loop with a fixed number of attempts
secret_code = "42"
attempts = 3

while attempts > 0:
    guess = input(f"Enter the code ({attempts} attempts left): ")
    if guess == secret_code:
        print("Code Broken! Access Granted.")
        break # Exits the loop early
    else:
        print("Wrong code.")
        attempts -= 1

if attempts == 0:
    print("Locked out.")

    