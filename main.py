from SistemaSolar import SistemaSolar
import pygame, sys
from pygame.locals import *

LARGURA = 1920
ALTURA = 1080


pygame.init()

janela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Simulacao Sistema Solar - By git.../robson1622')
pygame.display.set_icon(pygame.image.load("./Astros/logo.png"))

cor = (23,1,23)

sistema = SistemaSolar(janela)

while True: # Loop unico e principal
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    janela.fill(cor)
    sistema.atualizar()
    sistema.desenhar()
    pygame.display.update()