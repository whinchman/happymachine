import RPi.GPIO as GPIO
import time
import os

def printMessage(message):
    f = open("temp.txt", "w")
    f.write(message)
    f.close()
    mypath = os.path.dirname(os.path.abspath(__file__))
    myfilepath = mypath + "/temp.txt\""
    myCommand = "lp -d ZJ-58 \"" + myfilepath
    os.system(myCommand)

def my_callback(channel):
    if GPIO.input(6) == GPIO.HIGH:
        print('\n LOW at ' + str(datetime.datetime.now()))
    else:
        print('\n HIGH at ' + str(datetime.datetime.now())) 


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.IN)

GPIO.output(11, GPIO.LOW)
GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)

print("testing flash & grab input")

try:
    while 1:
        time.sleep(0.2)
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(11, GPIO.LOW)
        
except KeyboardInterrupt:
    GPIO.cleanup()


