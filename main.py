import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

GPIO.output(11, GPIO.LOW)

print("testing flash")

try:
    while 1:
        time.sleep(0.5)
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(11, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
    f = open("temp.txt", "w")
    f.write("printing from python maybe?\n\n\n\n")
    f.close()
    mypath = os.path.dirname(os.path.abspath(__file__))
    myfilepath = mypath + "/temp.txt\""
    myCommand = "lp -d ZJ-58 -o page-bottom=72 \"" + myfilepath
    os.system(myCommand)
