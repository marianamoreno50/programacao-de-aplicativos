nivel = int(input("digite seu nivel"))
quantidade_de_esfera = float(input("digite a quantidade de esfera"))

if nivel >= 20 and quantidade_de_esfera >= 50:
    print("habilidade super salto desbloqueada!")
elif nivel < 20 and quantidade_de_esfera < 50:
    print("requisitos insuficiente para nova habilidade")