import random

# Home page and instructions
print("\n===================================")
print("Welcome to the Number Guessing Game")
print("===================================\n")
print("How to play:")
print("1. You need to type a number between 1-100")
print("2. You will be recive 3 chance to guess the correct number after your first guess is incorrect")
print("3. Each chance (Attempts) you spend, will get you a different clue that will help you get closer to the correct number")
print("\n===GOOD LUCK!===\n")

command = input("Do you want to play the game? (Yes/No): ").strip().lower()

while command == "yes":

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
    first_guess = int(input("Please select a number from 1-100: "))
    if first_guess == number:
        print("Congrats your guess is correct")
    elif first_guess != number:
        attempts += 3
        print(f"Your first guess is incorrect\nYou have received {attempts} attempts")
        print(f"The number is between {free_clue}")
        number_guessed = int(input("Please enter your next guess: "))
    elif attempts == 0:
        print("NICE TRY! The actual number is '{number}'")

    # Function to provide clues based on attempts
    def clue_output(attempts):
        if attempts == 3:
            return f"The number is between {clue1}\nYou have {attempts} attempts left"
        elif attempts == 2:
            return f"The number is between {clue2}\nYou have {attempts} attempts left"
        elif attempts == 1:
            return f"The number is between {clue3}\nYou have {attempts} attempts left"
        
    # Checking the user's input
    if number_guessed == number:
        print("Congrats your guess is correct")
    else:
        while number_guessed != number and attempts != 0:
            attempts -= 1
            print(f"Attempts left: {attempts}")
            print(clue_output(attempts))
            number_guessed = int(input("Your guess is incorrect, try again: "))
            if attempts == 0:
                break

        else:
            print("Thank you for visiting. Goodbye!")
            break