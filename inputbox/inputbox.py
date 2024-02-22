import pygame
from uiconstants.constants import WHITE, RED, BLACK

# Define a class to represent an input box
class InputBox:
    def __init__(self, x, y, w, h, font, text=''):
        # Initialize the attributes of the input box
        self.rect = pygame.Rect(x, y, w, h) # The rectangle of the input box
        self.color = WHITE # The color of the input box
        self.text = text # The text of the input box
        self.active = False # The state of the input box
        self.font=font

    def handle_event(self, event):
        # Handle the events related to the input box
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicks on the input box
            if self.rect.collidepoint(event.pos):
                # Toggle the active state
                self.active = not self.active
            else:
                # Set the active state to False
                self.active = False
            # Change the color of the input box
            self.color = RED if self.active else WHITE
        if event.type == pygame.KEYDOWN:
            # If the user presses a key
            if self.active:
                # If the input box is active
                if event.key == pygame.K_RETURN:
                    # If the user presses enter, return the text
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    # If the user presses backspace, delete the last character
                    self.text = self.text[:-1]
                else:
                    # Otherwise, append the key to the text
                    self.text += event.unicode
        # Return None by default
        return None

    def draw(self, screen):
        # Draw the input box on the screen
        pygame.draw.rect(screen, self.color, self.rect) # Draw the rectangle
        text_surface = self.font.render(self.text, True, BLACK) # Render the text
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5)) # Blit the text on the screen
        self.rect.w = max(100, text_surface.get_width() + 10) # Adjust the width of the rectangle
