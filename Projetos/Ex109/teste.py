from Ex109 import moeda

num = float(input('\033[0;30;42mDigite o preço: R$\033[m'))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
porc = float(input('Taxa: '))
print(f'Aumentando {porc}% temos {moeda.aumento(num, porc, True)}')
print(f'Diminuindo {porc}% temos {moeda.subtracao(num, porc, True)}')
