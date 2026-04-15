def forest():
    print("You are in a dark forest. You survived!")

    def cave():
        print("You entered a cave, and fell. Game Over!")

        Choice = input("Forest or cave?").lower()
        if Choice == "forest":
            forest()
        else:
            cave()

            