#Import modules
import pygame
import sys 
import button

#Initialise the module
pygame.init()

#Window
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1020

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Snakes and Ladders")

#Setting window background
backg = pygame.image.load("bg.jpg")

#Defining dimenstions of background image
bx = 0
by = 0

#Defining background
def background():
    screen.blit(backg,(bx,by))

#Calling backgroung image
background()

# Define the font for the label
font = pygame.font.SysFont("Ariel", 100)

# Define the label position and text
label_x = 180
label_y = 200
#label_text = "Snakes and Ladders"

# Define a function to draw the label
def draw_label():
  # Draw the label text
  label = font.render("Snakes and Ladders", True, "White")
  label_rect = label.get_rect()
  label_rect.topleft = (label_x, label_y)
  screen.blit(label, label_rect)

#Draw label
draw_label()

#Load button images
start_img = pygame.image.load("start.jpg").convert_alpha()
exit_img = pygame.image.load("exit.jpg").convert_alpha()
    
#create button instance
start_button = button.Button(250, 400, start_img,0.8)
exit_button = button.Button(600, 400, exit_img,0.8)

#Game Loop
run = True 
while run:

    if start_button.draw(screen):
        print("Start")
    if exit_button.draw(screen):
        run = False

    #Event handler
    for event in pygame.event.get():
        #Quit Game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()