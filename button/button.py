import pygame

#Button class
class Button:
    def __init__(self,x,y,image, scale):
        width = image.get_width()
        height = image.get_height()
        self.iamge = pygame.transform.scale(image, (width*scale, height*scale))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        # self.text_rect = self.text.get_rect(center)
        
    # def draw(self, surface):
    #     surface.blit(self.image, (self.rect.x, self.rect.y))
    def update(self, screen):
        # if self.image is not None:
        screen.blit(self.image, self.rect)
        # screen.blit(self.text, self.text_rect)

    def draw(self, surface):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print(f"clicked and action = true")

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return(action)
    