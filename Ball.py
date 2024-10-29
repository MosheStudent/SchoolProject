import pygame
import random
import Character

pygame.mixer.init()
clock = pygame.time.Clock()
wallSound = pygame.mixer.Sound("wall.mp3")
deathSound = pygame.mixer.Sound("die.mp3")


class Ball (pygame.sprite.Sprite):
    def __init__(self, radius, pos):
        super().__init__()
        self.screen_wid = pos[0]
        self.screen_hie = pos[1]

        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255,255,255),(radius, radius), radius)

        self.rect = self.image.get_rect(center = (self.screen_wid//2, self.screen_hie//2))
        self.speed = [random.randint(-10, 10), random.randint(-10, 10)]


    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.topleft[0] <= 0:
            self.speed[0] *= -1
            wallSound.play()

        if self.rect.topright[0] >= self.screen_wid:
            self.speed[0] *=-1
            wallSound.play()

        if self.rect.topright[1] <= 0:
            self.speed [1] *= -1 
            wallSound.play()

        if self.rect.bottomleft[1] >= self.screen_hie:
            self.speed[1] *= -1
            wallSound.play()
        
    def end(self, Character):
        if self.rect.bottomleft [0] < Character.rect.bottomright[0] - 10:
            #deathSound.play()
            pass



        








