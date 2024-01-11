import pyttsx3 #this module is used to convert text to speech
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import subprocess

engine = pyttsx3.init('sapi5') #it will provide an api to give a voice
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #we have chose a voice provided by the api

def speak(audio): #the computer speaks out the data given as input in the parmeter
    engine.say(audio) #speaks
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
      speak("GOOD MORNING CHETANA, HAVE A GREAT MORNING!!")

    elif hour>=12 and hour<16: 
      speak("GOOD AFTERNOON CHETANA, HOPE YOU HAD YOUR YUMMY MEAL!!")

    elif hour>=16 and hour<20: 
      speak("GOOD EVENING CHETANA, HOPE YOU HAD A GREAT DAY!!")  

    else:
     speak("GOOD NIGHT CHETANA, SLEEP WELL!!")
    speak("I AM JARVIS , HOW MAY I HELP YOU CHETANA!!")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer() #this will help recognize audio  
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source) #the input user gives through the microphone

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Chetana: {query}\n")

    except Exception as e:
        print("I am unable to understand, could you please repeat")
        return "None"
    return query 
def introduction():
   print("Hi, I am JARVIS one point zero")
   speak('Hi, I am JARVIS one point zero')
     

if __name__ == "__main__":
    wishMe()
    while True:
      query = takeCommand().lower()

      if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        result =wikipedia.summary(query, sentences=2)
        speak("According to wikipedia:")
        print(result)
        speak(result)

      elif 'open google' in query:
        speak('opening google')
        webbrowser.open("google.com")

      elif 'open youtube' in query: 
        speak('opening youtube')
        webbrowser.open("youtube.com")

      elif 'play music' in query:
        webbrowser.open("spotify.com")  

      elif 'how are you' in query:
         speak('I am fine chetana, how are you')

      elif 'I am good' in query:
         speak('good to hear chetana') 

      elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Chetana, the time is: {strTime}")  

      elif 'open code' in query:
         # codePath = "path to your file"
         os.startfile(codePath)

      elif 'your name' in query:
         print("My name is JARVIS")
         speak('My name is JARVIS')
     
      elif 'who are you' in query:
         speak('I am JARVIS one point zero')

      elif 'weather' in query:
        data = webbrowser.open("weather.com")  
        speak(data)

      
      elif 'jokes' in query:
         speak(pyjokes.get_jokes())

      elif 'shutdown' in query:
         speak('Hold on a second, your system will shutdown soon')
         subprocess.call('shutdown / p /f') 

      elif 'love you' in query:
         speak('I dont understand such feelings')  

      elif 'created you' in query or 'made you' in query:
         speak('I was created by my master Chetana') 

      elif 'quit' in query or 'bye' in query:
         speak('Had a great time talking to you,hope we meet soon')
         exit()

      elif 'yourself' in query:
         introduction() 

      elif 'open chat GPT' in query:
         webbrowser.open("chat.openai.com")     



      


