import RPi.GPIO as GPIO
import time
import os
import datetime
import json
import random

# LED defines
YELLOW_LED = 11
GREEN_LED = 15
BLUE_LED = 18
RED_LED = 21

#button defines
YELLOW_BUTTON = 16
GREEN_BUTTON = 13
BLUE_BUTTON = 19
RED_BUTTON = 22

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

jokes = parsedData["jokes"]
fortunes = parsedData["fortunes"]
obliques = parsedData["obliques"]

def flashLED(pin):
    for x in range(0,6):
        time.sleep(0.1)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(pin, GPIO.LOW)

def printMessage(message):
    f = open("temp.txt", "w")
    f.write(message)
    f.close()
    mypath = os.path.dirname(os.path.abspath(__file__))
    myfilepath = mypath + "/temp.txt\""
    myCommand = "lp -d ZJ-58 \"" + myfilepath
    os.system(myCommand)

def yellow_button(channel):
    randIndex = random.randint(0,len(jokes)-1)
    printMessage(jokes[randIndex])
    flashLED(YELLOW_LED)

def green_button(channel):
    randIndex = random.randint(0,len(fortunes)-1)
    printMessage(fortunes[randIndex])
    flashLED(GREEN_LED)

def blue_button(channel):
    randIndex = random.randint(0,len(obliques)-1)
    printMessage(obliques[randIndex])
    flashLED(BLUE_LED)

def red_button(channel):
    printMessage("RED BUTTON")
    flashLED(RED_LED)

print("setting up GPIO")

try:
    # use the board count pinout. 
    GPIO.setmode(GPIO.BOARD)

    # setup output pins
    GPIO.setup(YELLOW_LED, GPIO.OUT)
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(BLUE_LED, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)

    #turn on all LEDS (low grounds out the 5v channel)
    GPIO.output(YELLOW_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(BLUE_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.LOW)


    # setup input pins
    GPIO.setup(YELLOW_BUTTON, GPIO.IN)
    GPIO.setup(GREEN_BUTTON, GPIO.IN)
    GPIO.setup(BLUE_BUTTON , GPIO.IN)
    GPIO.setup(RED_BUTTON , GPIO.IN)

    # set callbacks
    GPIO.add_event_detect(GREEN_BUTTON, GPIO.FALLING, callback=yellow_button, bouncetime=3000)
    GPIO.add_event_detect(YELLOW_BUTTON, GPIO.FALLING, callback=green_button, bouncetime=3000)
    GPIO.add_event_detect(BLUE_BUTTON, GPIO.FALLING, callback=blue_button, bouncetime=3000)
    GPIO.add_event_detect(RED_BUTTON, GPIO.FALLING, callback=red_button, bouncetime=3000)

    # RUN LOOP
    message = raw_input('\nPress any key to exit.\n')

except:
    print("GPIO FAILURE")

finally:
    GPIO.cleanup()


