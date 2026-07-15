lista_temporaria =[]

for i in range(10):
    n =int(input('digite o {} múmero: ' .format(i+1)))
    lista_temporaria.append(n)
numeros =list(lista_temporaria)
impares =[]
pares =[]

for n in numeros:
    if n % 2 != 0:
        impares.append(n)
    else:
        pares.append(n)

print('Os número ímpares são: {}' .format(impares))
print('Os números pares são :{}' .format(pares))