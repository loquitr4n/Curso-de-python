from time import sleep


def temp(a, b, c):
    if c < 0:
        c = c * -1
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {c} em {c}: ')
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += c
        print(f'{"<< FIM!!! >>":^20}')
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= c
        print(f'{"<< FIM >>":^20}')


# Programa principal:

if __name__ == '__main__':
    print('-x' * 20)
    temp(0, 10, 1)
    print('-x' * 20)
    temp(10, 0, 2)
    print('-x' * 20)
    print('Agora é sua vez de personalizar a contagem: ')
    print('-' * 40)
    temp(int(input('Inicio: ')),
         int(input('Fim:     ')),
         int(input('Passo:   ')))
