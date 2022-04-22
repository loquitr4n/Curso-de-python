from Ex110 import moeda

num = float(input('\033[0;30;42mDigite o preço: R$\033[m'))
aum = float(input('\033[0;30;43mTaxa de aumento: \033[m'))
sub = float(input('\033[0;30;43mTaxa de redução: \033[m'))
moeda.resumo(num, aum, sub)
