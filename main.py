import pygame
from pygame.locals import *
from sys import exit
import Character
import Ball


pygame.init()

screen_Width = 500
screen_Hieght = 500

screen = pygame.display.set_mode((screen_Width, screen_Hieght))
pygame.display.set_caption("PONG")

char = Character.Character(30, 100, 50, 0)
ball = Ball.Ball(20, (screen_Width, screen_Hieght))

allsprites = pygame.sprite.Group()
allsprites.add(ball)
allsprites.add(char)


clock = pygame.time.Clock()
while True:
    screen.fill((0,0,0))

    allsprites.draw(screen)
    allsprites.update()



    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pygame.display.flip()
    clock.tick(60)