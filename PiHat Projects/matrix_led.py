import RPi.GPIO as GPIO
import time
import random
import pygame
from pygame.locals import *

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the pin number for the green LED
GREEN_LED_PIN = 17

# Setup the GPIO pin as output
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

# Initialize Pygame
pygame.init()

# Set up the display
display_width, display_height = 800, 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Matrix LED Simulation")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Function to turn on the green LED
def green_led_on():
    GPIO.output(GREEN_LED_PIN, GPIO.HIGH)

# Function to turn off the green LED
def green_led_off():
    GPIO.output(GREEN_LED_PIN, GPIO.LOW)

try:
    # Loop through the pattern
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                # Exit the program when the window is closed
                GPIO.cleanup()
                pygame.quit()
                quit()

        # Randomly choose the position of the green LED in the display
        led_x = random.randint(0, display_width - 1)
        led_y = random.randint(0, display_height - 1)

        # Turn on the green LED at the chosen position
        green_led_on()

        # Draw the green LED on the display
        display.fill(BLACK)
        pygame.draw.circle(display, GREEN, (led_x, led_y), 3)
        pygame.display.update()

        # Wait for a short time
        time.sleep(0.05)

        # Turn off the green LED
        green_led_off()

        # Update the display to remove the green LED
        display.fill(BLACK)
        pygame.display.update()

        # Wait for a short time before the next iteration
        time.sleep(0.05)

finally:
    # Clean up the GPIO settings
    GPIO.cleanup()
    pygame.quit()
