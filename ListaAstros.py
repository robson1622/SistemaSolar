from Astro import Astro

class No:
    #-----------------------------------------------
    def __init__(self,elem=None,prox=None):
        self.elemento = elem
        self.proximo = None


class ListaAstros:
    #-----------------------------------------------
    def __init__(self) -> None:
        self.inicio = None
    #-----------------------------------------------
    def adicionar(self,astr):
        novo = No(astr)
        novo.proximo = self.inicio
        self.inicio = novo

    def desenhar(self):
        iterador = self.inicio
        while iterador:
            astr = iterador.elemento
            astr.desenhar()
            iterador = iterador.proximo
        

