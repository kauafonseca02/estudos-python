# ============================================================
# DIA 06 — FUNÇÕES E DICIONÁRIOS
# ============================================================

def contar_maiores(numeros):
    contador = 0
    for numero in numeros:
        if numero >= 18:
            contador += 1
    return contador

numeros = [12, 18, 25, 7, 30, 16]
print(contar_maiores(numeros))

pessoas = [
    {"nome": "Kadu", "idade": 26, "salario": 4000},
    {"nome": "Mila", "idade": 40, "salario": 3000},
    {"nome": "Rochelle", "idade": 52, "salario": 2200},
    {"nome": "Ichigo", "idade": 20, "salario": 10000}
]

def contar_pessoas(pessoas):
    contador = 0
    for pessoa in pessoas:
        if pessoa['idade'] >= 18 and pessoa['salario'] >= 2500:
            contador += 1
    return contador

print(contar_pessoas(pessoas))

def maior_salario(pessoas):
    maior = pessoas[0]["salario"]
    nome_maior = pessoas[0]["nome"]
    for pessoa in pessoas:
        if pessoa["salario"] > maior:
            maior = pessoa["salario"]
            nome_maior = pessoa["nome"]
    return nome_maior

print(maior_salario(pessoas))