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

Difficulty_Info = {
    "Easy": "You will recieve 10 attempts to guess the number.\nThe clues will be more detailed and easier to understand.\nGood luck!",
    "Medium": "You will recieve 7 attempts to guess the number.\nThe clues will be less detailed and more challenging to understand.\nGood luck!",
    "Hard": "You will recieve 5 attempts to guess the number.\nThe clues will be very vague and difficult to understand.\nGood luck!"
}
    

while True:
    print("== Difficulty Settings Menu ==")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Current level")
    settings = input("> Type '0' to back to main menu: ")

    if settings == "1":
        mode = "Easy"
        print("\n== Easy Mode Selected ==\n")
        while settings == "1":
            print("======Settings======")
            print("1. Info")
            print("0. Back to main menu")
            print("====================")
            difficulty = input("> Your choice: ")
            if difficulty == "1":
                print("You will recieve 10 attempts to guess the number.\nThe clues will be more detailed and easier to understand.\nGood luck!")
                continue
            elif difficulty == "0":
                print("\nSetting back to Difficulty Settings...\n")
                break
            else:
                while difficulty not in ["1", "0"]:
                    difficulty = input("Your choice is invalid, please try again: ")
                    if difficulty in ["1", "0"]:
                        break # Exit
            print("\nSetting back to Difficulty Settings...\n")
            break
    
    elif settings == "2":
        print("\n== Medium Mode Selected ==\n")
        mode = "Medium"
        while settings == "2":
            print("======Settings======")
            print("1. Info")
            print("0. Back to main menu")
            print("====================")
            difficulty = input("> Your choice: ")
            if difficulty == "1":
                print("You will recieve 7 attempts to guess the number.\nThe clues will be less detailed and more challenging to understand.\nGood luck!")
                continue
            elif difficulty == "0":
                print("\nSetting back to Difficulty Settings...\n")
                break
            else:
                while difficulty not in ["1", "0"]:
                    difficulty = input("Your choice is invalid, please try again: ")
                    if difficulty in ["1", "0"]:
                        break # Exit
            print("\nSetting back to Difficulty Settings...\n")
            break

    elif settings == "3":
        print("\n== Hard Mode Selected ==\n")
        mode = "Hard"
        while settings == "3":
            print("======Settings======")
            print("1. Info")
            print("0. Back to main menu")
            print("====================")
            difficulty = input("> Your choice: ")
            if difficulty == "1":
                print("You will recieve 5 attempts to guess the number.\nThe clues will be very vague and difficult to understand.\nGood luck!")
                continue
            elif difficulty == "0":
                print("\nSetting back to Difficulty Settings...\n")
                break
            else:
                while difficulty not in ["1", "0"]:
                    difficulty = input("Your choice is invalid, please try again: ")
                    if difficulty in ["1", "0"]:
                        break # Exit
            print("\nSetting back to Difficulty Settings...\n")
            break

    elif settings == "4":
        current_difficulty(mode)
        continue

    elif settings == "0":
        print("\nReturning to main menu...\n")
        break

    else:
        while settings not in ["1", "2", "3", "4", "0"]:
            settings = input("Your choice is invalid, please try again: ")
            if settings in ["1", "2", "3", "4", "0"]:
                break # Exit
