# ============================================================
# DIA 18 — RETORNAR MÚLTIPLOS VALORES EM UMA FUNÇÃO
# ============================================================

# Exercício 18.1 — Analisar produto
def analisar_produto(preco, quantidade):

    valor_total = preco * quantidade
    total = valor_total

    quantidade_recebida = quantidade
    estoque = quantidade_recebida

    return total, estoque

total, estoque = analisar_produto(40, 5)

print(total, estoque)


# Exercício 18.2 — Calcular o preço médio
def calcular_media(preco1, preco2):
    soma = preco1 + preco2
    media = soma / 2

    if preco1 > preco2:
        maior = preco1
    else:
        maior = preco2

    return media, maior

media, maior = calcular_media(40, 60)

print(media, maior)


# Exercício 18.3 — Analisar uma venda
def analisar_venda(preco, quantidade):
    total_venda = preco * quantidade
    valor_total = total_venda
    quantidade_vendida =  quantidade

    return valor_total, quantidade_vendida

valor_total, quantidade_vendida = analisar_venda(35, 4)

print(valor_total, quantidade_vendida)


# Exercício 18.4 — Calcular o saldo do estoque
def atualizar_estoque(estoque_atual, quantidade_vendida):
    estoque_restante = estoque_atual - quantidade_vendida
    estoque_atualizado = estoque_restante
    quantidade = quantidade_vendida

    return estoque_atualizado, quantidade

estoque_atualizado, quantidade = atualizar_estoque(20, 4)

print(estoque_atualizado, quantidade)


# Exercício 18.5 — Fechamento do Dia 18
def registrar_venda(preco, quantidade, estoque_atual):
    total_venda = preco * quantidade
    estoque_restante = estoque_atual - quantidade

    return total_venda, estoque_restante

total_venda, estoque_restante = registrar_venda(25, 3, 10)

print(total_venda, estoque_restante)