class Peca:
    def __init__(self, id, nome, custo, preco, estoque):
        self.id = id
        self.nome = nome
        self.custo = custo
        self.preco = preco
        self.estoque = estoque

pecas = []

def cadastrar_peca():
    nome = input("Nome: ")
    custo = float(input("Custo: "))
    preco = float(input("Preco: "))
    estoque = int(input("Estoque: "))
    nova_peca = Peca(
        id=len(pecas) + 1,
        nome=nome,
        custo=custo,
        preco=preco,
        estoque=estoque
    )
    pecas.append(nova_peca)

def registrar_producao():
    for p in pecas:
        print(p.id, p.nome, p.custo, p.preco, p.estoque)
    id_digitado = int(input("Id da peça: "))
    peca_encontrada = False
    for p in pecas:
        if p.id == id_digitado:
            valor_aumentar = int(input("Insira quanto quer aumentar no estoque: "))
            p.estoque += valor_aumentar
            peca_encontrada = True
            break
    if not peca_encontrada:
        print("Peça não encontrada!")

def vender_peca():
    for p in pecas:
        print(p.id, p.nome, p.custo, p.preco, p.estoque)
    id_digitado = int(input("Id da peça: "))
    peca_encontrada = False
    for p in pecas:
        if p.id == id_digitado:
            valor_venda = int(input("Insira a quantidade que deseja vender: "))
            if valor_venda > p.estoque:
                print("Estoque insuficiente!")
            else:
                p.estoque -= valor_venda
            peca_encontrada = True
            break
    if not peca_encontrada:
        print("Peça não encontrada!")

# Teste
cadastrar_peca()
for p in pecas:
    print(p.id, p.nome, p.custo, p.preco, p.estoque)

registrar_producao()
for p in pecas:
    print(p.id, p.nome, p.estoque)

vender_peca()
for p in pecas:
    print(p.id, p.nome, p.estoque)
