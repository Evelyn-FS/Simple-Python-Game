print("\n===================================")
print("Welcome to the Number Guessing Game!")
print("===================================\n")


while True:
    print("1. Start The Game")
    print("2. Difficulty")
    print("3. Scoreboard")
    print("4. Exit The Game")

    command = input("> Your choice: ")

    for x in ["1", "2", "3", "4"]:
        if command == "1":
            print("Game starting...")
            # Game logic goes here
        elif command == "2":
            print("Difficulty settings...")
            print("1. ")
            print("2. ")
            print("3. ")
            difficulty = input("> Your choice: ")
            # Difficulty settings logic goes here
        elif command == "3":
            print("Scoreboard...")
            # Scoreboard logic goes here
        elif command == "4":
            print("Exiting the game...")
            break
        else:
            while command not in ["1", "2", "3", "4"]:
                command = input("Your choice is invalid, please try again: ")
            continue  # Restart the main loop with the valid command

    if command == "4":
        break  # Exit the main loop if the user chooses to exit