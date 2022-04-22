from datetime import datetime


def idade(ano):
    b = datetime.now().year
    idd = b - a
    return idd


a = int(input('Em que ano você nasceu? '))
Idade = idade(a)
if 18 <= Idade <= 60:
    print(f'Com {Idade} anos: VOTO OBRIGATÓRIO.')
if Idade < 18:
    print(f'Com {Idade} anos: NÃO VOTA.')
if Idade > 60:
    print(f'Com {Idade} anos: VOTO OPCIONAL')