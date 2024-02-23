#Import modules
import pygame
import sys 
import button

#Initialise the module
pygame.init()

#Window
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Player Input")

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
label_x = 90
label_y = 200
#label_text = "Snakes and Ladders"

# Define a function to draw the label
def draw_label():
  # Draw the label text
  label = font.render("Select number of players", True, "White")
  label_rect = label.get_rect()
  label_rect.topleft = (label_x, label_y)
  screen.blit(label, label_rect)

#Draw label
draw_label()

#Load button images
two_img = pygame.image.load("C:\\Users\\mahes\Desktop\\Project\\twop.jpg").convert_alpha()
three_img = pygame.image.load("C:\\Users\\mahes\Desktop\\Project\\threep.jpg").convert_alpha()
four_img = pygame.image.load("C:\\Users\\mahes\Desktop\\Project\\fourp.jpg").convert_alpha()

    
#create button instance
two_button = button.Button(150, 400, two_img,0.8)
three_button = button.Button(410, 400, three_img,0.8)
four_button = button.Button(670, 400, four_img, 0.8)

#Game Loop
run = True 
while run:

    if two_button.draw(screen):
        print("[Player01, Player02]")
    if three_button.draw(screen):
        print("[Player01, Player02, Player03]")
    if four_button.draw(screen):
        print("[Player01, Player02, Player03, Player04]")

    #Event handler
    for event in pygame.event.get():
        #Quit Game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()