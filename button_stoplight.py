import RPi.GPIO as GPIO 
import time
from gpiozero import Button
from signal import pause

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup([23,16,24], GPIO.OUT)
GPIO.setup(6, GPIO.IN)

while True:
    pin6 = GPIO.input(6)
    if pin6 == 0:
        GPIO.output(23, GPIO.HIGH)
        time.sleep(4)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(4)
        GPIO.output(24, GPIO.LOW)
    elif pin6 == 1:
        GPIO.output(23,GPIO.LOW)
        GPIO.output(24,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
    