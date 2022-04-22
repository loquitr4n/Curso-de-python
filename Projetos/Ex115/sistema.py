from Ex115.Lib.interface import *
from Ex115.Lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        n = str(input('Digite o nome: '))
        i = leiaInt('Digite a idade: ')
        cadastrar(arq, n, i)
    elif resp == 3:
        cabecalho('SAINDO DO SISTEMA, ATE LOGO!')
        sleep(1.5)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)