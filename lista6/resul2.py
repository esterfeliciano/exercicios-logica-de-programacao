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
##
## Entrada: quatro números inteiros q1, q2, q3, q4.
## Saída: string representando o desempenho do aluno.
##
## Exemplo 1: q1=20, q2=25, q3=20, q4=25  -> "Excelente"
## Exemplo 2: q1=25, q2=25, q3=25, q4=10  -> "Bom"
## Exemplo 3: q1=10, q2=15, q3=20, q4=5   -> "Regular"
## Exemplo 4: q1=25, q2=25, q3=25, q4=26  -> "Inválido"
## Exemplo 5: q1=0, q2=25, q3=25, q4=25   -> "Reprovado"