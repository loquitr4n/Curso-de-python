if False:
    def area(l, c):
        área = l * c
        print(f'A área de um terreno de {l} x {c} é de  {área}m².')


    print(f'{"<< CONTROLE DE TERRENOS >>":^50}')
    print('-' * 50)
    resp = ''
    while resp != 'N':
        area(
            float(input('Digite a largura (m): ')),
            float(input('Digite o comprimento (m): '))
        )
        while True:
            resp = str(input('Deseja continuar? [S/N] ')).upper()
            if resp in 'NS':
                break
            print('ERRO! Digite somente S ou N.')
        print()


# Modo do professor:

def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg}x{comp} é  de {a}m²')


print(f'{"Controle de Terrenos":^40}')
print('-' * 40)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)