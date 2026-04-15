# quest_15.py
#nested if statements for multi-layered decisions

direction = input("Do you go left or right? ").lower()
if direction == "left":
 action= input("do you swim or wait? ").lower()
 if action == "swim":
     print("you found the hidden treasure!")
 else:
     print("you walked too long and a bird stole your hat")
else:
     print("you walked into a wall. ouch")
     