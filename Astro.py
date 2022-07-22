from audioop import mul
from Vetor import Vetor
import pygame, sys
from pygame.locals import *

multiplicadorJanela = 50


class Astro:
    #Posteriormente tem-se que colocar representacoes graficas
    #entao imagino que aqui ira as mesmas
    
    #atributo que guarda a janela onde os atros vao se desenhar
    janela = None
    def __init__(self,nome,pos = Vetor(0,0),vel = Vetor(0,0),ace = Vetor(0,0),mas = 0) -> None:
        self.posicao = pos
        self.velocidade = vel
        self.aceleracao = ace
        self.massa = mas
        self.nome = nome
        self.imagem = pygame.image.load('./Astros/'+nome+'.png')
    
    def desenhar(self):
        if (Astro.janela != None):
            Astro.janela.blit(self.imagem,(int(self.posicao.x*multiplicadorJanela),int(self.posicao.y*multiplicadorJanela) + 540))

    @classmethod
    def setJanela(cls,window):
        cls.janela = window
