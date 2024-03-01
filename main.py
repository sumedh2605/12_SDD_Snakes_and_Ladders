
# Import pygame module
import pygame
import sys
import random
from dice import dice
from button import button
from players import players
from uiconstants.constants import BLACK
from players import players
from snake_and_ladder_check import snake_and_ladder_check
import time

# Initialize pygame
pygame.init()

#Window
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

players_list=None

# Update the display
pygame.display.flip()

#Defining starting cordinates of background image
background_image_x = 0
background_image_y = 0

# Define the label position and text
label_x = 90
label_y = 200
#label_text = "Snakes and Ladders"
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
#create button instance
play_button = button.Button(250, 400, start_image,0.8)
exit_button = button.Button(600, 400, exit_image,0.8)

# select no of players images (from Shreeya's code)
select_two_players_img = pygame.transform.scale(pygame.image.load("./images/player2.png").convert_alpha(),(400,400))
select_three_players_img = pygame.transform.scale(pygame.image.load("./images/player3.png").convert_alpha(),(400,400))
select_four_players_img = pygame.transform.scale(pygame.image.load("./images/player4.png").convert_alpha(),(400,400))
select_two_players_button = button.Button(120, 200, select_two_players_img,0.8)
select_three_players_button = button.Button(450, 200, select_three_players_img,0.8)
select_four_players_button = button.Button(750, 200, select_four_players_img, 0.8)

# Roll dice button image
# button_img = pygame.image.load("./dice_images/click me.jpg").convert_alpha()
roll_dice_button_img = pygame.transform.scale(pygame.image.load("./dice_images/click me.jpg").convert_alpha(), (100,100))
roll_dice_button = button.Button(700, 600, roll_dice_button_img, 0.06)

# background_image = pygame.image.load("./dice_images/bg.jpg")
# background_image_rect = background_image.get_rect()
# game board image
snake_and_ladder_board_image = pygame.image.load("./images/istockphoto-531466314-1024x1024.jpg")
game_board_image = pygame.transform.scale(snake_and_ladder_board_image, (700,700))

# pawn images
pawn1 = pygame.image.load("./pawn_images/pawn.png").convert_alpha()
pawn2 = pygame.image.load("./pawn_images/pawn2.png").convert_alpha()
pawn3 = pygame.image.load("./pawn_images/pawn3.png").convert_alpha()
pawn4 = pygame.image.load("./pawn_images/pawn4.png").convert_alpha()

#dice images
dice_images = [pygame.transform.scale(pygame.image.load(f"./dice_images/{i}.jpg").convert_alpha(),(100,100)) for i in range(1, 7)]

# Gaytri's code
grid = []
for i in range (700, 0, -70):#y coordinate
    row = []
    for j in range (0, 700, 70):#x coordinates
        row.append((j,i))
    grid.append(row)


# Pawns initialization
Xone, Yone = grid[0][0]
Xtwo, Ytwo = grid[0][0]
Xthree, Ythree = grid[0][0]
Xfour, Yfour = grid[0][0]

pawns = [pawn1, pawn2, pawn3, pawn4]
pawn_names = ['1','2','3','4']
coords = [[Xone, Yone],[Xtwo, Ytwo], [Xthree, Ythree], [Xfour,Yfour]]
ladderstartX, ladderstartY = grid[0][8]
ladderendX, ladderendY = grid[4][7]
snakestartX, snakestartY = grid[3][4]
snakeendX, snakeendY = grid[1][2]

r=0

resized = [False, False, False, False]

current_player = 1  # Start with Player 1


#Defining background
def background():
    screen.blit(background_image,(background_image_x,background_image_y))



# Function to display players
def display_players(player_count):
    for player in range(player_count):
        pass
        #player_msg = font1.render(f"Player{player}", True, (255, 255, 255))
        #screen.blit(player_msg, (850, 451+30*player))


def display_pawns(player_count):
       #load all players onto board
        screen.blit(pawn1, (850,491+30))
        screen.blit(pawn2, (850, 491+60))
        screen.blit(pawn3, (850, 491+90))
        screen.blit(pawn4, (850, 491+120))
     
        
# Function to display whose turn it is to roll
def display_roll_message(player):
    # print(f"display roll message player = {player}")
    msg = font2.render(f"Player{player}'s  turn. Click to roll the dice", True, (255, 255, 155))
    y_position = 599
    screen.blit(msg, (850, y_position))

def draw_start_label():
      label_text = font.render("Snakes N Ladders", True, "White")
      screen.blit(label_text, (500, 200))


# Define a function to draw the label
def draw_label():
  # Draw the label text
  label = font.render("Select number of players", True, "White")
  label_rect = label.get_rect()
  label_rect.topleft = (500,200)
  screen.blit(label, label_rect)


def draw_board():
    label = font.render("board", True, "White")
    screen.blit(game_board_image,(game_board_image_x, game_board_image_y))

def draw_leader():
    label = font.render("leaderboard", True, "White")
    screen.blit(label, (label2_x, label2_y))


def find_next_player(current_player, player_count):
    print(f"current_player = {current_player}, player_count = {player_count}")
    if current_player==player_count:
        next_player = 1
    else:
        next_player = current_player + 1
    return next_player

# gaytri needs to change
def movement(X, Y, d, player_turn, dice_sum):
    if d < dice_sum:
        pygame.display.update()
        if Y == 675 or Y == 525 or Y == 375 or Y == 225 or Y == 75:  # switch direction every other row
            X -= 65
        else:
            X += 65

        if X > 675:  # border to go up one row
            X = 675
            Y -= 65
        if X < 0:
            X = 0
            Y -= 65
        coords[player_turn-1][0] = X
        coords[player_turn-1][1] = Y
    print(f"Movement X= {X}, Y={Y}")
    return(X,Y)


def move_player(player_turn,dice_sum, players_current_pos, players_tenatative_new_position, players_confirmed_new_position):
    # quotient, remander =  divmod(players_current_pos, 10)
    # print(f"quotient = {quotient}, remander = {remander}")
    Xpos = coords[player_turn-1][0]
    Ypos = coords[player_turn-1][1]

    # Xpos, Ypos = grid[quotient][remander]
    print(f"XPos = {Xpos}, YPos = {Ypos}")
    
    r = 0
    print(f"players current position = {players_current_pos}, player_tentative_position = {players_tenatative_new_position}, players_confirmed_new_position = {players_confirmed_new_position}")
    # Xpos, Ypos = movement(Xpos , Ypos, r, player_turn=player_turn, dice_sum=dice_sum)
        # go to players tenatative new position 
        # go to players confirmed new position

    while r != players_tenatative_new_position - players_current_pos:
        Xpos, Ypos = movement(Xpos , Ypos, r, player_turn=player_turn, dice_sum=players_tenatative_new_position - players_current_pos)
            
        r += 1 # increment the number of steps move
        

    # ladder encountered
    if players_tenatative_new_position!=players_confirmed_new_position and players_tenatative_new_position < players_confirmed_new_position:
        print(f"Ladder encountered: value of r = {r}")
        while r != players_confirmed_new_position - players_tenatative_new_position:
            Xpos, Ypos = movement(Xpos , Ypos, r, player_turn=player_turn, dice_sum=players_tenatative_new_position - players_current_pos)
            r += 1 # increment the number of steps move
    # snake encountered
    if players_tenatative_new_position!=players_confirmed_new_position and players_tenatative_new_position > players_confirmed_new_position:
        print(f"Snake encountered : value of r = {r}")
        while r != players_tenatative_new_position - players_confirmed_new_position:
            Xpos, Ypos = movement(Xpos , Ypos, r, player_turn=player_turn, dice_sum=players_tenatative_new_position - players_current_pos)
            r -= 1 # increment the number of steps move
    
    pygame.display.update()


def snakeorladders(Xpos, Ypos, player_turn):
    Xdif = (ladderendX - Xpos)
    Ydif = (ladderendY -Ypos)
    Xpos += Xdif
    Ypos += Ydif
    coords[player_turn][0] = Xpos
    coords[player_turn][1] = Ypos
    return (Xpos, Ypos)

def game_board_screen(player_count):
    pygame.display.set_caption("Snake and ladder: Game Board Screen")
    current_player = 1
    run=True
    while run:
        screen.blit(background_image, background_image_rect)  # Draw background
        # display_players(player_count)
        # display_pawns(player_count=player_count)

      

        display_roll_message(current_player)
        draw_board()  # Draw board label
        #draw_leader()  # Draw leaderboard label

          #load all players onto board # from gayatri
        screen.blit(pawn1, (coords[0][0], coords[0][1]))
        screen.blit(pawn2, (coords[1][0], coords[1][1]))
        screen.blit(pawn3, (coords[2][0], coords[2][1]))
        screen.blit(pawn4, (coords[3][0], coords[3][1]))
        # Draw buttons
        roll_dice_button.draw(screen)

        if 'dice1_button' in locals():
            dice1_button.draw(screen)
        if 'dice2_button' in locals():
            dice2_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                display_roll_message(current_player)
                if roll_dice_button.rect.collidepoint(event.pos):
                    print(f"playing for current_player = {current_player}")
                
                    # Roll the dice
                    
                    # dice1 = random.randint(1, 6)
                    # dice2 = random.randint(1, 6)
                    # print(f"Dice roll: {dice1}, {dice2}")
                    dice1, dice2 = dice.roll_dice(player_id=current_player)
                   
                     # Update dice buttons based on the rolled values
                    dice1_button = button.Button(720, 350, dice_images[dice1 - 1], 0.06)
                    dice2_button = button.Button(820, 350, dice_images[dice2 - 1], 0.06)
                    dice_sum = dice1 + dice2

                    screen.blit(background_image, background_image_rect)  # Draw background
                    display_players(player_count)
                    # display_pawns(player_count=player_count)
                    screen.blit(pawn1, (coords[0][0], coords[0][1]))
                    screen.blit(pawn2, (coords[1][0], coords[1][1]))
                    screen.blit(pawn3, (coords[2][0], coords[2][1]))
                    screen.blit(pawn4, (coords[3][0], coords[3][1]))
                    # display_roll_message(current_player)
                    draw_board()  # Draw board label
                    #draw_leader()  # Draw leaderboard label
                    roll_dice_button.draw(screen)
                    dice1_button.draw(screen)
                    dice2_button.draw(screen)
                    pygame.display.update()
                    pygame.time.delay(50)  # Add a delay of 50 milliseconds between frames

                    
                    
                    # Play turn for current player
                    players_current_pos = players.get_player_current_postion(current_player)
                    projected_new_pos, confirmed_new_position = players.play(current_player, dice_sum=dice_sum)
                    
                    print(f"tentative_new_postion = {projected_new_pos}, confirmed_new_position = {confirmed_new_position}")
                    # Move player's piece, handle game logic here # Gayatri to fix below method
                    move_player(current_player,dice_sum=dice_sum, players_current_pos=players_current_pos, players_tenatative_new_position=projected_new_pos, players_confirmed_new_position=confirmed_new_position)
                    
                    # Update players_current_pos
                    players.update_player_current_postion(player_id=current_player)
                    if dice_sum != 12:
                        
                        # print(f"current players is = {current_player}")
                        current_player=find_next_player(current_player, player_count)
                        print(f"next players is = {current_player}")

        pygame.display.update()
        clock.tick(20)  # Limit frame rate to 20 FPS


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
        
        players_list = []

        for event in pygame.event.get():
        #Quit Game
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if select_two_players_button.draw(screen):
                    player_count=2
                    players_dict=players.create_players(2)
                    print(f"players_list = {players_list}")
                if select_three_players_button.draw(screen):
                    player_count=3
                    player_dict = players.create_players(3)
                    # players.create_players(3)
                if select_four_players_button.draw(screen):
                    player_count = 4
                    player_dict = players.create_players(4)
                    # players.create_players(4)
                
                print(f"players_list = {players_list}, player_count = {player_count}")
                players_list = [i+1 for i in range(1, player_count)]
                game_board_screen(player_count)


        pygame.display.update()






#Calling backgroung image
background()    
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

        if play_button.draw(screen):
            print(f"exit")
    pygame.display.update()

# Quit pygame
pygame.quit()

