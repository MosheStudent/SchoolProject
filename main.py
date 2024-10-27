import pygame
from pygame.locals import *
from sys import exit
import Character


pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PONG")

char = Character.Character(30, 100, 50, 0)



while True:
    screen.fill((0,0,0))

    char.drawCharacter(screen)
    char.movement()

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pygame.display.update()