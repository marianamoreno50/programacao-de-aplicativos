cidades = ["Sao Paulo", "Rio de Janeiro", "Curitiba", "belo Horizonte"]
tarefa = input("digite alguma cidade")

if tarefa in cidades:
    posicao = cidades.index(tarefa)
    print(f"a cidade {tarefa} esta na posicao {posicao}")
else:
    print(f"a {tarefa} nao foi encontrada")