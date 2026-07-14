##Verifique se dois números têm o mesmo sinal (ambos positivos ou negativos).
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
if (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
    print("Os dois números têm o mesmo sinal.")     
    