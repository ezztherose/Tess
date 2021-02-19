import speech_recognition as sr
import pyttsx3

lisening = sr.Recognizer()

try:
    with sr.Microphone() as src:
        print('lisening...')
        voice = lisening.listen(src)
        com = lisening.recognize_google(voice)
        print(com)
except:
    print('exception')