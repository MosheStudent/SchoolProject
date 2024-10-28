import pygame
import random


class Ball (pygame.sprite.Sprite):
    def __init__(self, radius, pos):
        super().__init__()

        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255,255,255),(radius, radius), radius)

        self.rect = self.image.get_rect(center = pos)
        self.speed = [random.randint(-10, 10), random.randint(-10,10)]


    def update(self):

        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]






