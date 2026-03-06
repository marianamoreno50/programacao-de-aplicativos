print ("inspetor de qualidade")
comprimento = input("digite se o comprimento esta entre 10cm ou 12cm, responda com s/n: ")

if comprimento == "s":
    largura = input("digite se a largura esta entre 5cm ou 6cm, responda com s/n: ")
    if largura == "s":
        print("peca aprovada")
    else:
        print("reprovado, peca invalida")
else:
    print("reprovado, peca invalida")