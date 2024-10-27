import pygame
import random


class Ball:
    def __init__(self, radius):
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.image.fill((255, 255, 255))  # Fill the surface with white
        self.radius = radius
        self.rect = self.image.get_rect(center=(800 // 2, 800 // 2))

    def drawCharacter(self):
        pygame.draw.circle(self.image, (0,0,0), (self.radius, self.radius), self.radius)
    
    def movement(self):
        pass






