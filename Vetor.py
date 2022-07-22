import math

class Vetor:
    #------------------------------------------------
    def __init__(self,xn,yn):
        self.x = xn
        self.y = yn
    #------------------------------------------------
    def modulo(self):
        return math.sqrt((self.x**2) + (self.y**2))
    #------------------------------------------------
    def distanciaPontoB(self,B):
        return math.fmod(self.x - B.x , self.y - B.y)
    #------------------------------------------------
    def vetorUnitario(self):
        v = Vetor(self.x,self.y)
        hipotenusa = Vetor.modulo()
        v.x = v.x/hipotenusa
        v.y = v.y/hipotenusa
        return v
    #------------------------------------------------
    def vetorUnitarioParaB(self,B):
        v = Vetor(B.x - self.x,B.y - self.y)
        return v.vetorUnitario()

