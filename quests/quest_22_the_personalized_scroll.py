#!/usr/bin/python3
# This quest is about creating a personalized greeting function that takes a user's name and their quest as input and prints a customized message.
def personalized_greeting(name , quest):

  print(f"Hello, {name}! Your quest is to {quest}.")

user_name = input("Enter your name: ")
user_quest = input("Enter your quest: ")

personalized_greeting(user_name , user_quest)

