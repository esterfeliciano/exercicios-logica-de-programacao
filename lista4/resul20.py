pessoas = {}

while True:
    nome = input("Digite um nome (ou 'sair' para encerrar): ").strip()
    
    if nome.lower() == "sair":
        break
    
    idade = int(input("Digite a idade: "))
    pessoas[nome] = idade

pessoa_mais_velha = max(pessoas, key=pessoas.get)

print(f"A pessoa mais velha é {pessoa_mais_velha}, com {pessoas[pessoa_mais_velha]} anos")