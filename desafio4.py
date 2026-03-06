drone = int(input("digite o codigo do drone: "))
autorizacao = input("possui alguma autorizacao da torre? s/n: ")

if drone == 999 or autorizacao == "s":
    print("pouso autorizado")

  
    bateria = int(input("digite a bateria do drone"))
    clima = input("digite o clima: ")
    velocidade = int(input("digite a velocidade do vento"))

    if bateria < 10:
        print("autorize o pouso imediatamente!")

    elif bateria >= 10:
        if (clima == "ensolarado" or velocidade < 30) or (clima == "chuvoso" and velocidade < 10):
                print("pouso autorizado: iniciando descida")
        else:
            print("pouso negado: Condicoes meteriologicas muito perigosas") 
else: 
        print("ERRO 1: Drone nao identificado. Retornando a base")
