
import speech_recognition as sr
r=sr.Recognizer()

with sr.Microphone() as source:
    print("say something");
    audio=r.listen(source)
    print("over")

try:
    speech=r.recognize_google(audio)
    print(speech)
    ser.write(speech[0])

except:
    pass;
