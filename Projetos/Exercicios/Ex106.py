from time import sleep


# def ajuda():
#     while True:
#         frase('SISTEMA DE AJUDA PYHELP')
#         a = input('Função ou biblioteca: ').lower()
#         if a == 'fim':
#             frase('ATE LOGO!!!')
#             break
#         frase(f'Acessando o Manual do Comando "{a}"')
#         sleep(1)
#         help(a)
#
#
# ajuda()

# Resolução do professor

c = [
    '\033[m',         # 0 - sem cores
    '\033[0;30;41m',  # 1 - vermelho
    '\033[0;30;42m',  # 2 - verde
    '\033[0;30;43m',  # 3 - amarelo
    '\033[0;30;44m',  # 4 - azul
    '\033[0;30;45m',  # 5 - roxo
    '\033[0;30;46m',  # 6 - azul turqueza
    '\033[0;30;47m',  # 7 - branco
    '\033[0;30;47m'   # 8 - cinza
    ]


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', cor=3)
    print(c[7], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=6):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# Programa principal


if __name__ == '__main__':
    comando = ''
    while True:
        titulo('Sistema de Ajuda PyHELP', cor=5)
        comando = str(input('Função ou biblioteca: '))
        if comando.upper() == 'FIM':
            break
        else:
            ajuda(comando)
    titulo('ATE LOGO!!!', 1)
