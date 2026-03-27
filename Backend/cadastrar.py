class Produto:
    def __init__(self, id, nome, custo, preco, estoque):
        self.id = id
        self.nome = nome
        self.custo = custo
        self.preco = preco
        self.estoque = estoque
        self.data = data

produtos = []

def cadastrar_produto():
    
    nome = input("Nome: ")
    custo = input("Custo: ")
    preco = input("Preco: ")
    estoque = input("Estoque: ")
    novo_produto = Produto(
        id = len(produtos) + 1,
        nome = nome,
        custo = custo,
        preco = preco,
        estoque = estoque,
    )
    produtos.append(novo_produto)



cadastrar_produto()

for p in produtos:
    print(p.id, p.nome, p.custo, p.preco, p.estoque)
