
# Imports the Google Cloud client library
import os
import io
import pyaudio
import wave
from google.cloud import speech, language_v1


""" Listen to input audio and save as recording """

# Get credentials
credential_path = os.path.join(os.path.dirname(__file__), './','deltahacks-306803-01a16b6b0a26.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Set up for Recording
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 5
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

""" Use Google Cloud Speech To Text API to convert audio to text """

# Instantiates a client
client = speech.SpeechClient()

# Open audio recording
speech_file = os.path.join(os.path.dirname(__file__), './','output.wav')
with io.open(speech_file, "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=fs,
    language_code="en-US",
    audio_channel_count=2,
)

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)
text = "Error: Did not work"

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
    text = result.alternatives[0].transcript

# Instantiates a client
langClient = language_v1.LanguageServiceClient()
encoding_type = language_v1.EncodingType.UTF8

# The text to analyze
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
# sentiment = langClient.analyze_sentiment(request={'document': document}).document_sentiment

entities = langClient.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
print(entities)

for entity in entities.entities:
    print('Representative name for the entity: {}'.format(entity.name))
    print("Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))
    print("Salience score: {}".format(entity.salience))

    for metadata_name, metadata_value in entity.metadata.items():
        print(u"{}: {}".format(metadata_name, metadata_value))

    for mention in entity.mentions:
        print(u"Mention text: {}".format(mention.text.content))

        # Get the mention type, e.g. PROPER for proper noun
        print(
            u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)
        )

# print("Text: {}".format(text))
# print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))