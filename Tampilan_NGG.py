print("\n===================================")
print("Welcome to the Number Guessing Game!")
print("===================================\n")

print("1. ")
print("2. ")
print("3. ")
print("4. ")

command = input("> Your choice: ")

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
else:
    while command not in ["1", "2", "3", "4"]:
        print("Your input is invalid.")
        command = input("Please try again: ")
        if command in ["1", "2", "3", "4"]:
            break
