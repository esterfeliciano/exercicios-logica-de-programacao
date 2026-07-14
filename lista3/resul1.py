n1 =float(input("Digite o primeiro número: "))
if n1 < 0:
    n1 = 'negativo'
elif n1 == 0:
    n1 = 'zero'
else:
    n1 = 'positivo'
print('O numero é {}'.format(n1))