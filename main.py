import speech_recognition as sr
from taipy.gui import Gui, notify, navigate, Icon
from pages.dialog import *
import pyaudio
import wave
import os
import assemblyai as aai

recognizer = sr.Recognizer()
audio = pyaudio.PyAudio()
stop_recording = False
page = "New Journal"
text = ""
title = ""
dt = ""
summary = ""
img_path = "images/microphoneImg.png"
journals = [
    {'id': 0, 'date': '2024-01-29',
      'content': 'Woke up early today feeling completely refreshed and ready to embrace the day. I kicked things off with a leisurely stroll in the park, relishing the tranquility of the morning and basking in the beauty of the sunrise. A nutritious breakfast fueled my body and mind, setting a positive tone for my work ahead. I approached my tasks with enthusiasm, excited about the possibilities the day held.', 
      'title': 'A Fresh Start'},
    {'id': 1, 'date': '2024-01-28', 
     'content': 'Spent the day exploring a new book. The story is captivating, and I couldn\'t put it down. Took breaks to sip on some tea and reflect on the characters. A perfect day for some literary escape.. I spent the day immersed in a captivating book, unable to tear myself away from its pages. Each chapter unfolded like a vivid painting, and I took breaks to savor a cup of tea while reflecting on the characters journeys. It was the perfect day for a literary escape, a delightful blend of imagination and relaxation.', 
     'title': 'Dive into a Good Book'},
]
menu_lov = [
    ("My Journals", Icon('images/journalImg1.png', 'My Journals')),
    ("New Journal", Icon('images/journalImg1.png', 'New Journal')),
]

def upload_journal(state):
    date1 = state.dt.strftime('%Y-%m-%d') if state.dt else None
    data = {'id':len(state.journals), 'date':date1, 'content':state.summary, 'title':state.title}
    state.journals.append(data)
    notify(state, "success", "Successfully Saved Your Journal ✨")

def recognize_speech(state):
    with sr.AudioFile("audio/audio_file.wav") as source:
        try:
            audio_data = recognizer.record(source)
            notify(state, "success", "Recording complete. Processing speech... 🔥")
            text = recognizer.recognize_google(audio_data)
            notify(state, "success", "Speech recognized Successfully 🎉")
            state.text += text
        except sr.UnknownValueError:
            notify(state, "error", "Speech Recognition could not understand audio")
        except sr.RequestError as e:
            notify(state, "error", f"Could not request results from Google Speech Recognition service; {e}")

def start_recording_function(state):
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    notify(state, "info", "Listening...")
    frames = []

    try:
        while not state.stop_recording:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file = wave.open("audio/audio_file.wav","wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)

    sound_file.writeframes(b''.join(frames))
    sound_file.close()
    recognize_speech(state)

def stop_recording_function(state):
    state.stop_recording = True

def summarize_journal(state):
    aai.settings.api_key = "YOUR_API_KEY"
    audio_url = "audio/audio_file.wav"

    config = aai.TranscriptionConfig(
      summarization=True,
      summary_model=aai.SummarizationModel.informative,
      summary_type=aai.SummarizationType.bullets
    )

    transcript = aai.Transcriber().transcribe(audio_url, config)

    print(transcript.summary)
    state.summary = transcript.summary
    
    # Deleting the audio from the folder
    try:
        os.remove("audio/audio_file.wav")
        print("Audio file deleted successfully 🗑️")
    except OSError as e:
        print(f"Error deleting audio file: {e}")

def menu_fct(state, var_name, var_value):
    """Function that is called when there is a change in the menu control."""
    state.page = var_value['args'][0]
    navigate(state, state.page.replace(" ", "-"))


root_md = """
<|toggle|theme|>
<|menu|label=Menu|lov={menu_lov}|on_action=menu_fct|>
"""

#Define Pages
pages = {
    "/": root_md + dialog_md,
    "My-Journals": my_journals_md,
    "New-Journal": new_journal_md,
}

if __name__ == "__main__":
    gui = Gui(pages=pages)
    gui.run(title="Blog Your Journal", dark_mode=False, port=8494, debug=True, use_reloader=True)