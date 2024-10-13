import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 17 as an output
LED_PIN =5
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

finally:
    # Clean up the GPIO settings
    GPIO.cleanup()