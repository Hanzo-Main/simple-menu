# Course: CS 30
# Period: 1
# Date created: 21/02/04
# Date last modified: 21/02/04
# Name: Kira Gray
# Description: simple menu for RPG, accepts, confirms valid/invalid imputs.
# only accepts all lower case or all capital words

ans = True
# while loop that has if-elif-else statements inside for each option
while ans:
    print("""
      Go in one of the following directions:
      -> Left
      -> Right
      Do one of the following actions:
      -> Explore
      -> Attack
      -> Heal
      """)
    ans = input("What would you like to do? ")
    if ans == "Left".lower() or ans == "left".upper():
        print("You go left.")
    elif ans == "right".lower() or ans == "right".upper():
        print("You go right.")
    elif ans == "Explore".lower() or ans == "Explore".upper():
        print("You look around.")
    elif ans == "attack".lower() or ans == "attack".upper():
        print("You attack.")
    elif ans == "heal".lower() or ans == "heal".upper():
        print("You heal 20 points.")
    else:
        print("Invalid imput!")
