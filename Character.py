import pygame

class Character:
    def __init__(self, sizeW, sizeH, positionX, positionY):
        self.shape = pygame.Rect(positionX, positionY, sizeW, sizeH)
        

        self.positionX = positionX
        self.positionY = positionY
        self.sizeW = sizeW
        self.sizeH = sizeH

    def drawCharacter(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.shape) 

    def movement(self):
        px, py = pygame.mouse.get_pos()

        self.positionY = py
        self.shape.center = (self.positionX, self.positionY)