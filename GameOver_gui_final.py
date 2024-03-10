#Import modules
import pygame
import sys 
import button

#Initialise the module
pygame.init()

#Window
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game Over")

#Setting window background
background_image = pygame.image.load("bg.jpg")

#Defining dimenstions of background image
bx = 0
by = 0

#Defining background
def background(background_image):
    size = pygame.transform.scale(background_image,(1200,800))
    screen.blit(size,(0,0))

#Calling backgroung image
background(background_image)

# Define the font for the label
font = pygame.font.SysFont("Ariel", 200)

# Define the label position and text
label_x = 170
label_y = 300
#label_text = "Snakes and Ladders"

# Define a function to draw the label
def draw_label():
  # Draw the label text
  size = pygame.transform.scale(background_image,(1200,800))
  screen.blit(size,(0,0))
  label = font.render("GAME OVER", True, "White")
  label_rect = label.get_rect()
  label_rect.topleft = (label_x, label_y)
  screen.blit(label, label_rect)

#Draw label
draw_label()

#Game loop
run = True 

while run:

    #Event handler
    for event in pygame.event.get():
        #Quit Game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()


