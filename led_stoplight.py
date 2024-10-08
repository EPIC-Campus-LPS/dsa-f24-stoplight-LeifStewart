import RPi.GPIO as GPIO 


import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup([23,24,25], GPIO.OUT)
while True:
	GPIO.output(23, GPIO.HIGH)
	time.sleep(5)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(25, GPIO.HIGH)
	time.sleep(4)
	GPIO.output(25, GPIO.LOW)
