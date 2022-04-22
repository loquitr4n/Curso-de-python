def leiaInt(msg='0'):
    while True:
        try:
            a = int(input(msg))
        except (TypeError, ValueError):
            print('\033[1;31mERRO! Tipagem invalida, digite um valor INTEIRO valido.\033[m')
            continue
        else:
            return a


def leiaFloat(msg='0'):
    while True:
        try:
            b = float(input(msg))
        except (TypeError, ValueError):
            print('\033[1;31mERRO! Tipagem invalida, digite um valor REAL válido.\033[m')
            continue
        else:
            return b


if __name__ == '__main__':
    a = leiaInt('Digite um valor inteiro: ')
    b = leiaFloat('Digite um valor real: ')
    print(f'O valor inteiro inserido foi {a} e o valor real {b}')




