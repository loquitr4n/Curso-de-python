#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida 
# com uma contagem por extenso, de zero até vinte. Seu programa deverá ler 
# um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove',
'vinte')

while True:
    extenso = int(input('Digite um numero entre 0 e 20: '))
    if extenso > 20 or extenso < 0:
        print('Informação invalida, tente novamente.')
    if 0 <= extenso <= 20:
        print(f'Você digitou o numero {num[extenso]}')
        continuar = input('Deseja continuar? [S/N] ').lower()[0]
        if continuar == 'n':
            print('Obrigado, volte sempre.')
            break

