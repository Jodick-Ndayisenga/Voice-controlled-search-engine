import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
# Here if you want to get a particular voice
voices = engine.getProperty('voices')
# and here we got all the voices
engine.setProperty('voice', voices[1].id)
# we are setting the voice property that is on the index 1 to be our voice now
musics = ['Girlfriend by Ruger', 'Kwikwi by Zuchu', 'Cough(odo) ft.Empire', 'Nakupenda by Jay Melody',
          'Rush by Ayra Starr', 'Buga(lo lo lo) ft.techno', 'Fire by Zuchu', 'for my hand ft.Ed sheeran', 'Overloading(overdose) ft.Crayon, Ayra Starr', 'Desh Desh By Lava lava', 'Calm down by Rema', 'Nights Aviichi', 'Mad By neyo']

engine.say("Hey, what's up? My name is unonymous, a robot developped by Jodick Ndayisenga; Hope I will be able to serve you the best I can.")
engine.runAndWait()


def talk(words):
    engine.say(words)
    engine.runAndWait()
    # this run and wait function help to tell the engine to wait after it has run for other codes to run


def take_command():
    try:
        with sr.Microphone() as source:
            # we set our mic as source, this means, the input is now mic
            talk('Listening...')
            voice = listener.listen(source)
            command = (listener.recognize_google(voice)).lower()
            # this is telling google to get a text from whatever we said
            # print(command)
            if 'babe' in command and 'girlfriend' in command:
                command = command.replace('babe', '')
                command = command.replace('girlfriend', '')

            if 'babe' in command:
                command = command.replace('babe', '')

            if 'girlfriend' in command:
                command = command.replace('girlfriend', '')

    except:
        pass

    return command


def run_command():
    command = take_command()
    if 'play' in command:
        sentence = command.split()
        ind = sentence.index('play')
        song = sentence[ind+1:]
        word = ''

        word = ' '.join(song)

        print(word)
        talk('Playing' + word)
        pywhatkit.playonyt(word)

    elif 'time' in command:
        now = datetime.datetime.now().strftime('%I:%m:%p')
        if now[0] == 0:
            now = now[1:]
        print(now)
        # the strftime is the way to customize the way we want to get time read, I means we want to get 12hours format time
        # and p for either pm or am
        talk('Current time is ' + now)

    elif 'wikipedia' in command or 'who' in command or 'how' in command or 'what' in command:
        command = wikipedia.summary(command, 2)
        # print(command)
        talk(command)

    elif 'boyfriend' in command or 'honney' in command or 'romantic' in command:
        talk('The only man I ever have loved is Jodick Ndayisenga.')

    elif 'some music' in command or 'some song' in command or 'random music' in command or 'random music' in command:
        tune = random.choice(musics)
        talk(f'Gimme a second, I am going to play {tune}')
        pywhatkit.playonyt(tune)

    elif 'joke' in command or 'jokes' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    else:
        talk('Please, I did not get that. Can you say it again?')


while True:
    talk("So, who am I talking to? Tell me what you want me to do.")
    with sr.Microphone() as source:
        who = listener.listen(source)
        name = (listener.recognize_google(who).lower())
        if '2' not in name:
            talk(
                'Sorry, I do not know your name. Can you try again or ask the permission from Jodick?')
            continue
        else:
            talk('Ooh, yeah. How are you Jodick? ')
            while True:
                run_command()
                talk('Lemme know if there is anything else I can help you.')
