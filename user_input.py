#Load Libraries
import os
import time
import RPi.GPIO as GPIO

#Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)

#Supress warnings
GPIO.setwarnings(False)

#setup variables to store the pin numbers
LEDRed = 18
LEDYellow = 24
LEDGreen = 23

#set the LED pins to output
GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(LEDYellow, GPIO.OUT)
GPIO.setup(LEDGreen, GPIO.OUT)

#clears the screen
os.system('clear')



print("Which LED would you like to blink")
print("1: Red?")
print("2: Green?")
print("3: Yellow?")

#User input
led_choice = input("Choose your option: ")
count = input("How many times would you like it to blink?: ")

led_choice = int(led_choice)
count = int(count)

#set the LEDchoice variable depending on the LED Choice
if led_choice == 1:
    print("You picked the Red LED")
    LEDChoice = LEDRed
if led_choice == 2:
    print("You picked the Green LED")
    LEDChoice = LEDGreen
if led_choice == 3:
    print("You picked the Yellow LED")
    LEDChoice = LEDYellow

# If we have chosen a valid choice, flash LED
if LEDChoice>0:
    while count > 0:
        GPIO.output(LEDChoice, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LEDChoice, GPIO.LOW)
        time.sleep(1)
        count = count -1

GPIO.cleanup()


    
