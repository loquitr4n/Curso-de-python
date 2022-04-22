class Calculadora:

    def soma(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


if __name__ == '__main__':
    calculadora = Calculadora()
    print(calculadora.soma(10, 3))
    print(calculadora.sub(10, 2))
    print(calculadora.mult(3, 4))
    print(calculadora.div(100, 10))
