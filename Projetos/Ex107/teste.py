import moeda

num = float(input('\033[0;30;42mDigite o preço: R$\033[m'))
moeda.metade(num)
moeda.dobro(num)
porc = float(input('Taxa: '))
moeda.aumento(num, porc)
moeda.subtracao(num, porc)
