import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while(1):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(11, GPIO.LOW)
    time.sleep(.5)