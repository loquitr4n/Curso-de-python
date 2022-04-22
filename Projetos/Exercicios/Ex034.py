# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a 1250, calcule um aumento de 10%.
# Para salarios inferiores ou iguais 1250, o aumento é de 15%.

sal = float(input('Digite o salario atual: '))
if sal > 1250:
    new_sal = sal + (sal * 10/100)
if sal <= 1250:
    new_sal = sal + (sal * 15/100)


print(f'Seu salario era de \033[31m{sal}\033[m e passa a ser de \033[32mR${new_sal:.2f}\033[m.')