peca_hidraulica = input("digite se concluiu o curso de seguranca com s/n: ")

if peca_hidraulica == "s":
    instrutor = input("o instrutor esta presente? Responda com s/n: ")
    if instrutor == "s":
        print("acesso liberado! Sua operacao foi concluida com")
    else:
         print("espere o instrutor para ele ligar a maquina")
else:
    print("seu acesso foi negado, faca o treinamento antes")