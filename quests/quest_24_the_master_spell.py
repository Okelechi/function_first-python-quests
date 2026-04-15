#!/usr/bin/python3
# This quest is about creating a master spell that combines two functions: one to ask for the user's age and another to determine if they are old enough to vote. The master spell should call both functions in sequence.
def ask_for_age():
    age = int(input("Enter your age: "))
    return age

def can_they_vote(age):
    if age >= 18:
        print("You can vote!")
    else:
        print("You are too younf to vote!")

user_age = ask_for_age()
can_they_vote(user_age)
