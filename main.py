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
    f.write("printing from python maybe?")
    os.system("lp -d ZJ-58 test.txt")
