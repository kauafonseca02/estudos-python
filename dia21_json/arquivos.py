import json


def carregar_produtos():
    with open("dia21_json/produtos.json", "r") as arquivo:
        produtos = json.load(arquivo)

    return produtos

def salvar_produtos(produtos):
    with open("dia21_json/produtos.json", "w") as arquivo:
        json.dump(produtos, arquivo, indent=4)

    return "\nProdutos salvos com sucesso!\n"

def carregar_vendas():
    with open("dia21_json/vendas.json", "r") as arquivo:
        vendas = json.load(arquivo)

    return vendas

def salvar_vendas(vendas):
    with open("dia21_json/vendas.json", "w") as arquivo:
        json.dump(vendas, arquivo, indent=4)

    return "\nVendas salvas com sucesso!\n"

