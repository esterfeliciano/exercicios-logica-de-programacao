##Crie um dicionário com 4 nomes e notas de alunos. Calcule e mostre a média geral da turma.
nota_alunos = {}

for i in range(4):
    print('Aluno {}' .format(i+1))
    nome =str(input('Digite o nome: '))
    nota =float(input('Digite a nota:'))

    nota_alunos[nome]=nota

soma_total = sum(nota_alunos.values())
media = soma_total/5

print('A média da turma é {}. ' .format(media))