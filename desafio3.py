saldo_inicial = 2000.00
operacao = input("qual operacao voce ira realizar?")

if operacao == "depositar":
    depositar = float(input("qual o valor que voce quer depositar? R$: "))
    if depositar > 0.00: 
        valor_final = saldo_inicial + depositar
        print("saldo atual:", valor_final)

elif operacao == "sacar":
    sacar = float(input("qual valor voce quer sacar? R$: "))
    if (sacar > 0.00 and saque >= saldo_inicial) or saque == 100.00:
        valor_final = saldo_inicial - sacar

elif operacao == "extrato":
    print("seu saldo é:", saldo_inicial) 
    valor_final = saldo_inicial
    print("seu saldo agora é: ", valor_final)