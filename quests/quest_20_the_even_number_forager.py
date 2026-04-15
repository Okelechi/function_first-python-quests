# quest_20.py
# Using the modulo operator (%) inside a loop to filter numbers
for num in range(1, 21):
    if num % 2 == 0: # If remainder is 0 when divided by 2, it is even
        print(f"{num} is even.")