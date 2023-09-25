import speech_recognition as sr
import webbrowser

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source)  
    audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        text = text.lower()

        # Open websites based on recognized speech
        if "open youtube" in text:
            webbrowser.open("https://www.youtube.com")
        elif "open chatgpt" in text:
            webbrowser.open("https://www.chatgpt.com")
        elif "open google" in text:
            webbrowser.open("https://www.google.com")
        elif "open game" in text:
            webbrowser.open("https://smashkarts.io/")
        else:
            print("Command not recognized.")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
