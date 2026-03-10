senha = input("digite a sua senha: ")
tentativas = int(input("qunatas tentativas foram?: "))
token = input("voce possui algum token? (s/n): ")

if senha == "admin123"and (tentativas % 3 == 0 or token == "s"):
    print(f"Tentativa nº {tentativas}: ACESSO CONCEDIDO")
else:
    print(f"Tentativa nº {tentativas}: ACESSO BLOQUEADO POR PROTOCOLO")