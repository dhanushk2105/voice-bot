from utils import text2speech
from utils import speech2text

# Convert the text to speech

#text2speech.text2speech("Hello, World!")

while True:
    # Convert the speech to text
    text = speech2text.speech2text()
    if text == "exit":
        break
    text2speech.text2speech(text)