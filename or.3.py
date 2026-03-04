usuario = input("digite seu usuario: ")
senha = int(input("digite sua senha: "))

if (usuario == "adimin" or usuario == "root") and senha == 1234:
    print("acesso liberado")

else:
    print("acesso negado")