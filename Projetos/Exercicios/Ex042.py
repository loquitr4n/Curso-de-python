from math import fabs
print('='*40)
print('       ANALISADOR DE TRIÂNGULOS')
print('='*40)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if fabs(b-c) < a < b + c and fabs(a-c) < b < a + c and fabs(c-b) < c < c + b:
    print('Os segmentos acima podem formar um triangulo.')
    if a == b == c: # podemos tbm escrever "if a==b and b==c"
        print('Esse triangulo é equilatero!')
    elif a != b != c != a:
        print('Esse triangulo é escaleno!')
    else: # poderiamos escrever "elif a == b and b != c or a == c and c != b or b == c and b != a:"
        # deixamos sempre o mais dificil para colocar no else, pq nao precisa fazer a condição.
        print('Esse triangulo é isosceles!')
else:
    print('Os segmentos acima NÃO formam um triangulo.')