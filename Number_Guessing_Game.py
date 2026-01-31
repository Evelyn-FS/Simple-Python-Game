import random

print(" ")
print("===================================")
print(" ")
print("Welcome to the Number Guessing Game")
print(" ")
print("===================================")
print(" ")

# Generating a random number
number = random.randint(1, 100)

# Defining clues and attempts
clue_number = [20, 10, 5]
attempts = 0

# Asking the user to give an input
number_guessed = int(input("Please select a number from 1-100: "))

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
        less1, more1 = less, more
    elif i == 1:
        less2, more2 = less, more
    elif i == 2:
        less3, more3 = less, more

# Function to provide clues based on attempts
def clue(attempts):
    if attempts == 1:
        return f"The number is between {less1} and {more1}"
    elif attempts == 2:
        return f"The number is between {less2} and {more2}"
    elif attempts == 3:
        return f"The number is between {less3} and {more3}"
    return f"NICE TRY! The actual number is '{number}'"

# Checking the user's input
if number_guessed == number:
    print("Congrats your guess is correct")
else:
    while number_guessed != number and attempts <= 3:
        attempts += 1
        print(clue(attempts))
        number_guessed = int(input("Your guess is incorrect, try again: "))