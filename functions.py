import channel
import json

channels = []

def load_channels():
    global channels
    with open('urls.json', 'r') as file:
        data = json.load(file)

    for channel_data in data:
        new_channel = channel.Channel(channel_data['name'], channel_data['urls'])
        channels.append(new_channel)


def save_channels():
    data_to_save = []
    for ch in channels:
        data_to_save.append({'name': ch.type, 'urls': ch.urls})

    with open('urls.json', 'w') as file:
        json.dump(data_to_save, file)


def add_channel():
    name = input("Enter the name of the new channel: ")
    new_channel = channel.Channel(name, [])
    channels.append(new_channel)
    save_channels()


def delete_channel():
    name = input("Enter the name of the channel to delete: ")
    user_choice = input(f"Are you sure you want to delete channel {name}? \n WARNING!! You cannot undo this! "
                        f"Y/N").lower()
    if user_choice == 'y':
        for ch in channels:
            if ch.type.lower() == name.lower():
                channels.remove(ch)
                save_channels()
                return
        print("No such channel found.")


def play_channel():
    channel_name = input("Enter the name of the channel you want to play: ").lower()
    for ch in channels:
        if ch.type.lower() == channel_name:
            ch.play_media()
            return
    print("No such channel found.")


def add_url():
    channel_name = input("Which channel would you like to add a URL to?").lower()
    new_url = input("What is the URL?")

    for ch in channels:
        if ch.type.lower() == channel_name:
            ch.add_url_direct(new_url)
            save_channels()  # Remember to save changes
            return
    print("No such channel found.")


def incorrect_selection():
    print("You have selected incorrectly.")
    user_choice = input("Would you like to try once more? Y/N").lower()
    return user_choice == 'y'


main_menu = {
    '1': play_channel,
    'play': play_channel,
    '2': add_url,
    'add url': add_url,
    '3': add_channel,
    'add channel': add_channel,
    '4': delete_channel,
    'delete channel': delete_channel,
    '5': lambda: False,
    'exit': lambda: False
}
