nomes = []

while True:
    nome = input("Digite um nome (ou 'sair' para encerrar): ").strip()
    
    if nome.lower() == "sair":
        break
    
    nomes.append(nome)

nomes.sort()
print("Lista ordenada:", nomes)
