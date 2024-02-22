
# Import pygame module
import pygame

# import internal module
from inputbox.inputbox import InputBox
from players import players
from uiconstants.constants import BLACK

# Initialize pygame
pygame.init()

# Create a display surface object
screen = pygame.display.set_mode((800, 600))

# # Define some colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# Define a font object
font = pygame.font.SysFont("Arial", 32)



# Update the display
pygame.display.flip()

# Create an input box
input_box = InputBox(300, 200, 200, 50, font)

# Create a variable to store the input value
input_value = None

# Create a game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        # If the user clicks the close button, exit the loop
        if event.type == pygame.QUIT:
            running = False
        # Handle the event for the input box
        input_value = input_box.handle_event(event)
        # If the input box returns a value
        if input_value is not None:
            # Print the value and exit the loop
            print(input_value)
            # Call create player module from backend 
            players.create_players(int(input_value))
            # running = False
    # Fill the screen with black
    screen.fill(BLACK)
    # Draw the input box on the screen
    input_box.draw(screen)
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()

