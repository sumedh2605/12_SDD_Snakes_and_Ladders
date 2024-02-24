#Import modules
import pygame
import sys 
import button
import random
import time

#Initialise the module
pygame.init()

#Window
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1020

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game screen")

#Setting window background
backg = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\bg.jpg")

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
label_y = 150
#label_text = "Snakes and Ladders"

# Define a function to draw the label
def draw_board():
  # Draw the label text
  label = font.render("board", True, "White")
  label_rect = label.get_rect()
  label_rect.topleft = (label_x, label_y)
  screen.blit(label, label_rect)

#Draw label
draw_board()

# Define the label position and text
label2_x = 560
label2_y = 70
#label_text = "Snakes and Ladders"

# Define a function to draw the label
def draw_leader():
  # Draw the label text
  label = font.render("leaderboard", True, "White")
  label_rect = label.get_rect()
  label_rect.topleft = (label2_x, label2_y)
  screen.blit(label, label_rect)

#Draw label
draw_leader()

# Fonts
font1 = pygame.font.SysFont("Ariel", 45)
font2 = pygame.font.SysFont("Ariel", 40)

# Function to display players
def players():
    msg1 = font1.render("Player 1", True, (255, 255, 255))
    screen.blit(msg1, [850, 491])
    msg2 = font1.render("Player 2", True, (255, 255, 255))
    screen.blit(msg2, [850, 572])

# Function to display whose turn it is to roll
def display_roll_message(player):
    msg = font2.render(f"{player}'s turn. Click to roll the dice", True, (255, 255, 155))
    screen.blit(msg, [500, 522 if player == 'Player 1' else 599])

# Load start button image
button_img = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\click me.jpg").convert_alpha()
roll_button = button.Button(50, 550, button_img, 0.06)

d1_img = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\dice\\1.jpg").convert_alpha()
d2_img = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\dice\\2.jpg").convert_alpha()
d3_img = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\dice\\3.jpg").convert_alpha()
d4_img = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\dice\\4.jpg").convert_alpha()
d5_img = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\dice\\5.jpg").convert_alpha()
d6_img = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\dice\\6.jpg").convert_alpha()


dice1 = 1
dice2 = 2

if dice1 == 1:
    dice1_button = button.Button(720, 350, d1_img, 0.06)
elif dice1 == 2:
    dice1_button = button.Button(720, 350, d2_img, 0.06)
elif dice1 == 3:
    dice1_button = button.Button(720, 350, d3_img, 0.06)
elif dice1 == 4:
    dice1_button = button.Button(720, 350, d4_img, 0.06)
elif dice1 == 5:
    dice1_button = button.Button(720, 350, d5_img, 0.06)
else:
    dice1_button = button.Button(720, 350, d6_img, 0.06)

if dice2 == 1:
    dice2_button = button.Button(850, 350, d1_img, 0.06)
elif dice2 == 2:
    dice2_button = button.Button(850, 350, d2_img, 0.06)
elif dice2 == 3:
    roll_button3 = button.Button(850, 350, d3_img, 0.06)
elif dice2 == 4:
    roll_button3 = button.Button(850, 350, d4_img, 0.06)
elif dice2 == 5:
    roll_button3 = button.Button(850, 350, d5_img, 0.06)
else:
    roll_button3 = button.Button(850, 350, d6_img, 0.06)
            
# Game loop
running = True
current_player = "Player 1"  # Start with Player 1

while running:
    background()  # Draw background
    players()
    display_roll_message(current_player)
    draw_board()  # Draw board label
    draw_leader()  # Draw leaderboard label

    # Draw dice buttons
    dice1_button.draw(screen)
    dice2_button.draw(screen)

    if roll_button.draw(screen):
        # Roll the dice
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Dice roll: {dice1}, {dice2}")

        # Update dice buttons based on the rolled values
        dice1_button = button.Button(720, 350, eval(f'd{dice1}_img'), 0.06)
        dice2_button = button.Button(850, 350, eval(f'd{dice2}_img'), 0.06)

        # Move player's piece, handle game logic here
        # Here, I'm just printing the dice roll

        if dice1 != 6 and dice2 != 6:
            current_player = "Player 2" if current_player == "Player 1" else "Player 1"
            
    # Event handler
    for event in pygame.event.get():
        # Quit Game
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()

