import RPi.GPIO as gpio
import time

# H-Bridge info ****************************
# pi GPIO pin numbers are used
en1 = 16 
en2 = 12

pwr1_1 = 1 
pwr1_2 = 7
pwr2_1 = 8
pwr2_2 = 25

gpio.setwarnings(False)

# initializing GPIO pins
gpio.setmode(gpio.BCM)

gpio.setup(en1, gpio.OUT)
gpio.setup(en2, gpio.OUT)

gpio.setup(pwr1_1, gpio.OUT)
gpio.setup(pwr1_2, gpio.OUT)
gpio.setup(pwr2_1, gpio.OUT)
gpio.setup(pwr2_2, gpio.OUT)

gpio.output(en1, False)
gpio.output(en2, False)

gpio.output(pwr1_1, False)
gpio.output(pwr1_2, True)
gpio.output(pwr2_1, False)
gpio.output(pwr2_2, True)

print("Start")
gpio.output(en1, True)
time.sleep(100)

print("mid")
gpio.output(en1, False)
gpio.output(en2, True)
time.sleep(1)

gpio.output(en2, False)

print("stop")
