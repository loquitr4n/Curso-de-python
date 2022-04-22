# Faça um programa que leia a largura e a altura de uma parede em metros
# Calcule a sua área e a quantidade de tinta necessária para pinta-la.
# Sabendo que cada litro de tinta pinta uma área de 2m^2.

# Aqui vamos inserir a altura e largura da parede:

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

# Aqui vamos calcular a área:

area = altura * largura

print('Área da parede: {}m²'.format(area))

# Quantidade de tinta necessária:

tinta = area/2

print('Litros de tinta necessária: {} Litros'.format(tinta))