#!/usr/bin/python3

import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Wizard!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess it?\n")

guess = int(input("Enter your guess: "))
attempts += 1

while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try higher.\n")
    elif guess > secret_number:
        print("Too high! Try lower.\n")

    guess = int(input("Enter your guess: "))
    attempts += 1

print(f"\n CORRECT! The number was {secret_number}!")
print(f"You guessed it in {attempts} attempts!")


