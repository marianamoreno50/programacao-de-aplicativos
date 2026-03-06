temperatura = float(input("digite a temperatura atual :"))
if temperatura <= 30:
    print("clima estavel")
else:
    print("temperatura elevada! checando umidade")

umidade = float(input("digite a umidade da estufa: "))
if umidade > 40: 
    print("ligar irrigacao")
else:
    print("ligar apenas os ventiladores")