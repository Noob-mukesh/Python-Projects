import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser,requests
import pyaudio,os,time
from random import choice

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    """ this will wish user
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour <= 12:
        speak("good morning ,babe ")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon ,babe")
    elif hour >= 18 and hour <= 20:
        speak("good evening ,babe")
    else:
        speak("good night ,babe")

    speak("hello babe ,,,,,,how can i help ,,,,,,,,,,,,,,,,you my darling")


# def sendEmail():
#     pass
#   will not work due to change in privacy of google


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....\n please say how i can help u?....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogining dear wait for  a while...........")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said :--{query}")
    except Exception as e:
        # print(e)
        print("say  it again please:>>>>>")
        return "None"
    return query


if __name__ == "__main__":
    # speak("mukesh is a good boy")
    wishme()

    while True:
        query = takecommand().lower()
    #  logic
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(f"according to wikipedia {result}")
            print(result)
        if "open youtube" in query:
            webbrowser.open("youtube.com")
        if "open google" in query:
            webbrowser.open("google.com")
        if "open my photo" in query:
            loc = "C:\\Users\\mukes\\OneDrive\\Pictures\\Screenshots\\Screenshot (28).png"
            
        
            os.startfile(loc)
        if "play" in query:
            songnames=query.replace("play","")
            songname=query.replace(" ","")
        
            resp=requests.get(f"https://mukesh-api.vercel.app/songsearch?query={songname}").json()["url"]
            try:
                webbrowser.open(resp)
            except:
                pass

        if "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the  time is  {strtime}")
        
        if "gpt"  in query:
    
            resp=requests.get(f"https://mukesh-api.vercel.app/chatgpt?query={query}").json()["results"]
            # if not os.path.exists("gpt"):
            #     os.makedirs("gpt")
            # with open(f"gpt/response1.txt" ,"w") as f:
                
            #     f.write(resp)
            #     f.close()
            # os.startfile("gpt\\response1.txt")
            
            print(resp)
            speak(resp)
        if "thank" in query:
            speak("You are welcome babe ,how useful i am for you ?̥give me rating please..")

        if "stop" in query:
            exit()