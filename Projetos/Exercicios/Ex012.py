# Faça um programa que leia o preço de um produto e mostre seu novo
# preço com 5% de desconto.

produto = int(input('Digite o preço do produto: '))

# Aqui vamos calcular 5% do produto

novo_preço = produto - (produto * 5/10)

print('O produto com desconto de 5% custa: {}'.format(novo_preço))
