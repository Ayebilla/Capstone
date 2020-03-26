import serial
import pynmea2
ser = serial.Serial('/dev/ttyAMA0',9600)
while 1:
     data = ser.readline()
     if (data.startswith("$GPGGA")):
         msg = pynmea2.parse(data)
         print repr(msg)
