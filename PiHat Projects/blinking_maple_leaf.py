# Install the following library
#pip install pygame

import RPi.GPIO as GPIO
import time
import pygame
from pygame.locals import *

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the pin numbers for the white and red LEDs
WHITE_LED_PIN = 17
RED_LED_PIN = 18

# Setup the GPIO pins as output
GPIO.setup(WHITE_LED_PIN, GPIO.OUT)
GPIO.setup(RED_LED_PIN, GPIO.OUT)

# Initialize Pygame
pygame.init()

# Set up the display
display_width, display_height = 200, 200
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Blinking Maple Leaf")

# Maple Leaf coordinates (x, y)
maple_leaf = [
    (100, 25),
    (125, 75),
    (110, 100),
    (125, 125),
    (100, 110),
    (75, 125),
    (90, 100),
    (75, 75)
]

# Function to draw the maple leaf
def draw_maple_leaf():
    pygame.draw.polygon(display, (255, 0, 0), maple_leaf)

# Function to turn on the red LED
def red_led_on():
    GPIO.output(WHITE_LED_PIN, GPIO.LOW)
    GPIO.output(RED_LED_PIN, GPIO.HIGH)

# Function to turn on the white LED
def white_led_on():
    GPIO.output(RED_LED_PIN, GPIO.LOW)
    GPIO.output(WHITE_LED_PIN, GPIO.HIGH)

try:
    # Loop through the pattern
    for _ in range(5):  # Repeat the pattern 5 times
        white_led_on()
        draw_maple_leaf()
        pygame.display.update()
        time.sleep(1)  # White LED on for 1 second

        red_led_on()
        display.fill((255, 255, 255))  # Clear the display (turns off the maple leaf)
        pygame.display.update()
        time.sleep(1)  # Red LED on for 1 second

finally:
    # Clean up the GPIO settings
    GPIO.cleanup()
    pygame.quit()
