from operator import truediv
from CampoGravitacional import CampoGravitacional
from ListaAstros import ListaAstros
from Astro import Astro
from Vetor import Vetor
import pygame, sys
from pygame.locals import *


class SistemaSolar:
    ##-----main-----##
    
    def __init__(self,janela) -> None:
        #-----Criacao dos astros
        #-----A massa esta em unidades de massas terrestres, bem como a distancia
        self.lista = ListaAstros()
        Astro.setJanela(janela)

        Sol = Astro("Sol",Vetor(0,0),Vetor(0,0),Vetor(0,0),333000)
        Mercurio = Astro("Mercurio",Vetor(0.38607,0),Vetor(0,0),Vetor(0,0),0.6)
        Venus  = Astro("Venus",Vetor(0.72133,0),Vetor(0,0),Vetor(0,0),0.815)
        Terra  = Astro('Terra',Vetor(1,0),Vetor(0,0),Vetor(0,0),1)
        Marte  = Astro('Marte',Vetor(1.5196,0),Vetor(0,0),Vetor(0,0),0.107)
        Jupter  = Astro('Jupter',Vetor(5.18887,0),Vetor(0,0),Vetor(0,0),317.83)
        Saturno  = Astro('Saturno',Vetor(9.52933,0),Vetor(0,0),Vetor(0,0),95.159)
        Urano  = Astro('Urano',Vetor(19.2066,0),Vetor(0,0),Vetor(0,0),14.536)
        Netuno  = Astro('Netuno',Vetor(30.02867,0),Vetor(0,0),Vetor(0,0),17.147)
        Plutao  = Astro('Plutao',Vetor(39.48,0),Vetor(0,0),Vetor(0,0),0.0022)
        #----Adicao dos astros a lista
        self.lista.adicionar(Sol)
        self.lista.adicionar(Mercurio)
        self.lista.adicionar(Venus)
        self.lista.adicionar(Terra)
        self.lista.adicionar(Marte)
        self.lista.adicionar(Jupter)
        self.lista.adicionar(Saturno)
        self.lista.adicionar(Urano)
        self.lista.adicionar(Netuno)
        self.lista.adicionar(Plutao)

        self.campoG = CampoGravitacional(self.lista)
        self.campoG.velocidadeInicial()


    def atualizar(self):
        self.campoG.atualizar()

    def desenhar(self):
        self.lista.desenhar()
