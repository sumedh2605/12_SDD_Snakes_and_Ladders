import pygame
import sys 
import button
import random
import time

# Initialize Pygame
pygame.init()

# Set up the window
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1020
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game screen")

# Load background image
background_image = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\bg.jpg")
background_rect = background_image.get_rect()

# Define the font for the label
font = pygame.font.SysFont("Ariel", 100)

# Define label positions
label_x = 90
label_y = 150
label2_x = 560
label2_y = 70

# Define functions to draw labels
def draw_board():
    label = font.render("board", True, "White")
    screen.blit(label, (label_x, label_y))

def draw_leader():
    label = font.render("leaderboard", True, "White")
    screen.blit(label, (label2_x, label2_y))

# Fonts
font1 = pygame.font.SysFont("Ariel", 45)
font2 = pygame.font.SysFont("Ariel", 40)

# Function to display players
def display_players():
    player1_msg = font1.render("Player 1", True, (255, 255, 255))
    player2_msg = font1.render("Player 2", True, (255, 255, 255))
    screen.blit(player1_msg, (850, 491))
    screen.blit(player2_msg, (850, 572))

# Function to display whose turn it is to roll
def display_roll_message(player):
    msg = font2.render(f"{player}'s turn. Click to roll the dice", True, (255, 255, 155))
    y_position = 522 if player == 'Player 1' else 599
    screen.blit(msg, (500, y_position))

# Load start button image
button_img = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\click me.jpg").convert_alpha()
roll_button = button.Button(50, 550, button_img, 0.06)

# Load dice images
dice_images = [pygame.image.load(f"C:\\Users\\mahes\\Desktop\\Project\\dice\\{i}.jpg").convert_alpha() for i in range(1, 7)]

# Game loop
clock = pygame.time.Clock()
running = True
current_player = "Player 1"  # Start with Player 1

while running:
    screen.blit(background_image, background_rect)  # Draw background
    display_players()
    display_roll_message(current_player)
    draw_board()  # Draw board label
    draw_leader()  # Draw leaderboard label

    # Draw buttons
    roll_button.draw(screen)

    if 'dice1_button' in locals():
        dice1_button.draw(screen)
    if 'dice2_button' in locals():
        dice2_button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if roll_button.rect.collidepoint(event.pos):
                # Roll the dice
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                print(f"Dice roll: {dice1}, {dice2}")

                # Update dice buttons based on the rolled values
                for i in range(6):
                    dice1_button = button.Button(720, 350, dice_images[i], 0.06)
                    dice2_button = button.Button(850, 350, dice_images[i], 0.06)
                    screen.blit(background_image, background_rect)  # Draw background
                    display_players()
                    display_roll_message(current_player)
                    draw_board()  # Draw board label
                    draw_leader()  # Draw leaderboard label
                    roll_button.draw(screen)
                    dice1_button.draw(screen)
                    dice2_button.draw(screen)
                    pygame.display.update()
                    pygame.time.delay(50)  # Add a delay of 50 milliseconds between frames

                # Update dice buttons based on the rolled values
                dice1_button = button.Button(720, 350, dice_images[dice1 - 1], 0.06)
                dice2_button = button.Button(850, 350, dice_images[dice2 - 1], 0.06)

                # Move player's piece, handle game logic here
                if dice1 != 6 and dice2 != 6:
                    current_player = "Player 2" if current_player == "Player 1" else "Player 1"

    pygame.display.update()
    clock.tick(20)  # Limit frame rate to 30 FPS

pygame.quit()

