from django.forms import forms
import speech_recognition


class FileUploadForm(forms.Form):
    file = forms.FileField()


class stt:
    def speechTOrecognition (input_file):
        r = speech_recognition.Recognizer()
        with speech_recognition.AudioFile(input_file) as source:
            audio = r.record(source)
        sttResult = r.recognize_google(audio,language='zh-tw')
        return sttResult


