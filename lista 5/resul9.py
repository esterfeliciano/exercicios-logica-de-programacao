menor_par = None

for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    if numero % 2 == 0:
        if menor_par is None or numero < menor_par:
            menor_par = numero

if menor_par is not None:
    print(f"O menor número par foi: {menor_par}")
else:
    print("Nenhum número par foi digitado.")