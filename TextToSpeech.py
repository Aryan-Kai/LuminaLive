import pyttsx3


class TextToSpeech:
     
     def __init__(self,inputText):
         self.engine = pyttsx3.init()
         self.engine.setProperty('rate',170)
         self.engine.say(inputText)
         print("Text to Speech initialized.")

     def speak(self):
           print("Speaking now.")
           self.engine.runAndWait()

# o1 = TextToSpeech("Hello, this is a text to speech test.")
# o1.speak()