import speech_recognition as r

sr=r.Recognizer()
with r.Microphone() as source:
    print('speech anything:')
    try:
        global audio
        audio = sr.listen(source)

    except Exception as e:
        print(e)

try:

    text=sr.recognize_google(audio)
    print('you said'.format(text))
    f=open("file.txt","w+",encoding='utf-8')
    print('file write')
    f.write(text)
    f.close()


except Exception as e:
    print(e)