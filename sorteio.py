usuario = int(input("digite o id do usuario: "))
valor = float(input("digite o valor da compra: "))

if usuario % 2 == 0 and valor > 500.00:
    print(f"parabens usuario {usuario}! Voce ganhou um cupo, para sua compra de R${valor}")
else:
        print(f"obrigada pela compra, usuario {usuario}. Continue acopanhado as promocoes")