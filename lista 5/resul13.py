qtd_alunos = int(input("Quantos alunos há na sala? "))

aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(qtd_alunos):
    nota = float(input(f"Nota do aluno {i+1}: "))
    
    if nota >= 7:
        aprovados += 1
    elif nota >= 5:
        reprovados_recuperacao = True  # apenas ilustrativo, veja nota abaixo
        recuperacao += 1
    else:
        reprovados += 1

print(f"Aprovados: {aprovados}")
print(f"Em recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")