from gtts import gTTS
import pygame
import io

def text2speech(text: str, language: str = 'en') -> None:
    # Creating the gTTS object
    speech = gTTS(text=text, lang=language, slow=False)

    # Save the speech audio to a BytesIO object
    speech_fp = io.BytesIO()
    speech.write_to_fp(speech_fp)
    speech_fp.seek(0)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the speech audio from the BytesIO object
    pygame.mixer.music.load(speech_fp, 'mp3')

    # Play the audio
    pygame.mixer.music.play()

    # Keep the script running until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

