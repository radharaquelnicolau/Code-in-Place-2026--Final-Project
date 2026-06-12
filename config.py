user_xp = 0
user_lives = 5

def enter_to_continue():
    while True:
        user_input = input("Press [ENTER] to continue")
        if user_input == "":
            break
        print("Please press [ENTER] to continue.")
    #while loop serves as a way to make sure that only when the user presses enter will the program continue