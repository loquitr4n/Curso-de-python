#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

num = soma = cont = 0
num = int(input('Digite um valor [digite 999 p/ parar]: '))
while True:
    cont += 1
    soma += num
    num = int(input('Digite um valor [digite 999 p/ parar]: '))
    if num == 999:
        break
print('Você digitou {} e a soma dos numeros digitados é {}.'.format(cont,soma))