# Escreva dois numeros na tela e compare-os, mostrando na tela uma mensagem?
# O primeiro valor é maior.
# O segundo valor é maior.
# Nao existe valor maior, os dois são iguais.

print('=-'*40)
print('      COMPARADOR DE NUMEROS')
print('=-'*40)

a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))

if a > b:
    print('O primeiro valor é maior')
elif a < b:
    print('O segundo valor é maior')
else:
    print('Nao existe valor maior, os dois são iguais.')