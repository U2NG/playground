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
    GPIO.output(PINBuzzer, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(PINBuzzer, GPIO.LOW)
    time.sleep(0.1)

def letterSpace(): #The spave between letters
    time.sleep(0.2)

def wordSpace(): # the space between words
    time.sleep(0.6)

def morseS(): # the morese for S, ...
    dot()
    dot()
    dot()

def morseO(): # the morese for o, ---
    dash()
    dash()
    dash()

os.system('clear') # Clears the screen

print("Morese Code")

#prompt
loop_count = input("How many times would you like SOS to loop?: ")
loop_count = int(loop_count) # Convert text input into an integer

while loop_count > 0: # loop around the chosen number of times
    loop_count = loop_count - 1
    morseS()
    letterSpace()
    morseO()
    letterSpace()
    morseS()
    wordSpace()

GPIO.cleanup()


    
