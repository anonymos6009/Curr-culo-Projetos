import pygame
import sys
import random

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("happy`s laboratory")
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    tela.fill((255, 255, 255))
    pygame.display.flip()

    

