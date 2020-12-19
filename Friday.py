import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
#this assisstant is strictly for Developers and will consist of most of their daily needs at a single place
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0
].id)
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def boot():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Morning!")
    elif hour>=12 and hour<18:
        speak("Afternoon!")
    else:
        speak("Evening!")
    speak("wassup")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        r.energy_threshold=300
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again boss...")
        return "None"
    
if __name__=="__main__":
    boot()
    query=takeCommand().lower()
    if 'wiki' in query:
        speak('Searching Wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        speak(results)
        print(results)
        
        
    elif 'open youtube' in query:
            webbrowser.open("youtube.com")

    elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
            
    elif 'note' in query:
            speak('what should i write')
            querywrite=takeCommand()
            speak('Hour please?')
            queryhour=takeCommand()
            speak('minutes please?')
            queryminute=takeCommand()
            querytime=queryhour+'hours'+queryminute+'minutes'
            f = open("file.txt", "r+")
            f.write(querywrite+'remind at'+querytime)
            f.close()
            if (datetime.datetime.now().strftime("%H:%M")==querytime):
                speak('reading your schedule')
                f = open('file.txt','r')
                print(f.read())
                queryread=f.read()
                speak(queryread)
                f.close()
            #speak only the number of hour and minutes 
    elif 'bookmark' in query:    
        book={
        "psychological warfare":50
         }
        speak('which one')
        book1=takeCommand()
        path=book1+'.pdf'
        f=open(path,"r+")
        with open(path, 'rb') as f:
            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()
      
        speak(info.title)
        speak('by'+info.author)
        speak('which bookmark')
        page = pdf.getPage(book["book1"])
        text = page.extractText()
        print(text)
        speak('Should i speak the page?')
        check=takeCommand()
        if check=='yes':
            speak(text)
        
        
    elif 'mood check' in query:
        speak('Hey, how you feeling bud')
        f = open("Moodfile.txt", "a+")
        moodcheck=takeCommand()
        f.write(moodcheck+'\n at '+datetime.datetime.now().strftime("%H:%M"))
        f.close()
            
    elif 'plot' in query:
        speak("Inflation Graph beig plotted")
        df = pd.read_csv("cumulative.csv", delim_whitespace=True)
        df
        plt.plot(df["CPI-Value"], df["Date"], 'ro--')
        plt.show()
    