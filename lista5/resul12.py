n = int(input("Quantos números você vai digitar? "))

maior_par = None
menor_impar = None

for i in range(n):
    numero = int(input(f"Digite o número {i+1}: "))
    
    if numero % 2 == 0:
        if maior_par is None or numero > maior_par:
            maior_par = numero
    else:
        if menor_impar is None or numero < menor_impar:
            menor_impar = numero

print(f"Maior par: {maior_par}")
print(f"Menor ímpar: {menor_impar}")