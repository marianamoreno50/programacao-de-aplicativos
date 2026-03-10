codigo = int(input("coloque o codigo do pacote: "))
peso = float(input("digite o peso: "))

if peso < 5 and(codigo  % 10 == 0):
    print(f"pacote {codigo}: {}")