import math
from ListaAstros import ListaAstros
from Vetor import Vetor


class CampoGravitacional:

    #para que o sistema se mova mais rapido
    multiplicador = 0.000001
    #Caso seja necess'ario passar para valores reais
    #altere as costantes aqui
    constanteG = 0.01
    massaTerra = 1
    distanciaTerra = 1

    def __init__(self,lista) -> None:
        self.sistemaPlanetario = lista


    #chame apenas a funcao atualizar
    def calcular(self):
        assert self.sistemaPlanetario, "Sistema Planetario vazio."

        iterador = self.sistemaPlanetario.inicio
        forca = Vetor(0,0)
        fModulo = 0.0

        while iterador:
            astr = iterador.elemento
            forca = Vetor(0,0)
            fModulo = 0.0
            iterador2 = self.sistemaPlanetario.inicio
            #Calculo de forca gravitacional sobre o astro astr
            while iterador2:
                astro2 = iterador2.elemento
                #para nao considerar a forca sobre o proprio astro, distancia zero iria dar problemas
                if iterador2.elemento != astr:
                    #valores necessarios para o calculo da forca
                    distancia = Vetor((astro2.posicao.x - astr.posicao.x)*self.distanciaTerra,(astro2.posicao.y - astr.posicao.y)*self.distanciaTerra)
                    disModulo = distancia.modulo()
                    cosseno = distancia.x/disModulo
                    seno = distancia.y/disModulo
                    #calculo da forca
                    fModulo = (astro2.massa*astr.massa*self.constanteG)
                    fModulo = fModulo / (disModulo**2)
                    forca.x += fModulo*cosseno
                    forca.y += fModulo*seno
                iterador2 = iterador2.proximo

            astr.aceleracao.x = self.multiplicador*forca.x/astr.massa
            astr.aceleracao.y = self.multiplicador*forca.y/astr.massa
            iterador = iterador.proximo


    #Esta funcao calcula a forca resultante sobre o astro que foi passado no parametro
    #Consideracoes importantes, os valores seram proporcionais aos valores reais
    #(massa, posicao), mas para simplificar G = 1.
    def atualizar(self):
        iterador = self.sistemaPlanetario.inicio
        self.calcular()
        while iterador:
            astr = iterador.elemento
            astr.velocidade.x += astr.aceleracao.x
            astr.velocidade.y += astr.aceleracao.y
            astr.posicao.x += astr.velocidade.x
            astr.posicao.y += astr.velocidade.y
            iterador = iterador.proximo

    def velocidadeInicial(self):
        self.calcular()
        iterador = self.sistemaPlanetario.inicio
        while iterador:
            astr = iterador.elemento
            mult = 1
            if(astr.aceleracao.x < 0):
                mult = -1
            astr.velocidade.y = math.sqrt(astr.aceleracao.x*astr.posicao.x*mult)
            iterador = iterador.proximo