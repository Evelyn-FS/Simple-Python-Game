    # Difficulty settings logic
while True:
    print("Main Menu")
    while True:
        print("Difficulty settings...")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Current level")
        difficulty = input("> Type '0' to back to main menu: ")

        if difficulty == "1":
            print("\n== Easy Mode Selected ==\n")

        while difficulty == "1":
            print("======Settings======")
            print("1. Info")
            print("0. Back to main menu")
            print("====================")
            easy = input("> Your choice: ")

            if easy == "1":
                print("You will recieve 10 attempts to guess the number.\nThe clues will be more detailed and easier to understand.\nGood luck!")
                continue
            elif easy == "0":
                print("\nSetting back to main menu...\n")
                break
            else:
                while True:
                    easy = input("Your choice is invalid, please try again: ")
                    if easy in ["1", "0"]:
                        break # Exit the inner loop if the input is valid