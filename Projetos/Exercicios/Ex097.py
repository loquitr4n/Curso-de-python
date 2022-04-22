def frase(fr):
    tam = len(fr) + 4
    print('~' * tam)
    print(f'  {fr}')
    print('~' * tam)


if __name__ == '__main__':
    frase(str(input('Digite uma frase: ')))
