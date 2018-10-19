import RPi.GPIO as GPIO
import time
import os
import datetime
import json
import random

random.seed()

try:
    with open('./resources/text.json', 'r') as myfile:
        data=myfile.read()
    print(json.dumps(data))
except:
    print("Error Opening and Parsing Data File")

try:
    parsedData = json.loads(data)
except:
    print("failed to parse data to JSON")

messages = parsedData["jokes"]

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
    randIndex = random.randint(0,len(messages)-1)
    printMessage(messages[randIndex])

def green_button(channel):
    for x in range(0,6):
        time.sleep(0.1)
        GPIO.output(15, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(15, GPIO.LOW)

print("testing flash & grab input")



try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.IN)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.IN)

    GPIO.output(11, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.add_event_detect(13, GPIO.FALLING, callback=my_callback, bouncetime=1000)
    GPIO.add_event_detect(16, GPIO.FALLING, callback=green_button, bouncetime=1000)
    
    message = raw_input('\nPress any key to exit.\n')

except:
    print("somethings gone wrong")

finally:
    GPIO.cleanup()


