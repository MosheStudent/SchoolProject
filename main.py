import pygame
from pygame.locals import *
from sys import exit
import Character
import Ball


pygame.init()
pygame.mixer.init()

paddleSound = pygame.mixer.Sound("Paddle.mp3")



screen_Width = 500
screen_Hieght = 500

icon = pygame.image.load("Empty.png")

pygame.display.set_icon(icon)
screen = pygame.display.set_mode((screen_Width, screen_Hieght))
pygame.display.set_caption("PONG")

char = Character.Character(30, 100, 50, 0)
ball = Ball.Ball(20, (screen_Width, screen_Hieght), 10)

allsprites = pygame.sprite.Group()
allsprites.add(ball)
allsprites.add(char)


clock = pygame.time.Clock()
while True:
    screen.fill((0,0,0))

    allsprites.draw(screen)
    allsprites.update() 
    ball.end(char)

    if char.rect.colliderect(ball):
        if ball.speed[0] < 0: 
            ball.speed [0] *=-1


        paddleSound.play()
    
    if ball.end(char):
        exit()




    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pygame.display.flip()
    clock.tick(60)