# ============================================================
# DIA 16 — FUNÇÕES APLICADAS A LISTAS DE DICIONÁRIOS
# ============================================================

# Lista de produtos utilizada nos exercícios
produtos = [
    {"nome": "Fone", "preco": 85.00, "estoque": 10},
    {"nome": "Mouse", "preco": 60.00, "estoque": 5},
    {"nome": "Teclado", "preco": 120.00, "estoque": 8}
]

# Exercício 16.1 — Buscar produto pelo nome
def buscar_produto(produtos, nome_busca):
    for produto in produtos:
        if nome_busca.lower() ==  produto['nome'].lower():
            print(f"Nome do produto: {produto['nome']} - Preço: R$ {produto['preco']} - Estoque: {produto['estoque']}")
            break
    else:
        print("Produto não encontrado")

# Exercício 16.2 — Calcular o valor total do estoque
def calcular_valor_estoque(produtos):

    soma = 0

    for produto in produtos:
        total = produto['preco'] * produto['estoque']
        soma += total

    print(f"Valor total: R$ {soma:.2f}")
    

# Exercício 16.3 — Listar produtos com estoque baixo
def listar_produtos_baixo_estoque(produtos):
    for produto in produtos:
        if produto['estoque'] < 6:
            print(f"Produto: {produto['nome']} - Estoque {produto['estoque']}")


# Exercício 16.4 — Calcular o valor do estoque baixo
def calcular_valor_estoque_baixo(produtos):

    soma = 0

    for produto in produtos:
        if produto['estoque'] < 6:
            total = produto['preco'] * produto['estoque']
            soma += total

    print(f"Valor total: R$ {soma:.2f}")


# Chamando as funções
buscar_produto(produtos, "Mouse")
calcular_valor_estoque(produtos)
listar_produtos_baixo_estoque(produtos)
calcular_valor_estoque_baixo(produtos)