def hello():
    print("Hello World!")
hello()

# Import Libraries
import os
import time
import RPi.GPIO as GPIO

# Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM) #set the GPIO pin naming mode
GPIO.setwarnings(False) # supress warnings
PINBuzzer = 26 # sets the buzzer pin 26


ButtonPin = 25 # Set pin 25 as an input pin
GPIO.setup(ButtonPin, GPIO.IN) 


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

def letterSpace(): #The space between letters
    time.sleep(0.2)

def wordSpace(): # the space between words
    time.sleep(0.6)

def morseS(): # the morse for S, ...
    dot()
    dot()
    dot()

def morseO(): # the morse for o, ---
    dash()
    dash()
    dash()

os.system('clear') # Clears the screen

# print("Morse Code")
print("------------------")
print( "Button + GPIO + Morse code")
print("------------------")
print(GPIO.input(ButtonPin))

# If the button is pressed, ButtonPin will be FALSE
while True:
	# If the button is pressed, ButtonPin will be 'false'
    if GPIO.input(ButtonPin) == False:
            print("Sending SOS")
            print(GPIO.input(ButtonPin))
            morseS()
            letterSpace()
            morseO()
            letterSpace()
            morseS()
            wordSpace()
            time.sleep(2) # sleep for 2 seconds
    else:
	    os.system('clear') # Clears the screen
	    print("Waiting for you to send an SOS")
    time.sleep(0.5) # Sleep for 0.5 seconds


#prompt
#loop_count = input("How many times would you like SOS to loop?: ")
#loop_count = int(loop_count) # Convert text input into an integer

#while loop_count > 0: # loop around the chosen number of times
#    loop_count = loop_count - 1
#    morseS()
#    letterSpace()
#    morseO()
#    letterSpace()
#    morseS()
#    wordSpace()

#GPIO.cleanup()


    
