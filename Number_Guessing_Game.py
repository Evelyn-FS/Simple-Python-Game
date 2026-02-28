import random

# Home page and instructions
print("\n===================================")
print("Welcome to the Number Guessing Game")
print("===================================\n")

while True:
    print("==================")
    print("1. Start The Game")
    print("2. Difficulty")
    print("3. Scoreboard")
    print("4. Exit The Game")
    print("==================")

    command = input("> Your choice: ")

    for x in ["1", "2", "3", "4"]:
        if command == "1":
            print("Game starting...")

            # Game logic goes here
            
            number = random.randint(1, 100) # Generating a random number

            clue_number = [20, 15, 10, 5] # Defining clue ranges

            attempts = 0 # Initial attempts

            # Function to mask the last digit
            def masked_last_digit(number):
                if number >= 10 and number <= 100 and number % 10 != 0:
                    return (number // 10) * 10
                return number

            # Masked last digit of the number
            masked_number = masked_last_digit(number)

            # Calculating ranges for clues
            for i in range(len(clue_number)):
                less = masked_number - clue_number[i]
                more = masked_number + clue_number[i]
                if less < 1:
                    less = 1
                if more > 100:
                    more = 100
                if i == 0:
                    free_clue = f"{less} and {more}"
                elif i == 1:
                    clue1 = f"{less} and {more}"
                elif i == 2:
                    clue2 = f"{less} and {more}"
                elif i == 3:
                    clue3 = f"{less} and {more}"

            # Asking the user to give an input
            first_guess = int(input("\nPlease select a number from 1-100: "))
            if first_guess == number:
                print("Congrats your guess is correct")
            elif first_guess != number:
                attempts += 3
                print(f"\n=> Your first guess is incorrect\n=> You have received {attempts} attempts")
                print(f"=> The number is between {free_clue}")
                number_guessed = int(input("\nPlease enter your next guess: "))

            # Function to provide clues based on attempts
            def clue_output(attempts):
                if attempts == 3:
                    return f"=> The number is between {clue1}"
                elif attempts == 2:
                    return f"=> The number is between {clue2}"
                elif attempts == 1:
                    return f"=> The number is between {clue3}"
                return f"NICE TRY! The correct number was {number}\n"
                    
            # Checking the user's input
            while number_guessed != number and attempts > 0:
                print(f"\n=> Attempts left: {attempts}")
                print(f"{clue_output(attempts)}")
                number_guessed = int(input("\nYour guess is incorrect, try again: "))
                attempts -= 1
                if attempts == 0:
                    print(clue_output(attempts))
                    break
                elif number_guessed == number:
                    print("Congrats your guess is correct.")
                    break
                else:
                    while number_guessed is str() or number_guessed < 1 or number_guessed > 100:
                        number_guessed = int(input("Your guess is invalid, please try again: "))
                    continue  # Restart the guessing loop with the valid guess
            
            if number_guessed == number:
                print("\nSetting back to main menu...\n")
                continue  # Restart the main loop after a correct guess

        elif command == "2":
            print("Difficulty settings...")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            difficulty = input("> Type '0' to back to main menu: ")

            # Difficulty settings logic goes here

        elif command == "3":
            print("Scoreboard...")
            print("1. All score")
            print("2. Best score")
            print("3. Total game played")
            scoreboard = input("> Type '0' to back to main menu: ")

            # Scoreboard logic goes here

        elif command == "4":
            print("Exiting the game...")
            break
        else:
            while command not in ["1", "2", "3", "4"]:
                command = input("Your choice is invalid, please try again: ")
            continue  # Restart the main loop

    if command == "4":
        break  # Exit the main loop
                