import pygame
import sys
from pygame import mixer

#practice run to see if mute functionality works or not using pygames mixer

pygame.init()

# display
width, height = 1000, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mute Button")

# colours, rgb values
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

mixer.music.load('background_music.mp3')
mixer.music.play(-1) #the -1 allows the music to play on loop

def mute():
    mixer.music.pause()
def unmute():
    mixer.music.unpause()

#drawing the mute button
def draw_mutebutton():
    pygame.draw.rect(screen, red, (150, 50, 100, 50))
    font = pygame.font.Font(None, 36)
    text = font.render("Mute", True, white)
    screen.blit(text, (170, 60))

#drawing the unmute button
def draw_unmutebutton():
    pygame.draw.rect(screen, red, (450, 50, 100, 50))
    font = pygame.font.Font(None, 36)
    text = font.render("Unmute", True, white)
    screen.blit(text, (460, 60))

#loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            button_rect_mute = pygame.Rect(150, 50, 100, 50)
            if button_rect_mute.collidepoint(mouse_pos):
                mute()

            button_rect_unmute = pygame.Rect(450, 50, 100, 50)
            if button_rect_unmute.collidepoint(mouse_pos):
                unmute()

    screen.fill(black)
    draw_mutebutton()
    draw_unmutebutton()

    pygame.display.flip()