n = int(input("Quantos termos de Fibonacci você quer ver? "))

a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b