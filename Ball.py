import pygame
import random
import math

pygame.mixer.init()
clock = pygame.time.Clock()
wallSound = pygame.mixer.Sound("wall.mp3")
deathSound = pygame.mixer.Sound("die.mp3")


class Ball (pygame.sprite.Sprite):
    def __init__(self, radius, pos, speedVector):
        super().__init__()
        self.screen_wid = pos[0]
        self.screen_hie = pos[1]

        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255,255,255),(radius, radius), radius)

        self.rect = self.image.get_rect(center = (self.screen_wid//2, self.screen_hie//2))

        #makes constant speed vector: 

        speedlist = [-1, 1]

        self.speedX1 = random.randint(-(speedVector -1), -4)
        self.speedX2 = random.randint(4 , (speedVector - 1))

        speedxlist = [self.speedX1, self.speedX2]

        self.speedX = random.choice(speedxlist)
        self.speedCoefficient = random.choice(speedlist)



        self.speed = [self.speedX, int (self.speedCoefficient * math.sqrt((speedVector**2 - self.speedX**2)))]






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
        if self.rect.bottomleft[0] <= 3: 
            return True


        








