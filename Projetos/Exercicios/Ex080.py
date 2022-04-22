#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos 
# e cadastre-os em uma lista, já na posição correta de inserção 
# (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for n in range(0,5):
    a = int(input('Digite um valor:'))
    if n == 0 or a > lista[-1]:
        lista.append(a)
        print('O valor foi adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if a <= lista[pos]:
                lista.insert(pos, a)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-'*30)
print(f'Os valores digitados em ordem foram: {lista}')
input('Press anter for continue.')