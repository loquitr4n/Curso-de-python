def metade(n=0, inf=False):
    met = n/2
    return met if inf is False else moeda(int(met))


def dobro(n=0, inf=False):
    dob = n * 2
    return dob if inf is False else moeda(int(dob))


def aumento(n=0, p=100, inf=False):
    aum = (n * p/100) + n
    return aum if inf is False else moeda(int(aum))


def subtracao(n=0, p=100, inf=False):
    sub = n - (n * p/100)
    return sub if inf is False else moeda(int(sub))


def moeda(n=0, style='R$'):
    return f'{style}{n:.2f}'.replace('.', ',')


def resumo(n=0, aum=0, sub=0):
    print(f'{"-" * 40}\n{"RESUMO DO VALOR".center(40)}\n{"-" * 40}')
    print(f"Preço analisado:         \t{moeda(n)}")
    print(f"Dobro do preço:         \t{moeda(dobro(n))}")
    print(f"Metade do preço:         \t{moeda(int(metade(n)))}")
    print(f"{aum}% de aumento:         \t{aumento(n, aum, inf=True)}")
    print(f"{sub}% de redução:         \t{subtracao(n, sub, inf=True)}")


if __name__ == '__main__':
    print(f'{metade(200)}')
    print(f'{dobro(200)}')
    print(f'{subtracao(200, 50)}')
    print(f'{subtracao(200, 20)}')
