import whisper
from ollama import chat
from ollama import ChatResponse

class SpeechToText:
    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self,inputAudio):
        print("Input audio file:",inputAudio)
        try:
            self.result = self.model.transcribe(inputAudio)
            inputText  = self.result['text']
            return inputText
        except Exception as e:   
             print("exception:",e)
        
        
    def prompt(self,input):
        response:ChatResponse = chat(model="gemma3:270m",messages=[
            {
                'role':'user',
                'content':input
            }
        ])
        print(response['message']['content'])
        return response['message']['content']