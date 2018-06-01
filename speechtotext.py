import speech_recognition
import ffmpy

ff = ffmpy.FFmpeg(
    inputs={'seg.wav': None},
    outputs={'output.wav': None})
ff.run()


input_file = 'output.wav'
r = speech_recognition.Recognizer()
with speech_recognition.AudioFile(input_file) as source:
    audio = r.record(source)
sttResult = r.recognize_google(audio,language='zh-tw')
print (sttResult) 




    # file_path = './audiovoice.m4a'

    # with open(file_path, 'wb') as fd:
    #     for chunk in message_content.iter_content():
    #         fd.write(chunk)

    # ff = ffmpy.FFmpeg(
    #     inputs={'audiovoice.m4a': None},
    #     outputs={'output.wav': None})
    # ff.run()

    # r = sr.Recognizer()
    # audio = 'output.wav'

    # with sr.AudioFile(audio) as source:
    #     audio = r.record(source)

    # try:
    #     speech_text = r.recognize_google(audio,language = 'zh-TW')
