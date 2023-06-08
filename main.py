import webbrowser
import random
import json

with open('urls.json', 'r') as file:
    urls = json.load(file)

chillVideos = urls['chillVideos']
highEnergyVideos = urls['highEnergyVideos']

def play_chill():
    video = random.choice(chillVideos)
    webbrowser.open(video, new=1)

def play_high_energy():
    video = random.choice(highEnergyVideos)
    webbrowser.open(video, new=1)


def add_url():
    user_choice = input("Which playlist would you like to add a url to? Chill or High Energy").lower()
    new_url = input("What is the url?")
    if user_choice == "chill":
        chillVideos.append(new_url)
    elif user_choice == "high energy":
        highEnergyVideos.append(new_url)
    else:
        print("You have selected incorrectly.")
        return

    with open('urls.json', 'w') as file:
        json.dump({
            'chillVideos': chillVideos,
            'highEnergyVideos': highEnergyVideos,
        }, file)

    return True


def incorrect_selection():
    print("You have selected incorrectly.")
    user_choice = input("Would you like to try once more? Y/N").lower()
    return user_choice == 'y'


menu = {
    'chill': play_chill,
    'high energy': play_high_energy,
    'add url' : add_url,
    'exit': lambda: False,  # Return False to stop the loop
}

keep_going = True

while keep_going:
    choice = input("--Main Menu--\n"
                   "The choices are as follows:\n 1. Chill\n 2. High Energy\n 3. Add URL\n 4.Exit\n").lower()
    action = menu.get(choice, incorrect_selection)
    keep_going = action()
