from calculator import Calculadora

class Televisao:
    def __init__(self):
        self.ligada = True
        self.canal = 1

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def subir_canal(self, a):
        if self.ligada:
            self.canal += a

    def descer_canal(self, a):
        if self.ligada:
            self.canal -= a


if __name__ == '__main__':
    televisao = Televisao()
    televisao.power()
    televisao.power()
    televisao.subir_canal(20)
    televisao.descer_canal(15)
    print(televisao.ligada)
    print(televisao.canal)

calculadora = Calculadora()
print(calculadora.mult(3, 4))
