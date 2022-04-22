'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = dict()                                                          # Dicionario
lista = list()                                                          # Lista
idades = []                                                             # Lista das idades consultadas
mulheres = []                                                           
validacao = ''
while validacao != 'n':
    dados['Nome'] = str(input('Nome: '))
    while True:                                                         # Validação a saber do sexo. 
        sexo = str(input('Sexo: [M/F] ')).lower()
        if sexo in 'mf':
            break
        print('Dado incorreto. Por favor, digite somente M ou F.')
    dados['Idade'] = int(input('Idade: '))
    idades.append(dados['Idade'])
    dados['Sexo'] = sexo
    if sexo == 'f':
        mulheres.append(dados['Nome'])
    lista.append(dados.copy())
    while True:                                                         # Validação se pode continuar ou nao.
        validacao = str(input('Deseja continuar? [S/N]')).lower()
        if validacao in 'ns':
            break
        print('Opção incorreta, por favor digite apenas S ou N.')
media = sum(idades)/len(lista)                                          # Calculo da média das idades
print()
print('=x'*40)
print()
print(f'A) Ao todo foram cadastradas {len(lista)} pessoas.')            # Quantidade de pessoas cadastradas   
print(f'B) A média de idade é {media} ')                                # Media das idades
print(f'C) As mulhereres cadastradas foram {mulheres}')
print('Lista das pessoas que estao a cima da média: ')
for p in range(0,len(lista)): # Criei uma variavel p para rodar toda lista, logo após um if com cada item da lista na key='idade' teria q ser maior que a média.
    if lista[p]['Idade'] > media:
        print(f'Nome = {lista[p]["Nome"]}; Sexo = {lista[p]["Sexo"]}; Idade = {lista[p]["Idade"]} ')
print()
print('<<<ENCERRADO>>>')
print()