import functions

keep_going = True

functions.load_channels()

while keep_going:
    choice = input("--Main Menu--\n"
                   "The choices are as follows:\n 1. Play a Channel\n 2. Add URL to a Channel\n 3. Add Channel\n "
                   "4. Delete Channel\n 5. Exit\n").lower()
    action = functions.main_menu.get(choice, functions.incorrect_selection)
    action()

    user_selection = input("Would you like to continue operating the player? Y/N").lower()
    if user_selection != 'y':
        keep_going = False
