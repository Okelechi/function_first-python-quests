# Define the values
total_gold = 27
friends = 4

# Calculate how many each friend gets
each_friend_gets = total_gold // friends  # Floor division = whole number

# Calculate how many the goblin keeps (remainder)
goblin_keeps = total_gold % friends

# Print the results
print("Total gold:", total_gold)
print("Number of friends:", friends)
print("Each friend gets:", each_friend_gets, "gold pieces")
print("The goblin keeps:", goblin_keeps, "gold pieces")