import pyttsx3
# This module is use to the speak the text
"""Please swap down and read some information about these codes"""
import speech_recognition as sr
# This module is use for the speech  or to convert voice in to the text
import datetime
import time
# This is module is user for the date and set to sleep and many of the things
import wikipedia
# This module is used for to open  search
import webbrowser
# This module is user for the access to internet
from tqdm import tqdm
import os
# This   the window feature use
import random
# This module is use for the random no
import requests
# This module is use for requests to get the info
import json
# This get the news from the website
try:
    import pywhatkit as kit
except Exception as e:
    pass
""" 
This  is create to convert text in to the speech 
"""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
def speak(audio):
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
# This is another speak for another voice
def speak1(audio):
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
"""  
This funcation is make for input from the user in the from of voice """
def takecommand (pause_threshold = 1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"USER SAID: {query}\n")
    except Exception as e:
        speak("I am sorry, sir"+"I am not hear properly,Please say again...")
        return takecommand()
    return query
"""
This funcation is open to start the particule key word """
def takecommand1 (pause_threshold = 1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recongnizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"USER SAID:{query}\n")
    except Exception as e:
        speak1("sorry sir,I have some error")
        speak1("It may be internet connnection error")
        return takecommand1()
    return query
def takecommand2 (pause_threshold = 1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        # print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
    except Exception as e:
        return takecommand2()
    return query
def takecommand3 (pause_threshold = 1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recongnizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"USER SAID:{query}\n")
    except Exception as e:
        return "New tradding song"
    return query
""" This is made by the wishe me like good morning and good eveninng like """
def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning!,sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!,sir")

    else:
        speak("Good Evening!,Sir")
    # speak(" I am jarvis a computer program ,Please tell me may I help you")
    """
 This funcation is made for the intor of the jarvish to the another person 
  """
def intro():
    speak("Hello sir, I am a computer program develope by mister 'AKASH KUMAR'")
    speak("and Your nice name is, Sir")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 500
        r.pause_threshold = 0.5
        audio = r.listen(source)
        """This is to handel the exception to speech"""
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"USER SAID: {query}\n")
        speak(f"Nice to meet you mister {query}\n")
    except Exception as e:
        speak("Nice to meet you sir")
"""
 This funcation is get the current news
  """
def news ():
    speak("News for today.. ")
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d093053d72bc40248998159804e0e67d"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        print(article['title'])
        speak(article['title'])
        speak("Next news is....")
def searchanythings(query):
    search_item = query.split("for")[-1]
    url = "https://google.com/search?q="+ query
    webbrowser.get().open(url)
    speak(f"There is search result on google {search_item}")
"""
This funcation is make the program is very aqurite and good """
def youtubesong(query):
    try:
        speak("Just a second sir")
        kit.playonyt(query)
        speak("I hope you enjoy this video")
    except Exception as e:
        speak("sorry Sir,I have some error")
def visit(pronounces):
    for pronounce in pronounces:
        if pronounce in query:
            return True

def visit1(pronounces):
    for pronounce in pronounces:
        if pronounce in query:
            return True


"""
That is the respone fucation to give the resope the  by the program
"""
def respose(query):
    """
    This is write the code to open the wikipedia"""
    if visit(['wikipedia']):
        try:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query , sentences= 3)
            speak("Sir,According to wikipedia...")
            speak(result)
        except Exception as e:
            speak("I am sorry, sir i can not do this work "+"I have a littel error")
            return takecommand()
# This statement is use for the introducation of the program
    elif visit(['give your introduction','tell me your introducation','intro do','who are you','intro','give me your intro','jarvis intro','sir,ko intro do','intro jarvis']):
        intro()
    elif visit(['hey','hello','hello jarvis','kase ho jarvis','ok jarvis','jarvis']):
        n = random.randint(0,2)
        if n==1:
            speak("Hello sir,"+"I am here")
        if n==2:
            speak("Welcome, Sir..."+"I am computer program")
        else:
            speak("Welcome back, sir")
    elif visit(['what are you doing']):
        speak("I am doing some fun,sir")

    elif visit(['open google']):
         webbrowser.open("google.com")
         speak("opening the google")
    elif visit(['open youtube']):
         webbrowser.open("youtube.com")
         speak("opening youtube")
# This satement is use for the time
    elif visit(['what time','the time','time jarvis','what time jarvis']):
         str_time = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir, the time is {str_time}\n")

    
# This is statment is use for the play song and next song
    elif visit(['play song','play music','next song','change song','gaana bjao','play audio','next audio','change the musics']):
          speak("If you want to play on youtube")
          print("Say:Yes/No")
          query3 = takecommand3().lower()
          if 'yes' in query3:
              speak("Which song you want to listen")
              query3 = takecommand3().lower()
              youtubesong(query3)
          else:
            n = random.randint(1, 28)
            mus_dir = "F:\\musics"
            song = os.listdir(mus_dir)
            speak("One minit,Sir")
            os.startfile(os.path.join(mus_dir, song[n]))
            speak("I hope, you enjoy this song")

    elif visit(['play video','video song','next video']):
          n = random.randint(3,226)
          video_dir='F:\\'
          song = os.listdir(video_dir)
          speak("One minit,Sir")
          os.startfile(os.path.join(video_dir,song[n]))
          speak("I hope you enjoy this video,Sir")

# These statment is use for the openning the app
    elif visit(['open chroem','open google chrome']):
          code_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
          os.startfile(code_path)
          speak("Opening google chrome")
    elif visit(['open vs code','open code','i want to coding','open bs code','open b s code']):
          code_path = "C:\\Users\\Akash\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"""
          os.startfile(code_path)
          speak('Opening vs code'+'enjoy coding on this IDE')
    elif visit(['open sub line','open sublime','open sub lime']):
          code_path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
          os.startfile(code_path)
          speak("Opening sublime")
    elif visit(['open browser','open window browser']) :
          code_path = "C:\\Program Files (x86)\Microsoft\\Edge\\Application\\msedge.exe"
          os.startfile(code_path)
          speak("Opening window browser")
    elif visit(['open pycharm']):
          code_path = "C:\\Program Files\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
          os.startfile(code_path)
          speak("Opening pycharm")
    elif visit(['open notepad plus plus']):
          code_path = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
          os.startfile(code_path)
          speak("Opening notepad ++")
    elif visit(['open typing master']):
          code_path = "C:\\Program Files (x86)\\TypingMaster10\\tmaster.exe"
          os.startfile(code_path)
          speak("Opening typing master")
# This statment is write the to open the the drive
    elif visit(['open c drive',"open cd drive"]):
           code_pathc = "C:\\"
           os.startfile(code_pathc)
           speak("openinng c derive")
    elif visit(['open e drive']):
           code_path = "E:\\"
           os.startfile(code_path)
           speak("openinng e derive")
    elif visit(['open f drive']):
           code_path = "F:\\"
           os.startfile(code_path)
           speak("openinng f derive")
# This statment is write the tell tell the news
    elif visit(['today news','news','taaja kabar','aaj ki news','koi taja kabr']):
           news()
    elif visit(['stup','chup','stupied','shut up']):
        speak("Sorry, sir")
        time.sleep(20)
        speak("I am back, Sir..")
    elif visit(['system shutdown']):
        speak("System shutdown")
        os.system("shutdown /s")
    elif visit(['system restart']):
        speak("system restarting")
        os.system("shutdown /r")
    elif visit(['system logoff','sing off']):
        speak("system loggoff")
        os.system("shutdown /l")
    elif visit(["who is your creater","who is made you","who is akash","how is aakash","who is your creator"]):
        speak("Mister Akash kumar is my creater")
        speak("and i am obey all order of mister aakash")
    elif visit(["rukja","ruk ja","stop"]):
        speak("ok sir, Program will be Temporary Stop")
        while True:
            query1 = takecommand2().lower()
            if "ok ready" in query1:
                print("ok ready,sir")
                speak("ok ready ,sir")
                return False
    elif visit(['search video','search on youtube']):
        speak("what you want to serch on youtube")
        query = takecommand().lower()
        youtubesong(query)
    elif visit(['exit','quit','never back','out','gate out','gate lost']):
        speak("bye , Sir"+"have a nice day")
        os.system("exit")
        quit()
    else:
        speak("sir,you want to this search on google")
        print("sir,you want to this search on google 'say Yes/NO '")
        query1 = takecommand().lower()
        if 'yes'in query1:
            speak("ok sir I search on google")
            searchanythings(query)
        else:
            speak("ok sir")
            return True
if __name__ == '__main__':
    wishme()
    speak("Hello,sir Please,tell me the password")
    print("you have only 3 chance")
    i=0
    chance = 3

    while True:
        query = takecommand1().lower()
        if chance == 1:
            speak("i stop this program")
            exit()
        i += 1
        chance -= 1

        if "ok" in query:
            print("correct password")
            speak("welcome sir, I am a computer a program")
            speak("I am rady,to obey your order")
            while True:
                query = takecommand().lower()
                respose(query)
        else:
            print("wrong password")
            speak("worng password")
            speak("Please tell me the correct passwoed")
        print(f"you have only {chance}")
"""

How to use this porgram 
"
You can face Some module error you find and some location of like(musics,video) is not find
So ,Plese cheak thses error and solve it

"
follow these following step to use this program
Step 1: press the Ctrl+shift+right click
Step 2: open a pope and click open powershall window
step 3: write in powershall window "python myporgram.py"
 
Porgram will be started and it ask the password ("OK")
and you are use this program
After this, it runing all time when your are not say "stop"
It's feature....
You say "give me you intro"
You say "play song"
You say "play video song"
You say "system shutdown"
You say "system restart"
You say "system log off"
You say "what time"
You say "open google"
You say "open youtube"
You say "open vs code"
You say "open c derive"
You say "open f derive"
You say "open e derive"
You say "open notepad++"
You say "open window browers"
And you say anything it  search on google and ask you you want to search on google you say "Yes" if you say "NO"("it is not search on google") show your result

"""