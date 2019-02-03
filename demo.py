import serial
ser=serial.Serial("com4",9600);
while True:
    print(ser.readline())
    
