import random
import webbrowser


class Channel:
    def __init__(self, type, urls):
        self.type = type
        self.urls = urls

    def add_url_direct(self, url):
        self.urls.append(url)

    def remove_url(self):
        remove_url = input("Enter the full URL you would like to remove.")
        self.urls.remove(remove_url)

    def play_media(self):
        video = random.choice(self.urls)
        webbrowser.open(video, new=1)

    def display_urls(self):
        print(self.urls)

    def __str__(self):
        return self.type



