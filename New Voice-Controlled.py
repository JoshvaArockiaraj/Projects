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

        # Check if the recognized speech contains "open" and a URL
        if "open" in text:
            # Extract the URL from the recognized speech
            url = text.split("open", 1)[1].strip()
            webbrowser.open(url)
        else:
            print("Command not recognized.")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
