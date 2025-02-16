import sounddevice as sd
import numpy as np
import speech_recognition as sr
from scipy.io.wavfile import write

def record_audio(filename="output.wav", duration=5, fs=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    write(filename, fs, audio_data)  # Save as WAV file
    print("Recording complete.")

def recognize_speech(filename="output.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Could not request results, check your internet connection.")

if __name__ == "__main__":
    record_audio()
    recognize_speech()
