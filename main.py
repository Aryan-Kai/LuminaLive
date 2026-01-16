import sounddevice as sd
from scipy.io.wavfile import write
from SpeechToText import SpeechToText
from TextToSpeech import TextToSpeech

def record_audio(filename,duration=5,samplerate=44100) :
     print("Recording audio.....")
     print("devices:",sd.query_devices())

     audio_data = sd.rec(int(samplerate * duration),samplerate = samplerate,channels=1,dtype="int16")

     sd.wait()
     write(filename,samplerate,audio_data)

     print(f"Recording saved to {filename}")

     o1 = SpeechToText()
     input = o1.transcribe(filename)
     print(f"Transcription:{input}")
     resp = o1.prompt(input)
     print(f"Response from LLM:{resp}")
     o2 = TextToSpeech(resp)
     o2.speak()


if(__name__=="__main__"):
      # record_using_pyaudio()
      record_audio("D:\VoiceRecorder\output.wav",duration=3,samplerate=44100)