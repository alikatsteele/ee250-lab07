import RPi.GPIO as GPIO
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 23
MISO = 21
MOSI = 19
CS   = 24
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while(1):
    for i in range(5):
        GPIO.output(11, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(11, GPIO.LOW)
        time.sleep(.5)
        counter = 0
    while counter < 5:
        light = mcp.read_adc(0)
        print(light)
        if (light < 2):
            print("dark")
        else:
            print("light")