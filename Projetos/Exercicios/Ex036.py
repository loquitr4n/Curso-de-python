# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo q ela não pode exceder 30% do salario ou entao o emprestimo
# será negado.
print('=-'*40)
casa = float(input('Qual o valor da casa? ')) # Valor da casa
salario = float(input('Qual o salário do comprador? ')) # Salário do comprador
time = int(input('Em quantos anos será parcelado? ')) # Tempo de pagamento (em anos)
entrada = int(input('Vai ter algum valor de entrada? (se não, digite 0) '))
valor_real_a_pagar = casa - entrada
mensalidade = valor_real_a_pagar/(time*12)
print(mensalidade)#Valor das parcelas
print('=-'*40)
if mensalidade < (30/100 * salario):
    print('Seu emprestimo foi APROVADO!!!')
else:
    print('Seu emprestimo foi NEGADO!!!')
print('=-'*40)
juros = casa * 0.85/100 * time * 12
print('Irá pagar no final das contas um total de {:.1f} de juros'.format(juros))
print('=-'*40)