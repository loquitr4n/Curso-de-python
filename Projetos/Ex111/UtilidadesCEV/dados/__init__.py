from Ex111.UtilidadesCEV import moeda


def leiaDinheiro(msg=''):
    val = int(input(msg))
    if val.isnumeric():
        return moeda.moeda(int(msg))
    elif val.split == '':
        print(f'"{msg}" é um valor invalido')
