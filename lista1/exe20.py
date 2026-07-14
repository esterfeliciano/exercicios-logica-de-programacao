numero = int(input('Digite um número: '))
if numero % 3 == 0 and numero % 5 == 0:
    print('O número {} é múltiplo de 3 e de 5 ao mesmo tempo.'.format(numero))
else:
    print('O número {} não é múltiplo de 3 e de 5 ao mesmo tempo.'.format(numero))