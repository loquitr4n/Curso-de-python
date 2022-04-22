def metade(n):
    met = n/2
    print(f'A medade de R${n:.2f} é R${met:.2f}')


def dobro(n):
    dob = n * 2
    print(f'O drobro de R${n:.2f} é R${dob:.2f}')


def aumento(n, p=100):
    aum = (n * p/100) + n
    print(f'Aumentando {p}%, temos R${aum:.2f}')


def subtracao(n, p=100):
    sub = n - (n * p/100)
    print(f'Diminuindo {p}% temos R${sub:.2f}')


if __name__ == '__main__':
    metade(200)
    dobro(200)
    aumento(200, 25)
    subtracao(200, 20)
