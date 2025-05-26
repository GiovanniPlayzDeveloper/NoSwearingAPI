from datasets import load_dataset
import json
import sys
import os
import re

print("Preparing..")

class NoSwearingAPI:
    def __init__(self):
        self.curses = json.load(open("swears.json", "r"))

    def scan(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        for word in words:
            if word in self.curses["words"]:
                return True
        return False

api = NoSwearingAPI()
apiInfo = json.load(open("api.json", "r"))

os.system("clear")
print("TextGuard API Playground")
print(f"Developed by {apiInfo['author']} on {apiInfo['date']}")
print("Features in TextGuard API:")
for feature in apiInfo["features"]:
    print(f"- {feature}")
print("Enjoy testing TextGuard API!")

while True:
    try:
        userInput = input("\nEnter text: ")
        if api.scan(userInput):
            print("Text contains harmful words or phrases.")
        else:
            print("Text is safe and does not contain harmful words or phrases.")
    except KeyboardInterrupt:
        os.system("clear")
        print("Stopping..")
        sys.exit(1)
        
    except Exception as e:
        os.system("clear")
        print(f"Sorry, something went wrong. If this happens again, please report it to our Discord server.\n The following error has occurred: {e}")
        sys.exit(1)