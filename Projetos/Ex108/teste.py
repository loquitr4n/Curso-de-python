import moeda

num = float(input('\033[0;30;42mDigite o preço: R$\033[m'))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
porc = float(input('Taxa: '))
print(f'Aumentando {porc}% temos {moeda.moeda(moeda.aumento(num, porc))}')
print(f'Diminuindo {porc}% temos {moeda.moeda(moeda.subtracao(num, porc))}')
