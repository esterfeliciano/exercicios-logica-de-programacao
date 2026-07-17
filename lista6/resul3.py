## Desafio 03 - Sistema de Avaliação de Risco para Empréstimo
##
## Enunciado:
## Sistema de avaliação de risco para concessão de empréstimos, com
## base em quatro critérios do solicitante:
## - idade (inteiro em anos)
## - salario_mensal (float em mil reais)
## - tempo_emprego (inteiro em meses)
## - possui_dividas (booleano: true ou false)
##
## Regras:
## - Se qualquer critério for inválido (idade < 18 ou > 100, salário < 0,
##   tempo_emprego < 0), retorne "Dados inválidos".
## - Se possui_dividas for true e tempo_emprego for menor que 12 meses,
##   risco é "Alto".
## - Se salario_mensal for menor que 2 e tempo_emprego menor que 6,
##   risco é "Alto".
## - Se idade estiver entre 18 e 25 e salario_mensal for menor que 3,
##   risco é "Moderado".
## - Se idade for maior que 60 e tempo_emprego for menor que 24,
##   risco é "Moderado".
## - Se possui_dividas for true mas tempo_emprego for acima de 36 meses,
##   risco é "Moderado".
## - Se salario_mensal >= 5, tempo_emprego >= 36 e possui_dividas false,
##   risco é "Baixo".
## - Caso nenhuma condição acima seja satisfeita, retorne "Risco Indefinido".
##
## Entrada: idade (int), salario_mensal (float), tempo_emprego (int),
## possui_dividas (booleano).
## Saída: "Alto", "Moderado", "Baixo", "Dados inválidos" ou "Risco Indefinido".
##
## Exemplo 1: idade=22, salario_mensal=2.5, tempo_emprego=10, possui_dividas=false
##            -> "Moderado"
## Exemplo 2: idade=30, salario_mensal=5.5, tempo_emprego=40, possui_dividas=false
##            -> "Baixo"
## Exemplo 3: idade=65, salario_mensal=4.0, tempo_emprego=12, possui_dividas=false
##            -> "Moderado"
## Exemplo 4: idade=27, salario_mensal=1.5, tempo_emprego=3, possui_dividas=true
##            -> "Alto"
## Exemplo 5: idade=17, salario_mensal=2.0, tempo_emprego=6, possui_dividas=false
##            -> "Dados inválidos"

idade =int(input('Digite as sua idade: '))
salario = float(input("Digite o salário (em milhares, ex: 2 para 2000): ")) * 1000
tempo =int(input('Quantos meses você têm de trabalho?'))
dividas = input("Você possuí dividas? (s/n): ").lower().strip()

if dividas in ('s', 'sim', 'yes', 'y', 't', 'true'):
    dividas = True
else:
    dividas = False
## Dados inválidos
if idade < 18 or idade > 100 and salario <= 0 and tempo <= 0:
    print('Dados inválidos para fazer um empréstimo!')
elif dividas == True and tempo < 12:
    print('O risco de fazer um empréstimo é alto!')
elif salario <= 2000 and tempo < 6:
    print('O risco de fazer um emprétimo é alto!')
elif idade <= 18 or idade <= 25 and salario <= 3000:
    print('O risco de fazer um empréstimo é moderado.')
elif idade >= 60 and tempo < 24:
    ('O risco de fazer empréstimo  é moderado')
elif dividas == True and tempo > 36:
    print('O risco de fazer um empréstimo é moderado.')
elif salario >= 5000 and tempo >= 36 and dividas == False:
     print('O risco de fazer um empréstimo é baixo.')
else:
    print('Risco indefinido.')