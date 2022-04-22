def metade(n=0):
    met = n/2
    return met


def dobro(n=0):
    dob = n * 2
    return dob


def aumento(n=0, p=100):
    aum = (n * p/100) + n
    return aum


def subtracao(n=0, p=100):
    sub = n - (n * p/100)
    return sub


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


if __name__ == '__main__':
    print(f'{metade(200)}')
    print(f'{dobro(200)}')
    print(f'{subtracao(200, 50)}')
    print(f'{subtracao(200, 20)}')

