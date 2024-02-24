#Importing modules
import pygame 
import sys

# Window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1200
FPS = 60

#Defining classes and variables
class Game:
    #initialising variables
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        #Clock time to control FPS
        self.clock = pygame.time.Clock()

        self.gamestatemanager = Gamestatemanager("start")
        #instances of screens
        self.start = Start(self.screen, self.gamestatemanager)
        self.level = Level(self.screen, self.gamestatemanager)
        
        #Dictionary to map changes made to states of screen
        self.states = {"start": self.start, "level": self.level}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Check for mouse click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #Change state to the next one
                    current_state = self.gamestatemanager.get_state()
                    if current_state == "start":
                        self.gamestatemanager.set_state("level")
                    elif current_state == "level":
                        self.gamestatemanager.set_state("start")

            #Logic of current state
            self.states[self.gamestatemanager.get_state()].run()
            
            #Update display
            pygame.display.update()
            self.clock.tick(FPS)


class Level:
    def __init__(self, display, gamestatemanager):
        self.display = display
        self.gamestatemanager = gamestatemanager

    def run(self):
        #Call 1st screen
        self.display.fill((0, 0, 255))  # Fill with blue
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.gamestatemanager.set_state("start")

#Stub for screens
class Start:
    def __init__(self, display, gamestatemanager):
        self.display = display
        self.gamestatemanager = gamestatemanager

    def run(self):
        self.display.fill((255, 0, 0))  # Fill with red

class Gamestatemanager:
    def __init__(self, currentstate):
         self.currentstate = currentstate

    def get_state(self):
        return self.currentstate #get current state

    def set_state(self, state):
        self.currentstate = state #set current state

if __name__ == "__main__":
    game = Game()
    game.run()

