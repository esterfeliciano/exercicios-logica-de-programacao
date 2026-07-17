votos = {1: 0, 2: 0, 3: 0, 4: 0}

while True:
    voto = int(input("Digite o voto (1 a 4, ou -1 para encerrar): "))
    
    if voto == -1:
        break
    elif voto in votos:
        votos[voto] += 1
    else:
        print("Voto inválido!")

for candidato, total in votos.items():
    print(f"Candidato {candidato}: {total} votos")