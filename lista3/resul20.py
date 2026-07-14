n =int(input('Digite um número: '))
if n >= 1 and n < 100:
    digitos = 2
else:
    digitos = 'não é de dois'
if n % 2 == 0:
    ultimo = 'par'
else:
    ultimo = 'ímpar'
print('O número {} tem {} dígitos e é {}.'.format(n, digitos, ultimo))