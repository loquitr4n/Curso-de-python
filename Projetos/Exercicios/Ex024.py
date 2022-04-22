# Pergunte a cidade que em que vc nasceu, e se a cidade tiver o nome "santo", responda verdadeiro, se não,
# responda falso.

city = input('A sua cidade se inicia com santo? ') .lower().split()[0]
print(city == 'santo')

# teste split('/')
# data = input('Qual a data do seu aniverssário? ').split('/')
# print(f' Dia {data[0]} \n Mês {data[1]} \n Ano {data[2]}')