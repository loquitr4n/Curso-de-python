# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz.

a = int(input('Digite um numero:'))

b = a * 2
c = a * 3
d = a **(1/2)

#print('O dobro de {} é {}, seu triplo é {}, e a raiz é {:.2f}'.format(a,b,c,d))

#Tambem podemos escrever desta forma:

print('O dobro de {} é {}, seu triplo é {}, e a raiz é {:.2f}'.format(a,(a*2),(a*3),pow(a,(1/2))))
