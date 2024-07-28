from googletrans import Translator
from gtts import gTTS
import os
from playsound import playsound

def identify_language(text):
    translator = Translator()
    detection = translator.detect(text)
    return detection.lang


def main():
    text = input("Enter the text: ")
    lang = identify_language(text)
    print(lang,text)

main()