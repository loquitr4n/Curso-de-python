# Ajuda interativa:

# Digite no python console "help()".
# Digite qualquer função no console para obter ajuda.
# Para sair do help() digite quit().
# podemos utilizar o help(função) tambem.
# ou podemos tbm utlizar o print((input.__doc__)).

# Docstring:

# Para documentar uma função, utilizamos as docstrings para fazer um manual das funções (def) que (criarmos)
# ex:


def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela.
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    Criador: Gustavo Guanabara
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


contador(1, 10, 2)
help(contador)

# Parametros opcionais:

# Serve para caso existir um parametro que pode ou nao existir.
# EX:


def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


soma(2, 3)

# podemos pular um parametro opcional caso nao queiramos inserir o 'a' por exemplo:

soma(b=3, c=4)

# Escopo de uma variavel:

#EXEMPLO:


def teste():
    x = 8
    print(f'Na função teste n = {n}')
    print(f'Na função teste x = {x}')


# PROGRAMA PRINCIPAL
n=2
print(f'Na função principal, n vale {n}')
teste()
# print(f'No programa principal, x = {x}') --> Dará erro pois 'x' nao esta definido no program principal,
# e sim no na função teste()

# X é uma variavel local, pois só existe dentro da função teste()
# N é uma variavel global, pois existe em todo programa




