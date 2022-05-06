import pandas as pd

arquivo = r'C:\Users\Família\Desktop\Douglas\Curso de excel\Boletim.xlsx'
tabela = pd.read_excel(arquivo)


def media(bim):
    notas = []
    for i in tabela[bim]:
        notas.append(i)
    notas.pop()
    media_do_bimestre = f'{sum(notas)/len(notas):.2f}'
    return media_do_bimestre


print(f'{media("Primeiro bim")}'), print(f'{media("Segundo bim")}'), print(f'{media("Terceiro bim")}'), print(f'{media("Quarto bim")}')

# nomes = []
# notas1 = []
# notas2 = []
# notas3 = []
# notas4 = []
# for nome in tabela['Nome do aluno']:
#     nomes.append(nome)
# for nota in tabela['Primeiro bim']:
#     notas1.append(nota)
# for nota in tabela['Segundo bim']:
#     notas2.append(nota)
# for nota in tabela['Terceiro bim']:
#     notas3.append(nota)
# for nota in tabela['Quarto bim']:
#     notas4.append(nota)
#
# nomes.pop()
# notas4.pop()
# notas3.pop()
# notas2.pop()
# notas1.pop()
# media_pb = f'{sum(notas1)/len(notas1):.2f}'
# media_sb = f'{sum(notas2)/len(notas2):.2f}'
# media_tb = f'{sum(notas3)/len(notas3):.2f}'
# media_qb = f'{sum(notas4)/len(notas4):.2f}'
# print(media_pb)
# print(media_sb)
# print(media_tb)
# print(media_qb)

