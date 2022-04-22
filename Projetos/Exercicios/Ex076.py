#Exercício Python 076:Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos 
#preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('{:=^50}'.format(' LOJA DO DG '))
prod = ('Lapis:', 2.50 , 'Caneta:', 3.00, 'Caderno:', 15.00,'Lapiseira:', 7.50, 'Mochila:', 70.00, 
        'Estojo:',5.00,'Fichário:', 45.99, 'Folha A4:', 9.99, 'Compasso:', 7.00,'Transferidor:', 4.00)

for n in range(0,len(prod), 2):
    print(f'{prod[n]:_<40}',f'R${prod[n+1]:>7.2f}')
print('='*50)    