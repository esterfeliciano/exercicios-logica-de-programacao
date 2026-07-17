senha_correta = 1234
tentativas = 3

for tentativa in range(tentativas):
    senha_digitada = int(input("Digite a senha: "))
    
    if senha_digitada == senha_correta:
        print("Senha correta! Acesso liberado.")
        break
    else:
        print("Senha incorreta.")
else:
    print("Número de tentativas excedido. Acesso bloqueado.")