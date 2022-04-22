def lerDinheiro(msg):
    """
    -> Tratamento de dados para numeros float
    :param msg: Mesagem de input
    :return: retorna o float da entrada do input(msg)
    """
    val = False
    while not val:
        a = str(input(msg)).replace(',', '.').strip()
        if a.isalpha():
            print(f'\033[2;31mERRO! "{a}" É UMA ENTRADA INVALIDA.\033[m')
        elif a.strip() == '':
            print('\033[0;31mNenhuma entrada encontrada\033[m.')
        else:
            val = True
            return float(a)


def leiaint(msg):
    """
    -> Tratamento de dados para numeros inteiros
    :param msg: menssagem de input
    :return: retorna o n° inteiro da entrada do input(msg)
    """
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