media_escolar = float (input("digite sua media"))
renda_familiar = float (input("digite sua renda familiar"))
escola = input ("voce veio de escola publica? s/n")

if media_escolar > 8.0 and (renda_familiar < 2000.00 or escola == "s"):
    print("voce ganhou a bolsa")

elif media_escolar > 8.0 and (renda_familiar == 2000.00 or escola == "n"):
    print("voce nao ganhou a bolsa")