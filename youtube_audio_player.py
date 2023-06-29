import functions

keep_going = True

functions.load_channels()

while keep_going:
    choice = input("\n--Main Menu--\n"
                   "The choices are as follows:\n 1. Play a Channel\n 2. View Channels\n 3. Add URL to a Channel\n "
                   "4. Add Channel\n 5. Delete Channel\n 6. Exit\n").lower()
    action = functions.main_menu.get(choice, functions.incorrect_selection)
    keep_going = action()
