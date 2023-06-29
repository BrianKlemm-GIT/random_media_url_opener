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


def view_channels():
    i = 1
    for ch in channels:
        print(f"{i}.{ch}")
        i += 1
    return True


def save_channels():
    data_to_save = []
    for ch in channels:
        data_to_save.append({'name': ch.title, 'urls': ch.urls})

    with open('urls.json', 'w') as file:
        json.dump(data_to_save, file)


def add_channel():
    name = input("Enter the name of the new channel: ")
    new_channel = channel.Channel(name, [])
    channels.append(new_channel)
    save_channels()
    return True


def delete_channel():
    name = input("Enter the name of the channel to delete: ")
    user_choice = input(f"Are you sure you want to delete channel {name}? \n WARNING!! You cannot undo this! "
                        f"Y/N").lower()
    if user_choice == 'y':
        for ch in channels:
            if ch.title.lower() == name.lower():
                channels.remove(ch)
                save_channels()
                return True
        print("No such channel found.")
    return True


def play_channel():
    channel_name = input("Enter the name of the channel you want to play: ").lower()
    for ch in channels:
        if ch.title.lower() == channel_name:
            ch.play_media()
            return True
    print("No such channel found.")
    return True


def add_url():
    channel_name = input("Which channel would you like to add a URL to?").lower()
    new_url = input("What is the URL?")

    for ch in channels:
        if ch.title.lower() == channel_name:
            ch.add_url_direct(new_url)
            save_channels()  # Remember to save changes
            return True
    print("No such channel found.")
    return True


def incorrect_selection():
    print("You have selected incorrectly.")
    user_choice = input("Would you like to try once more? Y/N").lower()
    return user_choice == 'y'


main_menu = {
    '1': play_channel,
    'play': play_channel,
    '2': view_channels,
    'view': view_channels,
    '3': add_url,
    'add url': add_url,
    '4': add_channel,
    'add channel': add_channel,
    '5': delete_channel,
    'delete channel': delete_channel,
    '6': lambda: False,
    'exit': lambda: False
}
