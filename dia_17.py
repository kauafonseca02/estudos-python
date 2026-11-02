# ============================================================
# DIA 17 — FUNÇÕES COM RETURN
# ============================================================

# Exercício 17.1 — Criar função com return para calcular o valor total
def calcular_total(preco, quantidade):
    resultado = preco * quantidade
    return resultado

total = calcular_total(60, 3)

print(total)


# Exercício 17.2 — Retorno de função
def verificar_estoque(quantidade):
    if quantidade < 6:
        res = "Estoque baixo"
    else:
        res = "Estoque suficiente"

    return res

resultado = verificar_estoque(4)

print(resultado)


# Exercício 17.3 — Retorno aplicado ao sistema de vendas
def calcular_desconto(preco):
    if preco >= 100:
        res = preco * 0.10
    else:
        res = 0

    return res

resultado = calcular_desconto(150)

print(resultado)


# Exercício 17.4 — Aplicando o retorno em uma venda
def calcular_total_com_desconto(preco, quantidade):
    compra = preco * quantidade

    if compra >= 100:
        result = compra * 0.10
        valor_final = compra - result
    else:
        valor_final = compra

    return valor_final

    
total = calcular_total_com_desconto(60, 1)

print(total)


# Exercício 17.5 — Verificar e calcular o valor do estoque
def calcular_valor_estoque(preco, quantidade):
    if quantidade <= 0:
        res = "Estoque inválido! "
    else:
        soma = preco * quantidade
        res = soma

    return res

result = calcular_valor_estoque(25, 4)

print(result)