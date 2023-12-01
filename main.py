# Import libraries
import os
import subprocess
import webbrowser
import pyttsx3 as converter
import speech_recognition as recognizer
import time
import wikipedia
from gtts import gTTS

# Set up speech engine
engine = converter.init()

# Listener object
Listener = recognizer.Recognizer()

# Function to respond to user


def response(message):
    engine.say(message)
    time.sleep(1)
    engine.runAndWait()

# Function to recognize spoken command and convert to text using google recognizer


def recognizeCommand(audio):
    query = None
    try:
        query = Listener.recognize_google(audio, language='en-ke')
        print('Given command is ', query)

    except recognizer.UnknownValueError:
        print('Sorry! Audio was not recognized by Google Speech Recognition.')

    except recognizer.RequestError as e:
        print('Request Failed; {0}'.format(e))

    except:
        print('Unable to recognize ')
        return query


def respond(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save('speech.mp3')
    os.system('mpg321 speech.mp3')


# Function to listen to commands using microphone


def listenCommand():
    response('How may I assist you?')

    with recognizer.Microphone() as source:
        command = Listener.listen(source)

    query = recognizeCommand(command)
    return query


if __name__ == '__main__':
    query = listenCommand()

    # You can use the above query to perform tasks as per requirements

    # Repeat given query
    response('repeating query')
    time.sleep(1)
    response(query.lower())
    
    if 'wikipedia' in query:
            response('Searching Wikipedia...')
            statement = query.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            response("According to Wikipedia")
            print(results)
            response(results)
            
    elif "log off" in query or "sign out" in query:
            response("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
			
    time.sleep(3)

    # Search on wikipedia
    response('Searching on wikipedia...')
    try:
        result = wikipedia.summary(query, sentences=3)
        response('According to wikipedia')
        time.sleep(1)
        response(result.lower())

    except:
        response('Search failed')
