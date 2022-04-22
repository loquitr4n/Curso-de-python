# Desenvolva uma logica que calcule o IMC e imprima o resultado de acordo com a tabela abaixo:
# menor que 18.5 : abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 ate 40: obesidade
# acima de 40: obesidade morbida

print('{:=^40}'.format(' CALCULO DE IMC '))

peso = float(input('Digite o peso (em quilos): '))
altura = float(input('Digite a altura (em metros): '))
imc = peso/altura**2
print(f'Seu IMC é de {imc:.2f}')

if imc < 18.5:
    print('IMC abaixo de 18.5: Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('IMC entre 18.5 e 25: Peso ideal!')
elif 25 <= imc < 30:
    print('IMC entre 25 e 30: Sobrepeso!')
elif 30 <= imc < 40:
    print('IMC entre 30 e 40: Obesidade!')
elif imc >= 40:
    print('IMC acima de 40: Obesidade mórbida!')