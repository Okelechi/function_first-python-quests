# quest_14.py
# 'and' requires both conditions to be met
age = int(input("Enter age: "))
gold = int(input("Enter gold amount: "))

if age >= 18 and gold >= 20:
    print("Welcome to the club!")
else:
    print("You do not meet the requirements to enter.")