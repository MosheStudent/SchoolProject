import pygame

class Character (pygame.sprite.Sprite):
    def __init__(self, sizeW, sizeH, positionX, positionY):
        super().__init__()

        self.image = pygame.Surface((sizeW, sizeH))
        self.image.fill((255,255,255))
        
        self.rect = self.image.get_rect(center=(positionX, positionY))

    def update(self):
        px, py = pygame.mouse.get_pos()

        self.rect.centery = py

