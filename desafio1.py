nome_cliente = input ("digite seu nome")
valor_total = float(input("digite o valor total da compra"))
distancia_entrega = int(input("digite a distancia da entrega"))
cupom = (input("digite o seu cupom"))
frete = 40.00

if valor_total >= 1000.00 and cupom == "S":
    desconto = valor_total * 0.20
    total= valor_total - desconto
    ("parabens! Voce ganhou um mousepad gamer de brinde!")
elif valor_total > 500.00 and valor_total < 1000.00 and cumpom == "S":
    desconto = valor_total * 0.10
    total = valor_total - desconto 

         
if distancia_entrega <= 50 and valor_total > 200.00:
    frete = 0.00
    valor_final = valor_total + frete
else:
    valor_final = valor_total + frete 

print("nome do cliente" , nome_cliente)
print("valor total da compra" , valor_total)
print("valor do desconto" , cupom)
print("valor final a pagar" , valor_total)
