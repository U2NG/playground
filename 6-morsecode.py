def hello():
    print("Hello World!")
hello()

# Import Libraries
import os
import time
import RPi.GPIO as GPIO

# Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PINBuzzer = 22 # sets teh buzzer pin 22

# Sets PINBuzzer as an output pin and initialize it to 'off'
GPIO.setup(PINBuzzer, GPIO.OUT)
GPIO.output(PINBuzzer, GPIO.LOW)

# Define some 'user-defined functions'
def dot(): # a single morse dot
    GPIO.output(PINBuzzer, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(PINBuzzer, GPIO.LOW)
    time.sleep(0.1)

def dash(): # a single morse dash
