# Monte na tela um programa que leia um numero inteiro e mostre na tela seu
# sucessor e seu antecessor.

a = int(input('Digite um numero:'))

b = a + 1
c = a - 1

print('Seu antecessor é {}, e seu sucessor é {}.'.format(c,b))

# Podemos escrever tbm da seguinte forma:

#print('Seu antecessor é {}, e seu sucessor é {}.'.format((a-1),(a+1)))