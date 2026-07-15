numeros = []

for i in range(5):
    n = float(input('Digite o número: '))
    numeros.append(n)

maior_numero = max(numeros)
menor_numero = min(numeros)
soma_total = sum(numeros)

print('O maior número é o {}.'.format(maior_numero))
print('O menor número é o {}.'.format(menor_numero))
print('A soma total dos 5 números é {}.'.format(soma_total))