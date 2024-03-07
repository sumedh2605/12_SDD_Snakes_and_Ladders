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
#background_image_x = 0
#background_image_y = 0

# Define the label position and text
#label_x = 300
#label_y = 200
# label_text = "Snakes and Ladders"
game_board_image_x = 0
game_board_image_y = 0
label_x = 500
label_y = 200
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
play_button = button.Button(350, 400, start_image, 0.8)
exit_button = button.Button(700, 400, exit_image, 0.8)

# select no of players images (from Shreeya's code)
select_two_players_img = pygame.transform.scale(pygame.image.load("./images/player2.jpg").convert_alpha(), (200, 200))
select_three_players_img = pygame.transform.scale(pygame.image.load("./images/player3.jpg").convert_alpha(), (200, 200))
select_four_players_img = pygame.transform.scale(pygame.image.load("./images/player4.jpg").convert_alpha(), (200, 200))
select_two_players_button = button.Button(250, 400, select_two_players_img, 0.8)
select_three_players_button = button.Button(510, 400, select_three_players_img, 0.8)
select_four_players_button = button.Button(770, 400, select_four_players_img, 0.8)

# Roll dice button image
# button_img = pygame.image.load("./dice_images/click me.jpg").convert_alpha()
roll_dice_button_img = pygame.transform.scale(pygame.image.load("./dice_images/click me.jpg").convert_alpha(),
                                              (100, 100))
roll_dice_button = button.Button(700, 600, roll_dice_button_img, 0.06)

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
dice_images = [pygame.transform.scale(pygame.image.load(f"./dice_images/{i}.png").convert_alpha(), (100, 100)) for i in
               range(1, 7)]

# Gaytri's code
grid = []
for i in range(650, 15, -70):  # y coordinate
    row = []
    for j in range(15, 650, 70):  # x coordinates
        row.append((j, i))
    grid.append(row)
print(f"grid = {grid}")

# cords_grid = []
# for i in range (650, 15, -70):#y coordinate
#     # row = []
#     for j in range (15, 650, 70):#x coordinates
#         cords_grid.append((j,i))


# Pawns initialization
# Xone, Yone = grid[0][0]
# Xtwo, Ytwo = grid[0][0]
# Xthree, Ythree = grid[0][0]
# Xfour, Yfour = grid[0][0]
Xone, Yone = (15, 700)
Xtwo, Ytwo = (45, 700)
Xthree, Ythree = (75, 700)
Xfour, Yfour = (105, 700)

pawns = [pawn1, pawn2, pawn3, pawn4]
# pawn_names = ['1','2','3','4']
coords = [[Xone, Yone], [Xtwo, Ytwo], [Xthree, Ythree], [Xfour, Yfour]]

r = 0

resized = [False, False, False, False]

current_player = 1  # Start with Player 1


# Defining background
def background(background_image):
    size = pygame.transform.scale(background_image,(1200,800))
    screen.blit(size,(0,0))


# Function to display players
def display_players(player_count):
    for player in range(player_count):
        pass
        #player_msg = font1.render(f"Player{player}", True, (255, 255, 255))
        #screen.blit(player_msg, (850, 491 + 30 * player))


def display_pawns(player_count):
    # load all players onto board
    for i in range(player_count):
        screen.blit(pawns[i], (coords[i][0], coords[i][1]))
        # screen.blit(pawn2, (coords[1][0], coords[1][1]))
        # screen.blit(pawn3, (coords[2][0], coords[2][1]))
        # screen.blit(pawn4, (coords[3][0], coords[3][1]))    
        # screen.blit(pawn1, (850,491+30))
        # screen.blit(pawn2, (850, 491+60))
        # screen.blit(pawn3, (850, 491+90))
        # screen.blit(pawn4, (850, 491+120))


# Function to display whose turn it is to roll
def display_roll_message(player):
    # print(f"display roll message player = {player}")
    msg = font2.render(f"Player{player}'s turn.Click to roll the dice", True, (255, 255, 155))
    y_position = 499
    screen.blit(msg, (700, y_position))

def draw_start_label():
      label_text = font.render("Snakes N Ladders", True, "White")
      screen.blit(label_text, (500, 200))


# Define a function to draw the label
def draw_label():
    # Draw the label text
    label = font.render("Select number of players", True, "White")
    label_rect = label.get_rect()
    label_rect.topleft = (label_x, label_y)
    screen.blit(label, label_rect)


def draw_board():
    label = font.render("board", True, "White")
    screen.blit(game_board_image, (game_board_image_x, game_board_image_y))


def draw_leader():
    label = font.render("leaderboard", True, "White")
    screen.blit(label, (label2_x, label2_y))


def find_next_player(current_player):
    current_player_index = players_list.index(current_player)
    if players.get_is_complted_game(player_id=current_player) == 1 and current_player_index < len(players_list):
        # remove player from players_list, now next player is at the current players index
        players_list.remove(current_player)
        next_player = players_list[current_player_index]
    elif players.get_is_complted_game(player_id=current_player) == 1 and current_player_index == len(players_list):
        # remove player from players_list, now next player is at the current players index
        players_list.remove(current_player)
        if len(players_list) != 0:
            next_player = players_list[0]

    print(f"current_player_index = {current_player_index}")
    if current_player_index + 1 == len(players_list):
        index = 0
        next_player = players_list[index]
    else:
        index = current_player_index + 1
        next_player = players_list[index]
    print(f"index = {index}")
    return next_player


# gaytri needs to change
def movement(X, Y, d, player_turn, dice_sum):
    if d < dice_sum:
        # time.sleep(2)
        pygame.display.update()
        if Y == 700:  # players first turn
            X = 15
            Y = 650
        else:
            if Y == 650 or Y == 510 or Y == 370 or Y == 230 or Y == 90:  # switch direction every other row
                X += 70
            else:
                X -= 70

            if X > 700:  # border to go up one row
                X = 645
                Y -= 70
            if X < 0:
                X = 15
                Y -= 70
        coords[player_turn - 1][0] = X
        coords[player_turn - 1][1] = Y
        pygame.display.update()

        # screen.blit(pawn1, (coords[0][0], coords[0][1]))
        # screen.blit(pawn2, (coords[1][0], coords[1][1]))
        # screen.blit(pawn3, (coords[2][0], coords[2][1]))

        pygame.display.update()
        # screen.blit(pawn4, (coords[3][0], coords[3][1]))
    print(f"Movement X= {X}, Y={Y}")
    return (X, Y)


# def move_vector(player_turn, players_current_pos, players_new_pos):
#     Xpos = coords[player_turn-1][0]
#     Ypos = coords[player_turn-1][1]
#     player_vector = pygame.math.Vector2(Xpos, Ypos)

#     print(f"players_current_pos = {players_current_pos}")
#     print(f"players_tentative_new_pos = {players_tenatative_new_position}")
#     target_vector= pygame.math.Vector2(cords_grid[i])
#     print(f"target_x_pos = {target_vector.x}, target_ypos={target_vector.y}")
#     player_vector.move_towards_ip(target_vector, 5)
#     print(f"Xpos = {player_vector.x}")
#     print(f"Ypos = {player_vector.y}")

def move_source_to_target_linear(player_count, player_turn, player_vector, current_pos, target_pos):
    for i in range(current_pos + 1, target_pos, 1):
        # move to next grid
        target2_vector = pygame.math.Vector2(board_cords[i])
        distance_needs_to_travel = player_vector.distance_to(target2_vector)
        print(f"distance needs to travel = {distance_needs_to_travel}")
        # player_vector.move_towards_ip(target2_vector, distance_needs_to_travel)

        distance = 5
        while distance <= distance_needs_to_travel:
            player_vector.move_towards_ip(target2_vector, 5)
            # print(f"Xpos = {player_vector.x}")
            # print(f"Ypos = {player_vector.y}")
            distance = distance + 5
            # distance_needs_to_travel = player_vector.distance_to(target2_vector)

            coords[player_turn - 1][0] = player_vector.x
            coords[player_turn - 1][1] = player_vector.y

            draw_board()
            # screen.blit(pawn1, (coords[0][0], coords[0][1]))
            display_pawns(player_count=player_count)
            pygame.display.update()
            clock.tick(30)
        # clock.tick(2)
        # screen.blit(pawn1, (coords[0][0], coords[0][1]))


def move_source_to_target_diagonal(player_count, player_turn, player_vector, current_pos, target_pos):
    # move to next grid
    target2_vector = pygame.math.Vector2(board_cords[target_pos - 1])
    distance_needs_to_travel = player_vector.distance_to(target2_vector)
    print(f"distance needs to travel = {distance_needs_to_travel}")
    # player_vector.move_towards_ip(target2_vector, distance_needs_to_travel)

    distance = 5
    while distance <= distance_needs_to_travel:
        player_vector.move_towards_ip(target2_vector, 5)
        # print(f"Xpos = {player_vector.x}")
        # print(f"Ypos = {player_vector.y}")
        distance = distance + 5
        # distance_needs_to_travel = player_vector.distance_to(target2_vector)

        coords[player_turn - 1][0] = player_vector.x
        coords[player_turn - 1][1] = player_vector.y

        draw_board()
        # screen.blit(pawn1, (coords[0][0], coords[0][1]))
        display_pawns(player_count=player_count)
        pygame.display.update()
        clock.tick(30)
    # clock.tick(2)
    # screen.blit(pawn1, (coords[0][0], coords[0][1]))


def move_player_from_current_pos_to_target_pos(player_count, player_turn, players_current_pos,
                                               players_tenatative_new_position, players_confirmed_new_position):
    print(f"players_current_pos = {players_current_pos}")
    print(f"players_tentative_new_pos = {players_tenatative_new_position}")
    current_xpos = coords[player_turn - 1][0]
    current_ypos = coords[player_turn - 1][1]

    print(f"players current xpos = {current_xpos}, ypos = {current_ypos}")

    player_vector = pygame.math.Vector2(current_xpos, current_ypos)
    if players_current_pos == 0:
        target_vector = pygame.math.Vector2(board_cords[0])
        print(f"target_x_pos = {target_vector.x}, target_ypos={target_vector.y}")
        player_vector.move_towards_ip(target_vector, 50)
        # print(f"Xpos = {player_vector.x}")
        # print(f"Ypos = {player_vector.y}")

        coords[player_turn - 1][0] = player_vector.x
        coords[player_turn - 1][1] = player_vector.y

        # players_tenatative_new_position = 10
        # clock.tick(3)
        draw_board()
        display_pawns(player_count=3)
        # screen.blit(pawn1, (coords[0][0], coords[0][1]))
        pygame.display.update()

        clock.tick(30)

    # for i in range(players_current_pos+1, players_tenatative_new_position, 1):
    #     # move to next grid
    #     target2_vector = pygame.math.Vector2(board_cords[i])
    #     distance_needs_to_travel = player_vector.distance_to(target2_vector)
    #     print(f"distance needs to travel = {distance_needs_to_travel}")
    #     # player_vector.move_towards_ip(target2_vector, distance_needs_to_travel)

    #     distance = 5
    #     while distance <= distance_needs_to_travel:

    #         player_vector.move_towards_ip(target2_vector, 5)
    #         # print(f"Xpos = {player_vector.x}")
    #         # print(f"Ypos = {player_vector.y}")
    #         distance = distance + 5
    #         # distance_needs_to_travel = player_vector.distance_to(target2_vector)

    #         coords[player_turn-1][0] = player_vector.x
    #         coords[player_turn-1][1] = player_vector.y

    #         draw_board()
    #         # screen.blit(pawn1, (coords[0][0], coords[0][1]))
    #         display_pawns(player_count=3)
    #         pygame.display.update()
    #         clock.tick(30)
    #     # clock.tick(2)
    #     # screen.blit(pawn1, (coords[0][0], coords[0][1]))

    move_source_to_target_linear(player_count=player_count, player_turn=player_turn, player_vector=player_vector,
                                 current_pos=players_current_pos, target_pos=players_tenatative_new_position)
    # ladder found
    if (players_confirmed_new_position > players_tenatative_new_position) or (
            players_confirmed_new_position < players_tenatative_new_position):
        move_source_to_target_diagonal(player_count=player_count, player_turn=player_turn, player_vector=player_vector,
                                       current_pos=players_tenatative_new_position,
                                       target_pos=players_confirmed_new_position)
    # snake found
    # if players_confirmed_new_position < players_tenatative_new_position:
    #     move_source_to_target(player_turn, player_vector, current_pos=players_tenatative_new_position, target_pos=players_confirmed_new_position)


def move_player(player_turn, players_current_pos, players_tenatative_new_position, players_confirmed_new_position):
    Xpos = coords[player_turn - 1][0]
    Ypos = coords[player_turn - 1][1]

    print(f"XPos = {Xpos}, YPos = {Ypos}")

    r = 0
    print(
        f"players current position = {players_current_pos}, player_tentative_position = {players_tenatative_new_position}, players_confirmed_new_position = {players_confirmed_new_position}")

    while r != players_tenatative_new_position - players_current_pos:
        # pygame.display.update()
        # clock.tick(60)
        Xpos, Ypos = movement(Xpos, Ypos, r, player_turn=player_turn,
                              dice_sum=players_tenatative_new_position - players_current_pos)
        # pygame.time.delay(50)
        r += 1  # increment the number of steps move
        clock.tick(30)
        pygame.display.update()
        # clock.tick(10)
        # clock.tick(60)
    r = 0

    # ladder encountered
    if players_tenatative_new_position != players_confirmed_new_position and players_tenatative_new_position < players_confirmed_new_position:
        print(f"Ladder encountered: value of r = {r}")

        # pygame.display.update()
        while r != players_confirmed_new_position - players_tenatative_new_position:
            Xpos, Ypos = movement(Xpos, Ypos, r, player_turn=player_turn,
                                  dice_sum=players_tenatative_new_position - players_current_pos)
            r += 1  # increment the number of steps move
            # clock.tick(3)
            # clock.tick(60)
    r = 0
    # snake encountered
    if players_tenatative_new_position != players_confirmed_new_position and players_tenatative_new_position > players_confirmed_new_position:
        print(f"Snake encountered : value of r = {r}")
        # pygame.display.update()
        while r != players_tenatative_new_position - players_confirmed_new_position:
            Xpos, Ypos = movement(Xpos, Ypos, r, player_turn=player_turn,
                                  dice_sum=players_tenatative_new_position - players_current_pos)
            r -= 1  # increment the number of steps move
            # clock.tick(3)
            # clock.tick(60)
    r = 0
    pygame.display.update()


def game_board_screen(player_count):
    pygame.display.set_caption("Snake and ladder: Game Board Screen")
    size = pygame.transform.scale(background_image,(1200,800))
    current_player = 1
    run = True
    while run:
        clock = pygame.time.Clock()
        # clock.tick(3)
        screen.blit(size,(0,0))  # Draw background
        display_roll_message(current_player)
        draw_board()  # Draw board label
        # draw_leader()  # Draw leaderboard label

        # load all players onto board # from gayatri

        display_pawns(player_count=3)
        # screen.blit(pawn1, (coords[0][0], coords[0][1]))
        # screen.blit(pawn2, (coords[1][0], coords[1][1]))
        # screen.blit(pawn3, (coords[2][0], coords[2][1]))
        # screen.blit(pawn4, (coords[3][0], coords[3][1]))
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
                    print(f"playing for current_player = {current_player}")

                    # Roll the dice
                    for i in range(6):
                    # dice1, dice2 = dice.roll_dice(player_id=current_player)
                        dice_output = Roll_dice.dice_roll()
                        dice1 = dice_output[0]
                        dice2 = dice_output[1]

                        dice_sum = dice1 + dice2
                        print(f"*** player_id = {current_player}")
                        unlucky_rolls = players.get_unlucky_roll_list(player_id=current_player)
                        print(f"unlucky_rolls = {unlucky_rolls}")
                        if unlucky_rolls != None:
                            while (dice_sum in unlucky_rolls):
                                dice_output = Roll_dice.dice_roll()

                                dice1 = dice_output[0]
                                dice2 = dice_output[1]
                                dice_sum = dice1 + dice2
                                print(f"lucky_roll dice_sum {dice_sum} = {dice1} + {dice2}")

                        if dice_sum == 12:
                        # get consecutive turn count for player
                            consecutive_turn_count = players.get_consecutive_turn_count(player_id=current_player)
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

                        #screen.blit(background_image, background_image_rect)  # Draw background
                        display_players(player_count)
                        display_pawns(player_count=player_count)
                    # screen.blit(pawn1, (coords[0][0], coords[0][1]))
                    # screen.blit(pawn2, (coords[1][0], coords[1][1]))
                    # screen.blit(pawn3, (coords[2][0], coords[2][1]))
                    # screen.blit(pawn4, (coords[3][0], coords[3][1]))
                    # display_roll_message(current_player)
                        draw_board()  # Draw board label
                    #draw_leader()  # Draw leaderboard label
                        roll_dice_button.draw(screen)
                        dice1_button.draw(screen)
                        dice2_button.draw(screen)
                        pygame.display.update()
                        pygame.time.delay(200)  # Add a delay of 50 milliseconds between frames

                    # Play turn for current player
                    players_current_pos = players.get_player_current_postion(current_player)
                    projected_new_pos, confirmed_new_position = players.play(current_player, dice_sum=dice_sum)
                    if confirmed_new_position == 100:
                        print(f"Player : {current_player} reached to 100 position")
                        # remove player from players_list
                        # players_list.remove(current_player)
                    print(
                        f"tentative_new_postion = {projected_new_pos}, confirmed_new_position = {confirmed_new_position}")
                    # Move player's piece, handle game logic here # Gayatri to fix below method
                    # move_player(current_player, players_current_pos=players_current_pos, players_tenatative_new_position=projected_new_pos, players_confirmed_new_position=confirmed_new_position)
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

        pygame.display.update()
        # clock.tick(20)  # Limit frame rate to 30 FPS


def select_number_of_players_screen():
    run = True
    global players_list
    pygame.display.set_caption("Snake and ladder: Player Input")

    while run:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("black")
        background(background_image)
        draw_label()

        select_two_players_button.draw(screen)
        select_three_players_button.draw(screen)
        select_four_players_button.draw(screen)

        # players_list = []

        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if select_two_players_button.draw(screen):
                    player_count = 2
                    players_list = players.create_players(2)
                    print(f"players_list = {players_list}")
                if select_three_players_button.draw(screen):
                    player_count = 3
                    players_list = players.create_players(3)
                    # players.create_players(3)
                if select_four_players_button.draw(screen):
                    player_count = 4
                    players_list = players.create_players(4)
                    # players.create_players(4)

                print(f"players_list = {players_list}, player_count = {player_count}")
                # players_list = [i+1 for i in range(1, player_count)]
                game_board_screen(player_count)

        pygame.display.update()


# Calling backgroung image
background(background_image)
# Create a game loop
running = True
while running:

    draw_start_label()
    play_button.draw(screen)
    exit_button.draw(screen)

    # Handle events
    for event in pygame.event.get():
        # If the user clicks the close button, exit the loop
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if play_button.draw(screen):
            print(f"play")
            select_number_of_players_screen()

        if exit_button.draw(screen):
            print(f"exit")
            running = False
    pygame.display.update()

# Quit pygame
pygame.quit()

