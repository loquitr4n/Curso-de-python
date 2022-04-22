# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# a vista no dinheiro/cheque = 10% de desconto
# a vista no cartao 5% de desconto
# ate 2x no cartão, preço normal
# 3x ou mais no cartão, 20% de juros

print('=-'*40)
print('                             CALCULE SEU DESCONTO')
print('=-'*40)


preço = float(input('Qual o preço do produto? '))
forma_de_pagamento = input('Qual a forma de pagamento? ').lower().strip()
if 'cartao' in forma_de_pagamento:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas == 1:
        print('Preço a pagar R${}.'.format(preço - (5/100 * preço)))
    elif parcelas == 2:
        print('Preço a pagar: R${}.'.format(preço))
    elif parcelas >= 3:
        print('Preço a pagar: {}.'.format(preço + (20/100 * preço)))
elif 'dinheiro' or 'cheque' in forma_de_pagamento:
    print('Preço a pagar: R${}.'.format(preço - (preço*10/100)))

