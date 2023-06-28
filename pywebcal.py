import pywhatkit as pw
import pyttsx3 as ptt
import wikipedia
import webbrowser as wb
import platform

def add(*args):
        a = 0
        for i in args:
            a += i
        return a

def say(audio):
        engine = ptt.init()
        engine.say(audio)
        engine.runAndWait()

def squ(number,power):
        a = number
        t = power
        print(a**t)

def mul(*args):
        a = 1
        for i in args:
            a *= i
        return a

def sub(*args):
    a = 0
    for i in args:
        a -= i
    return a

def div(a=1,b=1,decimal = True,round_off = False):
        dif = float(a/b)
        dii = int(a/b)
        if decimal == True:
           print(dif)
        elif round_off == True:
           print(dii)

def rem(a=1,b=1):
        r = int(a%b)
        print(r)

def takcmd(userin = False):
                import speech_recognition as sr
                r = sr.Recognizer()
                with sr.Microphone() as source:
                        print("listening...")
                        r.pause_threshold = 1
                        audio = r.listen(source)
                try:
                        print("recognizing...")
                        query = r.recognize_google(audio, language='en-in')
                        if userin == True:
                            print(query)
                except Exception as e:
                        # print(e)
                        # print('say that again please...')
                        return "None"
                return query

def youtube(search):
        pw.playonyt(search)

def google(search, search1 = None):

        if search1 == None:
            wb.open(f'https://www.google.com/search?q={search}')
        else:
            wb.open(f'https://www.google.com/search?q={search}')
            wb.open(f'https://www.google.com/search?q={search1}')

def wiki(wsearch,presult = False, no_of_sen=2):
        wsearch.replace("wikipedia", "")
        if presult == True:
                results = wikipedia.summary(wsearch, sentences=no_of_sen)
                print(results)

        else:
                wb.open(f'https://en.wikipedia.org/wiki/{wsearch}')
def bing(search=None, search2 = None):
    wb.open(f'https://www.bing.com/search?q={search}')
    if search2 == None:
        pass
    else:
        wb.open(f'https://www.bing.com/search?q={search}')
        wb.open(f'https://www.bing.com/search?q={search2}')


def flipkart(search):
    wb.open(f'https://www.flipkart.com/search?q={search}')

def amazon(search):
    wb.open(f'https://www.amazon.in/s?k={search}')

def sqroot(number,upto=100):
    for i in range(1,upto):
        if number/i == i:
            print(i)
        else:
            pass

def factors(number,upto=100):
    a= []
    for i in range(1,upto):
        if (number%i) == 0 :
            a.append(i)

        else:
            pass
    print(a)

class whatsmsg():
   def whats_personal(number=str,message=str,hour=int,min=int):
        pw.sendwhats_image(number,message,hour,min)

   def whats_personal_instantly(number=str,message=str):
       pw.sendwhatmsg_instantly(number,message)

   def whats_img(name=str,image_path=str,comment_img=''):
       pw.sendwhats_image(name,image_path,comment_img)

   def whats_group(group_name= str,message=str,hour=int,min=int):
      pw.sendwhatmsg_to_group(group_name,message,hour,min)

   def whats_group_instantly(group_name= str,message=str):
      pw.sendwhatmsg_to_group_instantly(group_name,message)


def face_search(search=str):
    wb.open(f'https://www.facebook.com/search/top/?q={search}')

def map_search(search=str):
    wb.open(f'https://www.google.com/maps/place/{search}')
def describe(object):
        import pandas as pd
        sc = pd.Series(object)
        desc = sc.describe()
        return desc


