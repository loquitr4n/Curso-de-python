# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante '
# a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        a = str(input(msg)).strip()
        if a.isnumeric():
            valor = int(a)
            ok = True
            return valor
        else:
            print('\033[0;31mERRO! Digite um numero inteiro válido.\033[m')


# Programa principal

if __name__ == '__main__':
    n = leiaint('Digite um numero: ')
    print(f'Voce acabou de digitar o numero {n}.')
