import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))

grid = []
for i in range (750, 0, -75):#y coordinate
    row = []
    for j in range (0, 750, 75):#x coordinates
        row.append((j,i))
    grid.append(row)

# stubs
projected_positon = 8
confirmed_position = 13
dice_sum = 8
ladderstartX, ladderstartY = grid[0][8]
ladderendX, ladderendY = grid[4][7]
snakestartX, snakestartY = grid[3][4]
snakeendX, snakeendY = grid[1][2]
turn = 1 #whose turn it is



#converts board number to dictionary coord
Y = int(confirmed_position/10)
X = int(confirmed_position%10)

# loads all images and starting coordinates
pawn1 = pygame.image.load(r'images/pawn.png')
Xone, Yone = grid[0][0]
pawn2 = pygame.image.load(r'images/pawn2.png')
Xtwo, Ytwo = grid[0][0]
pawn3 = pygame.image.load(r'images/pawn3.png')
Xthree, Ythree = grid[0][0]
pawn4 = pygame.image.load(r'images/pawn4.png')
Xfour, Yfour = grid[0][0]

#lists for convinience
pawns = [pawn1, pawn2, pawn3, pawn4]
pawn_names = ['1','2','3','4']
coords = [[Xone, Yone],[Xtwo, Ytwo], [Xthree, Ythree], [Xfour,Yfour]]

r=0

resized = [False, False, False, False]

def movement(X, Y, d):
    if d < dice_sum:
        pygame.display.update()
        if Y == 675 or Y == 525 or Y == 375 or Y == 225 or Y == 75:  # switch direction every other row
            X -= 75
        else:
            X += 75

        if X > 675:  # border to go up one row
            X = 675
            Y -= 75
        if X < 0:
            X = 0
            Y -= 75
        coords[turn][0] = X
        coords[turn][1] = Y
    return(X,Y)

def snakeorladders(Xpos, Ypos):
    Xdif = (ladderendX - Xpos)
    Ydif = (ladderendY -Ypos)
    Xpos += Xdif
    Ypos += Ydif
    coords[turn][0] = Xpos
    coords[turn][1] = Ypos
    return (Xpos, Ypos)


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

    Xpos = coords[turn][0]
    Ypos = coords[turn][1]


    # call function to move correct player across the board
    Xpos, Ypos = movement(Xpos , Ypos, r)
    if r != dice_sum:
        r += 1 # increment the number of steps move


    # call function to move player on a ladder
    if (Xpos, Ypos) == (ladderstartX, ladderstartY) and r == dice_sum:
        Xpos, Ypos = snakeorladders(Xpos, Ypos)
    if (Xpos, Ypos) == (snakestartX, snakestartY) and r == dice_sum:
        Xpos, Ypos = snakeorladders(Xpos, Ypos)
    pygame.display.update()



    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
