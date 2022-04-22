# Verifique se existe a palavra "Silva" no meio do nome de alguem.

name = input('Qual seu nome todo? ').lower().split()
print('Seu nome tem silva? {}'.format('silva' in name[1:-1]))