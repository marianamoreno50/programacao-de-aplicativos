vagas = ["Ocupado", "Livre", "Ocupado", "Livre"]
usuario = int(input("digite um numero entre 0 e 3"))

if usuario % 2 == 0 and vagas[usuario] == ("livre"):
    print("vaga liberada")
else:
    print("vaga ocupada")