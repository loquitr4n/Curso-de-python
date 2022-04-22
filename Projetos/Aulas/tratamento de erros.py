# Tratamento de erros:
try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possivel fazer divisão por zero.')

except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados.')

except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}')

else:
    print(f'O resultado foi {r}')

finally:
    print('Obrigado, volte sempre!')