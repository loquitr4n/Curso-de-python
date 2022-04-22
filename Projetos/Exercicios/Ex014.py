# Vamos fazer um conversor de temperaturo de graus celsius para farenheint.

c = float(input('Digite a temperatura em graus celsius: '))
f = (9*c/5) + 32

print('{:.1f}°C em fareheint é {:.1f}°F'.format(c,f))

