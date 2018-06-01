from django.forms import forms
import speech_recognition, ffmpy, os


class FileUploadForm(forms.Form):
    file = forms.FileField()


class stt:
    def speechTOrecognition (input_file):
        
        ff = ffmpy.FFmpeg(
            inputs = { input_file : None },
            outputs = {'output.wav' : None }
            )
        ff.run()

        input_file = 'output.wav'

        r = speech_recognition.Recognizer()
        with speech_recognition.AudioFile(input_file) as source:
            audio = r.record(source)
        sttResult = r.recognize_google(audio,language='zh-tw')
        os.remove('output.wav')
        return sttResult
        


