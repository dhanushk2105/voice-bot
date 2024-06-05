#python funtiàon to convert speech to text

import speech_recognition as sr

def speech2text() -> str:
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture the audio
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    # Convert speech to text
    try:
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")
        return text
    except Exception as e:
        print(f"Error: {e}")
        return ""
    
