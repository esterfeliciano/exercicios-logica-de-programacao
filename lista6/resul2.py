## Desafio 02 - Classificador de Pontuação de Prova
##
## Enunciado:
## Sistema para classificar o desempenho de um aluno em uma prova com
## 4 questões, cada uma valendo no máximo 25 pontos. Receba os valores
## inteiros q1, q2, q3, q4 (notas de cada questão) e classifique:
## - "Inválido" se qualquer nota for negativa ou maior que 25.
## - "Reprovado" se a soma for menor que 50.
## - "Regular" se a soma estiver entre 50 e 74 (inclusive),
##   mas nenhuma das notas for zero.
## - "Bom" se a soma estiver entre 75 e 89 (inclusive), e pelo menos
##   uma das questões tiver nota máxima (25).
## - "Excelente" se a soma for 90 ou mais, e nenhuma nota for menor que 20.
## - "Desempenho indefinido" se nenhuma condição acima se aplicar.

notas = []

for i in range(4):
    nota = int(input(f"Digite a nota da questão {i+1}: "))
    notas.append(nota)

soma = sum(notas)

if any(nota < 0 or nota > 25 for nota in notas):
    print("Inválido")
elif soma >= 90 and min(notas) >= 20:
    print("Excelente")
elif 75 <= soma <= 89 and 25 in notas:
    print("Bom")
elif 50 <= soma <= 74 and 0 not in notas:
    print("Regular")
elif soma < 50:
    print("Reprovado")
else:
    print("Desempenho indefinido")