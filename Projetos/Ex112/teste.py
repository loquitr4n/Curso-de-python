from Ex112.UtilidadesCEV import moeda
from Ex112.UtilidadesCEV import dados

num = dados.lerDinheiro('\033[1;32mDigite o preço: \033[m')
aum = dados.lerDinheiro('\033[1;32mTaxa de aumento:\033[m ')
sub = dados.lerDinheiro('\033[1;32mTaxa de redução:\033[m ')
moeda.resumo(num, aum, sub)
