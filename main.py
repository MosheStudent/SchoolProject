import pygame
from pygame.locals import *
from sys import exit
import Character
import Ball


pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PONG")

char = Character.Character(30, 100, 50, 0)
ball = Ball.Ball(40, (50,50))

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