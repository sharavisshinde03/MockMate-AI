import speech_recognition as sr
from pydub import AudioSegment

import uuid
import os

# ---------------- SPEECH TO TEXT ---------------- #

def speech_to_text(audio_path):

    recognizer = sr.Recognizer()

    # BETTER SPEED + ACCURACY

    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1

    wav_path = f"{uuid.uuid4()}.wav"

    try:

        # CONVERT AUDIO

        audio = AudioSegment.from_file(
            audio_path
        )

        # NORMALIZE AUDIO

        audio = audio.set_channels(1)
        audio = audio.set_frame_rate(16000)

        audio.export(
            wav_path,
            format="wav"
        )

        with sr.AudioFile(wav_path) as source:

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio_data = recognizer.record(
                source
            )

        # GOOGLE SPEECH RECOGNITION

        text = recognizer.recognize_google(
            audio_data,
            language="en-US"
        )

        # CLEANUP

        if os.path.exists(wav_path):
            os.remove(wav_path)

        return text.strip()

    except sr.UnknownValueError:

        return "Sorry, I could not understand the audio."

    except sr.RequestError:

        return "Speech service is unavailable."

    except Exception as e:

        print(
            "Speech Recognition Error:",
            e
        )

        return ""

    finally:

        if os.path.exists(wav_path):

            try:
                os.remove(wav_path)
            except:
                pass