def escrever_arquivo(texto):
    arquivo = open('texto.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(texto):
    arquivo = open('texto.txt', 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


if __name__ == '__main__':
    atualizar_arquivo('oi')
    ler_arquivo('texto.txt')
    ler_arquivo('texto.txt')



