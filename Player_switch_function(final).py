#Inporting modules
import pygame
import sys
import button
import random

#Initialising pygame
pygame.init()

# Window
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snakes and Ladders")
screen.fill((255, 255, 255))

# Fonts
font1 = pygame.font.SysFont("Calibri", 25)
font2 = pygame.font.SysFont("Calibri", 20)

# Function to display players
def players():
    msg1 = font1.render("Player 1", True, (255, 0, 0))
    screen.blit(msg1, [25, 251])
    msg2 = font1.render("Player 2", True, (0, 0, 255))
    screen.blit(msg2, [25, 362])

# Function to display whose turn it is to roll
def display_roll_message(player):
    msg = font2.render(f"{player}'s turn. Click to roll the dice.", True, (0, 0, 0))
    screen.blit(msg, [35, 290 if player == 'Player 1' else 400])

# Load start button image
button_img = pygame.image.load("click me.jpg").convert_alpha()
start_button = button.Button(300, 500, button_img, 0.8)

# Game loop
running = True
current_player = "Player 1"  # Start with Player 1

while running:
    screen.fill((255, 255, 255))
    players()
    display_roll_message(current_player)

    if start_button.draw(screen):
        # Roll the dice
        dice = random.randint(1, 12)
        print(f"Dice roll: {dice}")

        # Move player's piece, handle game logic here
        # Here, I'm just printing the dice roll
        
        if dice != 12:
            current_player = "Player 2" if current_player == "Player 1" else "Player 1"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()


