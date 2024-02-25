import pygame
import sys
import button
import random

# Initialize Pygame
pygame.init()

# Set up the window
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game screen")

# Load background image
background_image = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\bg.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Define the font for the label
font = pygame.font.SysFont("Arial", 100)

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
font1 = pygame.font.SysFont("Arial", 45)
font2 = pygame.font.SysFont("Arial", 40)
font_player = pygame.font.SysFont("Arial", 30)
font_roll = pygame.font.SysFont("Arial", 30)

# Function to display players
def display_players(players):
    player_msg_positions = []
    for i in range(len(players)):
        player_msg_positions.append((SCREEN_WIDTH - 250, 451 + 50*i))
    
    for i in range(len(players)):
        player_msg = font_player.render(f"{players[i]}", True, (255, 255, 255))
        screen.blit(player_msg, player_msg_positions[i])

# Function to display whose turn it is to roll
def display_roll_message(player):
    msg = font_roll.render("Click to roll the dice", True, (255, 255, 155))
    y_position = 480 if player == players[0] else 530 if player == players[1] else 579 if player == players[2] else 632
    screen.blit(msg, (960, y_position))

# Load start button image
button_img = pygame.image.load("C:\\Users\\mahes\\Desktop\\Project\\click me.jpg").convert_alpha()
roll_button = button.Button(50, 550, button_img, 0.06)

# Load dice images
dice_images = [pygame.image.load(f"C:\\Users\\mahes\\Desktop\\Project\\dice\\{i}.jpg").convert_alpha() for i in range(1, 7)]

# Input number of players
num_players = 4
players = [f"Player {i+1}" for i in range(num_players)]
current_player_index = 0  # Start with Player 1

# Game loop
clock = pygame.time.Clock()
running = True

# Create dice buttons
dice1_button = button.Button(720, 350, dice_images[0], 0.06)
dice2_button = button.Button(850, 350, dice_images[0], 0.06)

rolling = False
roll_animation_counter = 0
final_dice1 = 1
final_dice2 = 1

while running:
    screen.blit(background_image, (0, 0))  # Draw background
    display_players(players)
    display_roll_message(players[current_player_index])
    draw_board()  # Draw board label
    draw_leader()  # Draw leaderboard label

    # Draw buttons
    roll_button.draw(screen)
    dice1_button.draw(screen)
    dice2_button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if roll_button.rect.collidepoint(event.pos) and not rolling:
                rolling = True

    if rolling:
        roll_animation_counter += 1
        if roll_animation_counter < 20:
            # Simulate rolling animation
            dice1_button.image = dice_images[random.randint(0, 5)]
            dice2_button.image = dice_images[random.randint(0, 5)]
        else:
            # Roll the dice and display final values
            final_dice1 = random.randint(1, 6)
            final_dice2 = random.randint(1, 6)
            dice1_button.image = dice_images[final_dice1 - 1]
            dice2_button.image = dice_images[final_dice2 - 1]

            # Check if it's a double roll of 6
            if final_dice1 == 6 and final_dice2 == 6:
                # Handle double roll logic here
                pass
            else:
                # Move player's piece, handle game logic here
                current_player_index = (current_player_index + 1) % num_players
                rolling = False
                roll_animation_counter = 0

    pygame.display.update()
    clock.tick(20)  # Limit frame rate to 20 FPS

pygame.quit()


