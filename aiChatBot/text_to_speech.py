import pyttsx3

def main(my_text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 250)
    engine.say(my_text)
    engine.runAndWait()