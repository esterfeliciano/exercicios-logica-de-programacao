##Peça dois números e verifique se a divisão entre eles é exata.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
if n2 != 0:
    if n1 % n2 == 0:
        print("A divisão entre os dois números é exata.")
    else:
        print("A divisão entre os dois números não é exata.")   