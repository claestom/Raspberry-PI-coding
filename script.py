import subprocess
import sys

# Ensure the RPi.GPIO library is installed
subprocess.check_call([sys.executable, "-m", "pip", "install", "RPi.GPIO"])

import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 17 as an output
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    # Turn on the LED
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED is on")
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Turn off the LED
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED is off")