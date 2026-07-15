lista_temporaria = []

for i in range (3):
    n =int(input(f'Digite o {i+1} número:'))
    lista_temporaria.append(n)
numeros =tuple(lista_temporaria)
print(f'A tupla foi criada:{numeros}')