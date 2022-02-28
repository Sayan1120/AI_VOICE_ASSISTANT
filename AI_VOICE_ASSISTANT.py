import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
from datetime import date
import randfacts

engine = pyttsx3.init()
engine.setProperty("rate", 175)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[2].id)
recognizer = sr.Recognizer()


def engineTalk(text):
    engine.say(text)
    engine.runAndWait()


def runAlexa():


    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('\n')
        print("Start Speaking")
        engineTalk("Listening....")
        recordedAudio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(recordedAudio, language='en-in')
        command = command.lower()
        if "alexa" in command:
            command = command.replace("alexa")
            print(f"You said {command}")

        else:
            print(f"You said {command}")

        if 'hello' in command:
            print("Hello, how may I help you?")
            engineTalk("Hello, how may I help you?")

        elif 'who are you' in command:
            print("I am alexa your virtual assistant aka your bestfriend🤟")
            engineTalk("I am alexa your virtual assistant aka your bestfriend")

        elif 'what can you do' in command:
            print("""I can play songs on youtube, tell you a joke, search on wikipedia, tell date and time, find your location, locate area on map, open different websites like instagram, youtube, gmail, git hub, Stack overflow, twitter, linkedin and searches on Google and even tell you some random facts, how may I help you?😎""")

            engineTalk("""I can play songs on youtube, tell you a joke, search on wikipedia, tell date and time, find your location, locate area on map, open different websites like Instagram, youtube, gmail, git hub, Stack overflow twitter, linkedin and searches on Google and even tell you some random facts, how may I help you?""")

        elif 'play song' in command:
            song = command.replace('play', '')
            print(f"Playing {song}")
            engineTalk(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'date and time' in command:
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
            date1 = today.strftime("%B %d, %Y")
            print("Today's date is ", date1, "Current time is ", time)
            engineTalk(f"Today is {date1}")
            engineTalk(f"and current time is {time}")

        elif 'time and date' in command:
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
            date1 = today.strftime("%B %d, %Y")
            print("Today's date is ", date1, " and current time is ", time)
            engineTalk("Today is {}".format(date1))
            engineTalk(f"and current time is {time}")

        elif 'date' in command:
            today = date.today()
            print("Today's date is {today}")
            date1 = today.strftime("%B %d, %Y")
            print("Today's date is {}".format(date1))
            engineTalk("Today's date is ")
            engineTalk(date1)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(f"Current time is {time}")
            engineTalk(f"Current time is {time}")

        elif 'tell me about' in command:
            engineTalk("Searching Wikipedia....")
            name = command.replace("tell me about", "")
            results = wikipedia.summary(name, sentences=2)
            engineTalk("According to Wikipedia")
            print(results)
            engineTalk(results)

        elif 'wikipedia' in command:
            engineTalk("Searching Wikipedia....")
            name = command.replace("wikipedia", "")
            results = wikipedia.summary(name, sentences=2)
            engineTalk("According to Wikipedia")
            print(results)
            engineTalk(results)

        elif 'who is ' in command:
            engineTalk("Searching Wikipedia....")
            name = command.replace('who is', '')
            results = wikipedia.summary(name, 1)
            engineTalk("According to wikipedia")
            print(results)
            engineTalk(results)

        elif 'who was' in command:
            engineTalk("Searching Wikipedia....")
            name = command.replace("who was", "")
            results = wikipedia.summary(name, sentences=3)
            engineTalk("According to Wikipedia")
            print(results)
            engineTalk(results)

        elif 'what is' in command:
            search = 'https://www.google.com/search?q=' + command
            print("Here's what I found on internet....")
            engineTalk("Searching....")
            webbrowser.open(search)

        elif 'where is ' in command:
            engineTalk('locating ...')
            loc = command.replace('where is', '')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            engineTalk('Here is the location of '+loc)

        elif 'tell me a joke' in command:
            Jokes = pyjokes.get_joke()
            print(Jokes)
            engineTalk(Jokes)

        elif 'search' in command:
            search = 'https://www.google.com/search?q=' + command
            engineTalk("Searching....")
            webbrowser.open(search)

        elif 'searching my location' in command:
            url = "https://www.google.com/maps/search/where+am+I+?/"
            webbrowser.get().open(url)
            engineTalk("According the google maps, you must be somewhere near here")

        elif 'locate ' in command:
            engineTalk('locating ...')
            loc = command.replace('locate', '')
            if 'on map' in loc:
                loc = loc.replace('on map', ' ')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            engineTalk('Here is the location of '+loc)

        elif 'bootcamps' in command:
            search = 'http://tathastu.twowaits.in/kickstart_full_stack_development.html' + command
            engineTalk("Searching for the bootcamps....")
            engineTalk("Opening bootcamps")
            webbrowser.open(search)

        elif 'boot camps' in command:
            search = 'http://tathastu.twowaits.in/kickstart_python.html' + command
            engineTalk("Searching for the bootcamps....")
            engineTalk("Opening bootcamps")
            webbrowser.open(search)

        elif 'data science bootcamps' in command:
            search = 'http://tathastu.twowaits.in/kickstart_data_science.html' + command
            engineTalk("Searching for the bootcamps....")
            engineTalk("Opening bootcamps")
            webbrowser.open(search)

        elif 'open google' in command:
            print("Opening google...")
            engineTalk("Opening Google...")
            webbrowser.open_new('https://www.google.com/')

        elif 'open gmail' in command:
            print("Opening gmail....")
            engineTalk("Opening gmail....")
            webbrowser.open_new('https://mail.google.com/')

        elif 'open youtube' in command:
            print("Opening Youtube....")
            engineTalk("Opening Youtube....")
            webbrowser.open_new('https://www.youtube.com/')

        elif 'open stack overflow' in command:
            print("Opening Stack overflow...")
            engineTalk("Opening Stack Overflow...")
            webbrowser.open_new('https://stackoverflow.com/')

        elif 'open instagram' in command:
            print("Opening Instagram...")
            engineTalk("Opening Instagram...")
            webbrowser.open_new('https://www.instagram.com/?hl=en')

        elif 'open github' in command:
            print("Opening Github")
            engineTalk("Opening Github")
            webbrowser.open_new('https://github.com/')

        elif 'open twitter' in command:
            print("Opening Twitter...")
            engineTalk("Opening Twitter...")
            webbrowser.open_new('https://twitter.com/?lang=en')

        elif 'open linkedin' in command:
            print("Opening Linkedin...")
            engineTalk("Opening Linkedin...")
            webbrowser.open_new('https://www.linkedin.com/')

        elif 'tell me a fact' in command:
            engineTalk("Searching for a random fact")
            Y = randfacts.get_fact()
            print("Here'a random fact just for you😇")
            engineTalk("Here's a random fact just for you")
            print(Y)
            engineTalk(Y)

        elif 'bye' in command:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                print("Good bye and have a good morning!😄")
                engineTalk("Good bye and have a good morning!")

            elif hour >= 12 and hour < 18:
                print("Good bye and have a good afternoon!😄")
                engineTalk("Good bye and have good afternoon!")

            else:
                print("Good bye and have a good night!😄")
                engineTalk("Good bye and have a good night!")
            print(hour)
            sys.exit()

        elif 'thank you' in command:
            print("You're Welcome!😄")
            engineTalk("You're Welcome!")

        elif 'thanks' in command:
            print("You're Welcome!😄")
            engineTalk("You're Welcome!")

        elif 'see you again' in command:
            print("We'll meet again!😇")
            engineTalk("We'll meet again!")
            sys.exit()

        elif 'stop' in command:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                print("Good bye and have a good morning!😄")
                engineTalk("Good bye and have a good morning!")

            elif hour >= 12 and hour < 18:
                print("Good bye and have a good afternoon!😄")
                engineTalk("Good bye and have good afternoon!")

            else:
                print("Good bye and have a good night!😄")
                engineTalk("Good bye and have a good night!")
            print(hour)
            sys.exit()

        else:
            print("Here's what I found on the internet..🖐️")
            engineTalk("Here's what I found on the internet..")
            search = 'https://www.google.com/search?q='+command
            webbrowser.open(search)

    except Exception as e:
        print(e)


print("Clearing Background noise...Please wait!")
engineTalk("Clearing Background noise...Please wait!")
print("\n")
print("Hello, I am mini Alexa, How may I help you?")
engineTalk("Hello, I am mini Alexa, How may I help you?")

while True:
    runAlexa()
