# Difficulty settings logic

print("\n== Main Menu ==\n")

mode = ""

def difficulty_sub_menu(mode):
    print(f"\n== {mode} Mode Selected ==\n")
    while True:
        print("======Settings======")
        print("1. Info")
        print("0. Back to main menu")
        print("====================")
        choice = input("> Your choice: ")
        if choice == "1":
            print(Difficulty_Info[mode])
        elif choice == "0":
            print("\nSetting back to Difficulty Settings...\n")
            break
        else:
            print("Your choice is invalid, please try again.")
    return mode

def current_difficulty(mode):
    if mode == "Easy":
        print("\n=> Your current difficulty level is >Easy<.\n")
    elif mode == "Medium":
        print("\n=> Your current difficulty level is >Medium<.\n")
    elif mode == "Hard":
        print("\n=> Your current difficulty level is >Hard<.\n")
    else:
        print("\n=> No difficulty level selected yet.\n")

def get_valid_input(prompt, valid_options):
    choice = input(prompt)
    while choice not in valid_options:
        choice = input("Your choice is invalid, please try again: ")
    return choice

Difficulty_Info = {
    "Easy": "You will recieve 10 attempts to guess the number.\nThe clues will be more detailed and easier to understand.\nGood luck!",
    "Medium": "You will recieve 7 attempts to guess the number.\nThe clues will be less detailed and more challenging to understand.\nGood luck!",
    "Hard": "You will recieve 5 attempts to guess the number.\nThe clues will be very vague and difficult to understand.\nGood luck!"
}

Difficultu_Options = {
    "1": "Easy",
    "2": "Medium",
    "3": "Hard"}

while True:
    print("== Difficulty Settings Menu ==")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Current level")

    settings = input("> Type '0' to back to main menu: ")

    if settings == "1":
        mode = "Easy"
        difficulty_sub_menu(mode)
    elif settings == "2":
        mode = "Medium"
        difficulty_sub_menu(mode)
    elif settings == "3":
        mode = "Hard"
        difficulty_sub_menu(mode)
    

    settings = get_valid_input("Select a difficulty level:\n1. Easy\n2. Medium\n3. Hard\n0. Exit\n> Your choice: ", ["1", "2", "3", "0"])
    if settings in Difficultu_Options:
        mode = Difficultu_Options[settings]
    elif settings == "4":
        current_mode = current_difficulty(mode)
    elif settings == "0":
        print("Exiting the program. Goodbye!")
        break