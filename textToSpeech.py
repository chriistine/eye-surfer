from google.cloud import texttospeech
import os
import pygame

def textToSpeech(text: str):

    # Get credentials
    credential_path = os.path.join(os.path.dirname(__file__), './','deltahacks-306803-01a16b6b0a26.json')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    print(text)
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        # os.startfile('output.mp3')
        print('Audio content written to file "output.mp3"')
        
    try:        
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    except KeyboardInterrupt:
        print("Interrupted by User")
        pygame.mixer.music.stop()
    
    pygame.mixer.quit()
    out.close()
    os.remove('output.mp3')
