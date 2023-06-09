import random
import webbrowser


class Channel:
    def __init__(self, type, url):
        self.type = type
        self.url = url

    def add_url(self):
        new_url = input("Enter the full URL you would like to add.")
        self.url.append(new_url)

    def remove_url(self):
        remove_url = input("Enter the full URL you would like to remove.")
        self.url.remove(remove_url)

    def play_media(self):
        video = random.choice(self.url)
        webbrowser.open(video, new=1)

    def display_urls(self):
        print(self.url)


