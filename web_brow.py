import serial
import time
import webbrowser
ser = serial.Serial('COM4', 9600)
while (1):
    print (ser.readline()[0:-2])
    time.sleep(0.1)
    if ser.readline()[0:-2]==b'y':
        webbrowser.open("https://www.youtube.com")
    elif ser.readline()[0:-2]==b'g':
        webbrowser.open("https://www.google.com")
    else:
        print("\n not site selected")
        
#webbrowser.open("https://www.youtube.com")
