# ============================================================
# DIA 19 — RETORNAR MÚLTIPLOS VALORES EM UMA FUNÇÃO
# ============================================================

produtos = [
    {"nome": "Fone", "preco": 85.00, "estoque": 10},
    {"nome": "Mouse", "preco": 60.00, "estoque": 0},
    {"nome": "Teclado", "preco": 120.00, "estoque": 8},
    {"nome": "Monitor", "preco": 700.00, "estoque": 3}
]

def listar_produtos_sem_estoque(produtos):
    for produto in produtos:
        if produto['estoque'] == 0:
            print(f"\nNome do produto com estoque zerado: {produto['nome']}.\n")
listar_produtos_sem_estoque(produtos)

def listar_valor_por_produto(produtos):
    for produto in produtos:
        valor_estoque_produto = produto['preco'] * produto['estoque']
        print(f"\nNome do produto: {produto['nome']} - Valor em estoque: R$ {valor_estoque_produto:.2f}\n")
listar_valor_por_produto(produtos)


# Exercício 19.3 — Calcular o valor total do estoque
def calcular_valor_total_estoque(produtos):
    valor_estoque_total = 0
    for produto in produtos:
        valor_estoque_produto = produto['preco'] * produto['estoque']
        valor_estoque_total += valor_estoque_produto

    return valor_estoque_total

valor_total = calcular_valor_total_estoque(produtos)

print(f"Valor total: R$ {valor_total:.2f}")


# Exercício 19.4 — Encontrar o produto mais caro
def encontrar_produto_mais_caro(produtos):
    maior_preco = produtos[0]['preco']
    nome_maior = produtos[0]['nome']

    for produto in produtos:
        if produto['preco'] > maior_preco:
            maior_preco = produto['preco']
            nome_maior = produto['nome']

    return maior_preco, nome_maior

maior_preco, nome_maior = encontrar_produto_mais_caro(produtos)

print(f"\nNome do produto: {nome_maior} - Preço: R$ {maior_preco:.2f}\n")


# Dia 19 — Exercício 19.5
def gerar_relatorio_estoque(produtos):

    c = 0
    total_estoque = 0

    maior_preco = produtos[0]['preco']
    nome_maior = produtos[0]['nome']

    for produto in produtos:
        total = produto['preco'] * produto['estoque']
        total_estoque += total

        if produto['estoque'] == 0:
            c += 1

        if produto['preco'] > maior_preco:
            maior_preco = produto['preco']
            nome_maior = produto['nome']

    relatorio = {
        "valor_total": total_estoque,
        "sem_estoque": c,
        "produto_mais_caro": nome_maior,
        "preco_mais_caro": maior_preco
    }

    return relatorio

result = gerar_relatorio_estoque(produtos)

print(f"\nValor total do estoque: R$ {result['valor_total']}")
print(f"Quantidade de produtos sem estoque: {result['sem_estoque']}")
print(f"Produto mais caro: {result['produto_mais_caro']} - Preço: R$ {result['preco_mais_caro']:.2f}")