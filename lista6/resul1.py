## Desafio 01 - Validador de Triângulo
##
## Enunciado:
## Dado três números inteiros positivos a, b e c, represente os comprimentos de três lados.
## 
## Você deve determinar se esses lados podem formar um triângulo válido, e se sim, classificá-lo como:
## - Equilátero (todos os lados iguais),
## - Isósceles (dois lados iguais),
## - Escaleno (todos os lados diferentes).
## 
## Se os lados não puderem formar um triângulo, retorne a string "Não é um triângulo".
## 
## Regras para formar um triângulo:
## Os valores a, b, c formam um triângulo se:
## - a < b + c
## - b < a + c
## - c < a + b
## 
## Entrada:
## Três números inteiros positivos a, b e c.
## 
## Saída:
## Uma string que será:
## - "Equilátero"  
## - "Isósceles"  
## - "Escaleno"  
## - ou "Não é um triângulo"
## 
## Exemplos:
## - Exemplo 1: a = 3, b = 3, c = 3 -> "Equilátero"
## - Exemplo 2: a = 3, b = 4, c = 5 -> "Escaleno"
## - Exemplo 3: a = 1, b = 2, c = 3 -> "Não é um triângulo"
## - Exemplo 4: a = 2, b = 2, c = 3 -> "Isósceles"

a =int(input('Digite o lado a do triâgulo: '))
b =int(input('Digite o lado b do triângilo: '))
c =int(input('Digite o lado c do triângulo :'))

## conferindo o lado a
if a < b + c:
    ladoA = True
else:
    ladoA = False

## conferindo o lado b
if b < a + c:
    ladoB = True
else:
    ladoB = False

## conferindo o lado c
if c < a + b:
    ladoC = True
else:
    ladoC = False

## vendo se é um triangulo válido
if ladoA == True and ladoB == True and ladoC == True:
   ladosV = True
else:
    ladosV = False

## classificando só se for um triângulo válido
if ladosV == True:
    if a == b and b == c:
        print('O triângulo é equilátero.')
    elif a == b or a == c or b == c:
        print('O triângulo é isóceles.')
    else:
        print('O triâgulo é escaleno.')
else:
    print('Não é um triângulo.')