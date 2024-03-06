# Import pygame module
import pygame
import sys
import random
# from dice import dice
from dice import Roll_dice
from button import button
from players import players
from uiconstants.constants import BLACK
from players import players
from snake_and_ladder_check import snake_and_ladder_check
import time
from uiconstants.board_cord import board_cords

# Initialize pygame
pygame.init()

# Window
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
# Create a display surface object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# Define a font object
font = pygame.font.SysFont("Arial", 32)
font1 = pygame.font.SysFont("Ariel", 45)
font2 = pygame.font.SysFont("Ariel", 40)

# set up clock
clock = pygame.time.Clock()

players_list = []

# Update the display
pygame.display.flip()

# Defining starting cordinates of background image
background_image_x = 0
background_image_y = 0

# Define the label position and text
label_x = 90
label_y = 200
# label_text = "Snakes and Ladders"
game_board_image_x = 0
game_board_image_y = 0
label_x = 10
label_y = 10
label2_x = 560
label2_y = 70

# images in the game
# background image
background_image = pygame.image.load(r'./images/bg.jpg')
background_image_rect = background_image.get_rect()
# start and exit images
start_image = pygame.image.load("./images/start.jpg").convert_alpha()
exit_image = pygame.image.load("./images/exit.jpg").convert_alpha()
# create button instance
play_button = button.Button(250, 400, start_image, 0.8)
exit_button = button.Button(600, 400, exit_image, 0.8)

# select no of players images (from Shreeya's code)
select_two_players_img = pygame.transform.scale(pygame.image.load("./images/player2.jpg").convert_alpha(), (200, 200))
select_three_players_img = pygame.transform.scale(pygame.image.load("./images/player3.jpg").convert_alpha(), (200, 200))
select_four_players_img = pygame.transform.scale(pygame.image.load("./images/player4.jpg").convert_alpha(), (200, 200))
select_two_players_button = button.Button(150, 400, select_two_players_img, 0.8)
select_three_players_button = button.Button(410, 400, select_three_players_img, 0.8)
select_four_players_button = button.Button(670, 400, select_four_players_img, 0.8)

# Roll dice button image
# button_img = pygame.image.load("./dice_images/click me.jpg").convert_alpha()
roll_dice_button_img = pygame.transform.scale(pygame.image.load("./dice_images/click me.jpg").convert_alpha(),
                                              (100, 100))
roll_dice_button = button.Button(900, 600, roll_dice_button_img, 0.06)

# background_image = pygame.image.load("./dice_images/bg.jpg")
# background_image_rect = background_image.get_rect()
# game board image
snake_and_ladder_board_image = pygame.image.load("./images/istockphoto-531466314-1024x1024.jpg")
game_board_image = pygame.transform.scale(snake_and_ladder_board_image, (700, 700))

# pawn images
pawn1 = pygame.transform.scale(pygame.image.load("./pawn_images/pawn.png").convert_alpha(), (40, 40))
pawn2 = pygame.transform.scale(pygame.image.load("./pawn_images/pawn2.png").convert_alpha(), (40, 40))
pawn3 = pygame.transform.scale(pygame.image.load("./pawn_images/pawn3.png").convert_alpha(), (40, 40))
pawn4 = pygame.transform.scale(pygame.image.load("./pawn_images/pawn4.png").convert_alpha(), (40, 40))

# dice images
dice_images = [pygame.transform.scale(pygame.image.load(f"./dice_images/{i}.jpg").convert_alpha(), (100, 100)) for i in
               range(1, 7)]

# Pawns Initial positions
Xone, Yone = (15, 700)
Xtwo, Ytwo = (45, 700)
Xthree, Ythree = (75, 700)
Xfour, Yfour = (105, 700)

pawns = [pawn1, pawn2, pawn3, pawn4]

coords = [[Xone, Yone], [Xtwo, Ytwo], [Xthree, Ythree], [Xfour, Yfour]]

r = 0

resized = [False, False, False, False]

current_player = 1  # Start with Player 1


# Defining background
def background():
    screen.blit(background_image, (background_image_x, background_image_y))


# Function to display players    -done by Shreya, modularise by sumedh
def display_players(player_count):
    for player in range(player_count):
        player_msg = font1.render(f"Player{player}", True, (255, 255, 255))
        screen.blit(player_msg, (850, 491 + 30 * player))


# Function to display pawns   -done by Gayatri, modularise by sumedh
def display_pawns(player_count):
    # load all players onto board
    for i in range(player_count):
        screen.blit(pawns[i], (coords[i][0], coords[i][1]))


# Function to display whose turn it is to roll  -done by shreya, modularise by sumedh
def display_roll_message(player):
    msg = font2.render(f"Player{player}'s  turn. Click to roll the dice", True, (255, 255, 155))
    y_position = 599
    screen.blit(msg, (850, y_position))


# Define a function to draw the label  -done by shreya, modularise by sumedh
def draw_label():
    # Draw the label text
    label = font.render("Select number of players", True, "White")
    label_rect = label.get_rect()
    label_rect.topleft = (label_x, label_y)
    screen.blit(label, label_rect)


# Darw board   - done by shreya, modularised bu sumedh
def draw_board():
    label = font.render("board", True, "White")
    screen.blit(game_board_image, (game_board_image_x, game_board_image_y))


# Draw leader
def draw_leader():
    label = font.render("leaderboard", True, "White")
    screen.blit(label, (label2_x, label2_y))


# find next player  - done by shreya, modularise by sumedh and added extra functionalities to find next player when current player has won
def find_next_player(current_player):
    """
    Find Next player
    Args:
        current_player: current player

    Returns: next_player

    """
    current_player_index = players_list.index(current_player)
    # check if current player reaches to winning position
    if players.get_is_complted_game(player_id=current_player) == 1 and current_player_index + 1 < len(players_list):
        # remove player from players_list, now next player is at the current players index
        players_list.remove(current_player)
        next_player = players_list[current_player_index]
        return next_player
    elif players.get_is_complted_game(player_id=current_player) == 1 and current_player_index + 1 == len(players_list):
        # remove player from players_list, now next player is at the current players index
        players_list.remove(current_player)
        if len(players_list) != 0:
            next_player = players_list[0]
        return next_player

    if current_player_index + 1 == len(players_list):
        index = 0
        next_player = players_list[index]
    else:
        index = current_player_index + 1
        next_player = players_list[index]
    return next_player


# done by sumedh
def move_source_to_target_linear(player_count, player_turn, player_vector, current_pos, target_pos):
    """Move current player from current position to target position in linear manner

    Args:
        player_count (int): Total no of players
        player_turn (int): current player
        player_vector (Vector): player vector
        current_pos (int): current position
        target_pos (int): target position
    """
    # move to next tile until reaches to target_pos
    for i in range(current_pos + 1, target_pos, 1):
        target_vector = pygame.math.Vector2(board_cords[i])
        distance_needs_to_travel = player_vector.distance_to(target_vector)

        distance = 5
        while distance <= distance_needs_to_travel:
            # moves 5 pixels in target vectors direction
            player_vector.move_towards_ip(target_vector, 5)
            distance = distance + 5
            coords[player_turn - 1][0] = player_vector.x
            coords[player_turn - 1][1] = player_vector.y
            draw_board()
            display_pawns(player_count=player_count)
            pygame.display.update()
            clock.tick(30)


# done by sumedh
def move_source_to_target_diagonal(player_count, player_turn, player_vector, current_pos, target_pos):
    """Move current player from source to target in diagonal path

    Args:
        player_count (int): Total no of players
        player_turn (int): current player
        player_vector (Vector): player vector
        current_pos (int): current position
        target_pos (int): target position
    """
    # move to next grid
    target2_vector = pygame.math.Vector2(board_cords[target_pos - 1])
    distance_needs_to_travel = player_vector.distance_to(target2_vector)

    distance = 5
    while distance <= distance_needs_to_travel:
        # moves 5 pixels in target vectors direction
        player_vector.move_towards_ip(target2_vector, 5)
        distance = distance + 5
        coords[player_turn - 1][0] = player_vector.x
        coords[player_turn - 1][1] = player_vector.y

        draw_board()
        display_pawns(player_count=player_count)
        pygame.display.update()
        clock.tick(30)


# done by sumedh
def move_player_from_current_pos_to_target_pos(player_count, player_turn, players_current_pos,
                                               players_tenatative_new_position, players_confirmed_new_position):
    # get cordinatates for players current posistion
    current_xpos = coords[player_turn - 1][0]
    current_ypos = coords[player_turn - 1][1]

    # Craete player vector based on current position
    player_vector = pygame.math.Vector2(current_xpos, current_ypos)
    # Very first movement to bring pawns on game board
    if players_current_pos == 0:
        target_vector = pygame.math.Vector2(board_cords[0])
        player_vector.move_towards_ip(target_vector, 50)
        # update current players cordinates to player vector target position
        coords[player_turn - 1][0] = player_vector.x
        coords[player_turn - 1][1] = player_vector.y

        draw_board()
        display_pawns(player_count=player_count)
        pygame.display.update()
        clock.tick(30)

    # move from players current position to projected new position
    move_source_to_target_linear(player_count, player_turn, player_vector, current_pos=players_current_pos,
                                 target_pos=players_tenatative_new_position)
    # ladder or snake found
    if (players_confirmed_new_position > players_tenatative_new_position) or (
            players_confirmed_new_position < players_tenatative_new_position):
        # move from players projected new posistion to players confirmed new position
        move_source_to_target_diagonal(player_count, player_turn, player_vector,
                                       current_pos=players_tenatative_new_position,
                                       target_pos=players_confirmed_new_position)


def final_results_screen():
    print("Game Over !!! screen with All states for player")

# Its an integration module by sumedh
def game_board_screen(player_count):
    pygame.display.set_caption("Snake and ladder: Game Board Screen")
    current_player = 1
    run = True
    while run:
        clock = pygame.time.Clock()
        screen.blit(background_image, background_image_rect)  # Draw background
        display_roll_message(current_player)
        draw_board()  # Draw board label
        # draw_leader()  # Draw leaderboard label

        # load all players onto board
        display_pawns(player_count=player_count)

        # Draw buttons
        roll_dice_button.draw(screen)

        if 'dice1_button' in locals():
            dice1_button.draw(screen)
        if 'dice2_button' in locals():
            dice2_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # pygame.QUIT
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                display_roll_message(current_player)
                if roll_dice_button.rect.collidepoint(event.pos):
                    # Roll dice for current player
                    dice_output = Roll_dice.dice_roll()
                    dice1 = dice_output[0]
                    dice2 = dice_output[1]
                    dice_sum = dice1 + dice2

                    # This is used mainly to find overrun count and provide players lucky roll
                    unlucky_rolls = players.get_unlucky_roll_list(player_id=current_player)

                    if unlucky_rolls != None:
                        while (dice_sum in unlucky_rolls):
                            dice_output = Roll_dice.dice_roll()
                            dice1 = dice_output[0]
                            dice2 = dice_output[1]
                            dice_sum = dice1 + dice2
                    # get consecutive turn count for player
                    if dice_sum == 12:
                        consecutive_turn_count = players.get_consecutive_turn_count(player_id=current_player)
                        # If consecutive_turn_count reaches to 3 , Make sure player will not get another roll with dice_sum=12
                        if consecutive_turn_count == 3:
                            while dice_sum == 12:
                                dice_output = Roll_dice.dice_roll(player_id=current_player)
                                dice1 = dice_output[0]
                                dice2 = dice_output[1]
                                dice_sum = dice1 + dice2

                    # Update dice buttons based on the rolled values
                    dice1_button = button.Button(720, 350, dice_images[dice1 - 1], 0.06)
                    dice2_button = button.Button(850, 350, dice_images[dice2 - 1], 0.06)
                    dice_sum = dice1 + dice2

                    screen.blit(background_image, background_image_rect)  # Draw background
                    display_players(player_count)
                    draw_board()  # Draw board label

                    # draw_leader()  # Draw leaderboard label
                    display_pawns(player_count=player_count)
                    roll_dice_button.draw(screen)
                    dice1_button.draw(screen)
                    dice2_button.draw(screen)
                    pygame.display.update()
                    pygame.time.delay(50)  # Add a delay of 50 milliseconds between frames

                    # Play turn for current player
                    players_current_pos = players.get_player_current_postion(current_player)
                    projected_new_pos, confirmed_new_position = players.play(current_player, dice_sum=dice_sum)




                    # Move player from current position to target position
                    if players_current_pos != 100:
                        move_player_from_current_pos_to_target_pos(player_count, current_player,
                                                                   players_current_pos=players_current_pos,
                                                                   players_tenatative_new_position=projected_new_pos,
                                                                   players_confirmed_new_position=confirmed_new_position)

                        # Update players_current_pos
                        players.update_player_current_postion(player_id=current_player)
                    if dice_sum != 12:

                        # check if all players reach on hundered/winning position
                        if len(players.get_winners()) != player_count:
                            current_player = find_next_player(current_player=current_player)
                            print(f"next players is = {current_player}")
                        else:
                            print(f"Game Over !!!!")

        pygame.display.update()


# done by shreya, modularised by sumedh
def select_number_of_players_screen():
    run = True
    global players_list
    pygame.display.set_caption("Snake and ladder: Player Input")

    while run:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("black")
        background()
        draw_label()

        select_two_players_button.draw(screen)
        select_three_players_button.draw(screen)
        select_four_players_button.draw(screen)

        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if select_two_players_button.draw(screen):
                    players_list = players.create_players(2)
                if select_three_players_button.draw(screen):
                    players_list = players.create_players(3)
                if select_four_players_button.draw(screen):
                    players_list = players.create_players(4)
                player_count = len(players_list)
                # call game board screen
                game_board_screen(player_count)

        pygame.display.update()


# Calling backgroung image
background()
# Create a game loop
running = True
while running:

    play_button.draw(screen)
    exit_button.draw(screen)

    # Handle events
    for event in pygame.event.get():
        # If the user clicks the close button, exit the loop
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        #select number of players screen
        if play_button.draw(screen):
            select_number_of_players_screen()

        if play_button.draw(screen):
            print(f"exit")
    pygame.display.update()

# Quit pygame
pygame.quit()

