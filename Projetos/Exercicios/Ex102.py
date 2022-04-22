# Programa principal:

def fatorial(n=1, show=False):
    '''
    -> Calculo de fatorial
    :param n: N° a ser calculado o fatorial
    :param show: Mostrar ou não a memoria de calculo
    :return: fatorial de n
    '''
    f = 1
    print('-' * 30)
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f = f * c
    return f


print(f'{fatorial(int(input("Digite um numero: ")), True)}')
help(fatorial)
print('-' * 30)
