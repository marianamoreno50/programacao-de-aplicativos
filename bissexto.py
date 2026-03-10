ano = int(input("digite o ano: "))

if(ano% 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"o ano {ano} e bisexto")
else:
    print(f"o ano {ano} e comum")
    
