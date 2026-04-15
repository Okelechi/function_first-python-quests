#!/usr/bin/python3

# Ask the user for their score
score = int(input("Enter your score (0-100): "))

# Check the score and assign a grade
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Needs Improvement")


