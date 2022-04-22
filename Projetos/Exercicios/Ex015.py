# Escreva um program que pergute a quantidade de km percorridas por um carro
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dia = int(input('Alugou o carro por quantos dias? '))
km = float(input('Qual a quilometragem percorrida? '))

preço_a_pagar = dia * 60.0 + km * 0.15

print('O preço a pagar pelo aluguel do carro é: R${:.2f}'.format(preço_a_pagar))

