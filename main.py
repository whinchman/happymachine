import RPi.GPIO as GPIO
import time
import os
import datetime

def flashLED():
    for x in range(0,6):
        time.sleep(0.1)
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(11, GPIO.LOW)

def printMessage(message):
    f = open("temp.txt", "w")
    f.write(message)
    f.close()
    mypath = os.path.dirname(os.path.abspath(__file__))
    myfilepath = mypath + "/temp.txt\""
    myCommand = "lp -d ZJ-58 \"" + myfilepath
    os.system(myCommand)

def my_callback(channel):
    flashLED()
    printMessage("OMG PRINTING WHEN I PRESS A BUTTON. DAMN!!!!!")

print("testing flash & grab input")

try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.IN)

    GPIO.output(11, GPIO.LOW)
    GPIO.add_event_detect(13, GPIO.LOW, callback=my_callback)
    
    message = raw_input('\nPress any key to exit.\n')
 
finally:
    GPIO.cleanup()


