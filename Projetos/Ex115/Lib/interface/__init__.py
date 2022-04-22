from Exercicios.Ex113 import leiaInt


def leiaInt(msg='0'):
    while True:
        try:
            a = int(input(msg))
        except (TypeError, ValueError):
            print('\033[1;31mERRO! Tipagem invalida, digite um valor INTEIRO valido.\033[m')
            continue
        else:
            return a


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for i in lista:
        print(f'{cont} - {i}')
        cont += 1
    linha()
    opc = leiaInt('\033[1;33mSua opção: \033[m')
    return opc

