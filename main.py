import json
import sys
import os
import re

print("Preparing..")

class NoSwearingAPI:
    def __init__(self):
        self.curses = json.load(open("swears.json", "r"))

    def clean_text(self, text):
        return re.sub(r'[^a-zA-Z]', '', text.lower())

    def scan(self, text):
        cleaned = self.clean_text(text)
        for word in self.curses["words"]:
            if word in cleaned:
                return True
        return False
