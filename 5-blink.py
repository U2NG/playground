
# Import Libraries
import os
import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set pin 25 as an input pin
ButtonPin = 25
GPIO.setup(ButtonPin, GPIO.IN) 

print("------------------")
print( "Button + GPIO")
print("------------------")
print(GPIO.input(ButtonPin))

# The commands indented after this 'while' will be repeated
# forever of until 'Ctrl + c' is pressed.
while True:
	# If the button is pressed, ButtonPin will be 'false'
	if GPIO.input(ButtonPin) == False:
		print("Button Pressed")
		print(GPIO.input(ButtonPin))
		time.sleep(1) # sleep for 1 second
	else:
		os.system('clear') # Clears the screen
		print("Waiting for you to press a button")
	time.sleep(0.5) # Sleep for 0.5 seconds
