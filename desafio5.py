quantidades = int(input("qunatas garrafas passaram pela esteira hoje?: "))

if quantidades == 500:
    print("HORA DA LIMPEZA, parea maquina")
    print("QUALIDADE, retire a amostra para o teste")

if quantidades % 500 == 0:
    print("HORA DA LIMPEZA, pare a maquina")

elif quantidades % 100 == 0:
    print("QUALIDADE, retire a amostra para teste")
 
else:
    print(f"produção em dia. Garrafa numero {quantidades} processada")