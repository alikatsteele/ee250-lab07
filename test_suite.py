import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

GPIO.setup(17, GPIO.OUT)

while(1):
    for i in range(5):
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.5)
        counter = 0
    while counter < 50:
        light = mcp.read_adc(0)
        print(light)
        if (light < 150):
            print("dark")
        else:
            print("light")
        time.sleep(0.1)
        counter = counter+1
    for i in range(4):
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.2)
        counter = 0
        turn_off = 0
    while counter < 50:
        sound = mcp.read_adc(1)
        print(sound)
        if turn_off == 1:
            GPIO.output(17, GPIO.LOW)
            turn_off = 0
        if (sound > 600):
            GPIO.output(17, GPIO.HIGH)
            turn_off = 1
        time.sleep(0.1)
        counter = counter+1