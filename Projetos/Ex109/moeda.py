def metade(n=0, inf=False):
    met = n/2
    return met if inf is False else moeda(met)


def dobro(n=0, inf=False):
    dob = n * 2
    return dob if inf is False else moeda(dob)


def aumento(n=0, p=100, inf=False):
    aum = (n * p/100) + n
    return aum if inf is False else moeda(aum)


def subtracao(n=0, p=100, inf=False):
    sub = n - (n * p/100)
    return sub if inf is False else moeda(sub)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


if __name__ == '__main__':
    print(f'{metade(200)}')
    print(f'{dobro(200)}')
    print(f'{subtracao(200, 50)}')
    print(f'{subtracao(200, 20)}')

