#github link: https://github.com/alikatsteele/ee250-lab07.git
#team members: Alice Steele and James Li

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #set GPIO layout to BCM

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

GPIO.setup(17, GPIO.OUT) #configures LED as output

while(1):
    for i in range(5): #repeat 5 times
        GPIO.output(17, GPIO.HIGH) #turn LED on
        time.sleep(0.5) #wait .5 seconds
        GPIO.output(17, GPIO.LOW) #turn LED off
        time.sleep(0.5) #wait .5 seconds
        counter = 0 #reset counter
    while counter < 50: #repeat 50 times
        light = mcp.read_adc(0) #read light sensor
        print(light) #print light sensor value
        if (light < 150): #if sensor value less than this determined threshold print dark, otherwise print light
            print("dark") 
        else:
            print("light")
        time.sleep(0.1) #wait 100 milliseconds
        counter = counter+1 #update counter
    for i in range(4): #repeat 4 times, turn LED on for 200 milliseconds, turn LED off for 200 milliseconds
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.2)
        counter = 0 #reset counter
        turn_off = 0 #reset this flag
    while counter < 50: #repeat 50 times
        sound = mcp.read_adc(1) #read sound sensor
        print(sound) #print out sensor value
        if turn_off == 1: #if flagged, turn off the LED
            GPIO.output(17, GPIO.LOW)
            turn_off = 0
        if (sound > 500): #if sensor reads a value above this threshold, turn the LED on
            GPIO.output(17, GPIO.HIGH)
            turn_off = 1
        time.sleep(0.1) #wait 100 milliseconds
        counter = counter+1 #update counter
