'''
This is a Very Simple Python Script to drive the EarthLCD XLK-10x1-USB  SmartLCD
It is based on a simple ARM9 Microcontroller which simply sends a frame from USB to the LCD display
one screen at a time. The entire screen must be written each time with this controller. EarthLCD has other 
solutions to drive this LCD under development. This is meant to be a demonstration platform for prototyping 
and small qty production. It is based on the EarthLCD-10.4-1024100 TFT LCD, a 10.4" 1024 X 100  Pixel Display.
What it does is read 16 bit bmp files in order 0001.bmp 0002.bmp ect .
And send them to the display .
ken@earthlcd.com
'''
import serial
#from serial.tools import list_ports
import io
import sys
import os
import time
import re
 
comPorts = []
units = []
x = 0 
ser = 0
 
ser1 = serial.Serial()
ser1.baudrate = 115200 
 
# Set comport here Windows COM?? 
ser1.port = '/dev/ttyACM0' 
print ser1.port
ser1.timeout = 5
ser1.open()
 
# edit image path here ..
imagesFileNames1 = os.listdir('/home/pi/KeyView/Unint1/') 
sorted_files1 = sorted(imagesFileNames1, key=lambda x: int(x.split('.')[3]) if (x.endswith("py ")) else x)
for x in range(0, len(sorted_files1)):
    print sorted_files1[x]
 
bmp1 = open('/home/pi/KeyView/Unint1/' + sorted_files1[0], 'rb')
Data1 = bmp1.read()
 
i1 = 0
 
 
delay2 = 0
while(True):
    bmp1 = open('/home/pi/KeyView/Unint1/' + sorted_files1[i1], 'rb')
    Data1 = bmp1.read()
    bmp1.close()
    ser1.write(Data1)
    time.sleep(.05)  # change this for the time between files
    i1 += 1
    if i1 == len(sorted_files1):
        i1 = 0
ser.close()
