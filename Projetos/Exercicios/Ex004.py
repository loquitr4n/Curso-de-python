# Crie um programa que digite algo e mostre as especificações

a = input('Digite algo:')

print('O tipo primitivo desse valor é' , type(a))
print('Só tem espaços?', a.isspace())
print('Sé tem numero?' , a.isnumeric())
print('É alfabético?' , a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Esta em maiuscula?' , a.isupper())
print('Está em minuscula?' , a.islower())
print('Esta capitalizada?' , a.istitle())