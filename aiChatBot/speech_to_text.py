import speech_recognition as sr


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)

        print(r.recognize_google(audio))
        return r.recognize_google(audio)
            


if __name__ == "__main__":
    
    main()

