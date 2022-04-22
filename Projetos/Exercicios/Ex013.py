# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo
# salário com 15% de aumento.

# Salário anterior:

salario = float(input('Salário anterior: '))

# Calculo:

aumento = salario + (salario*(15/100))

# Novo salário:

print('Novo salário: {}'.format(aumento))
