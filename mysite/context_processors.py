from django.http import HttpResponse
from mysite.forms import FileUploadForm
from mysite.forms import stt

# 作為渲染html使用

def handle_uploaded_file(f):
    with open('static/audio/audio.wav', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            sttResult = stt.speechTOrecognition('static/audio/audio.wav')
            return {'sttResult': sttResult}            
    else:
        form = FileUploadForm()
    return {'form': form}

def audio_form(request):
    form = FileUploadForm()
    return {'form': form}