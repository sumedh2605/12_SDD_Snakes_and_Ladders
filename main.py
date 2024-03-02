import pygame

pygame.init()

screen = pygame.display.set_mode((700, 700)) #changed

grid = []
for i in range (649, -51, -70):#y coordinate changed
    row = []
    for j in range (19, 719, 70):#x coordinates changed
        row.append((j,i))
    grid.append(row)

ladders = {71: 92,
           61: 82,
           56: 75,
           36: 77,
           9: 30,
           6: 17}

snakes = {97: 78,
          95: 56,
          88: 38,
          62: 18,
          32: 10,
          35: 5}

# stubs
projected_positon = 6
confirmed_position = 17
dice_sum = 13
ladderstartX, ladderstartY = grid[0][8]
ladderendX, ladderendY = grid[4][7]
snakestartX, snakestartY = grid[3][4]
snakeendX, snakeendY = grid[1][2]
turn = 0 #whose turn it is



#converts board number to dictionary coord


# loads all images and starting coordinates
pawn1 = pygame.image.load(r'images/pawn.png')
pawn1 = pygame.transform.scale(pawn1, (32,32))
Xg1, Yg1 = 0, 0
Xone, Yone = grid[Xg1][Yg1]
pawn2 = pygame.image.load(r'images/pawn2.png')
pawn2 = pygame.transform.scale(pawn2, (32,32))
Xg2, Yg2 = 0, 0
Xtwo, Ytwo = grid[Xg2][Yg2]
pawn3 = pygame.image.load(r'images/pawn3.png')
pawn3 = pygame.transform.scale(pawn3, (32,32))
Xg3, Yg3 = 0, 0
Xthree, Ythree = grid[Xg3][Yg3]
pawn4 = pygame.image.load(r'images/pawn4.png')
pawn4 = pygame.transform.scale(pawn3, (32,32))
Xg4, Yg4 = 0, 0
Xfour, Yfour = grid[Xg4][Yg4]

#lists for convinience
pawns = [pawn1, pawn2, pawn3, pawn4]
coords = [[Xone, Yone],[Xtwo, Ytwo], [Xthree, Ythree], [Xfour,Yfour]]
gridcoord = [[Xg1, Yg1],[Xg2,Yg2],[Xg3,Yg3],[Xg4,Yg4]]


resized = [False, False, False, False]
X_board = 0

def movement(X, Y, X_board):
    if position < projected_positon:
        pygame.display.update()
        if Y == 1 or Y == 3 or Y == 5 or Y == 7 or Y == 9:  # switch direction every other row
            X -= 1
            if X < 0:
                X = 0
                Y -= 1
            X_board = (10-X)
            print (X)
            print (X_board)
        else:
            X += 1
            X_board = X
            if X > 9:  # border to go up one row
                X = 9
                X_board = (10-X)
                Y += 1
        gridcoord[turn][0], gridcoord[turn][1] = X, Y
    return(X,Y, X_board)

def snakeorladders(Xpos, Ypos):
    if position in ladders:
        new_position = ladders[position]
    elif position in snakes:
        new_position = snakes[position]
    Ypos = int(new_position / 10)
    Xpos = int(new_position % 10)
    coords[turn][0] = Xpos
    coords[turn][1] = Ypos
    return Xpos, Ypos


#Game loop
running = True
while running:
    clock = pygame.time.Clock()
    clock.tick(3)

    #load all players onto board
    screen.blit(pawn1, (coords[0][0], coords[0][1]))
    screen.blit(pawn2, (coords[1][0], coords[1][1]))
    screen.blit(pawn3, (coords[2][0], coords[2][1]))
    screen.blit(pawn4, (coords[3][0], coords[3][1]))

    Xpos = gridcoord[turn][0]
    Ypos = gridcoord[turn][1]

    position = Ypos * 10 + X_board

    # call function to move correct player across the board
    Xpos, Ypos, X_board = movement(Xpos, Ypos, X_board)
    coords[turn][0], coords[turn][1] = grid[Ypos][Xpos]


    if position in ladders and position == projected_positon or position in snakes and position == projected_positon:
        Xpos, Ypos = snakeorladders(Xpos, Ypos)
        coords[turn][0], coords[turn][1] = grid[Ypos][Xpos]
    pygame.display.update()



    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False