cargo = input("seu cargo: ")
codigo = int(input("seu codigo: "))
botao_emergncia = input("s/n: ")
epi = input("EPI completo? s/n: ")

if (cargo == "engenheiro" or "tecnico") and (codigo == 1234 or botao_emergencia == "s" ) and epi == "s": 
    print("acesso liberado")

else:
    print("acesso negado risco de seguranca")
    
