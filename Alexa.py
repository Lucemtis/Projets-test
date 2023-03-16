import speech_recognition as sr
import pyttsx3
import pywikibot
import wikitextparser

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def choose_microphone():
    return sr.Microphone(device_index=4)

def take_command():
    try:
        with choose_microphone() as source:
            print("listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='fr-FR')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', "")
                print(command)
    except:
        command = ""
    return command

def run_alexa():
    command = take_command()
    print(command)
    site = pywikibot.Site('fr', 'wikipedia')
    page = pywikibot.Page(site, command)
    text = wikitextparser.parse(page.text).sections[0].plain_text()
    print(text)
    talk(text)


while True:
    run_alexa()
