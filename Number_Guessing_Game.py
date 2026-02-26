import random

# Home page and instructions
print("\n===================================")
print("Welcome to the Number Guessing Game")
print("===================================\n")

while True:
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")

    command = input("> Your choice: ")

    while command == "1":
        
            # Generating a random number
            number = random.randint(1, 100)

            # Defining clue ranges
            clue_number = [20, 15, 10, 5]

            # Initial attempts
            attempts = 0

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

            if number_guessed == number:
                print("Congrats your guess is correct")
            else:
                print(clue_output(attempts))
                