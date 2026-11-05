import json
from json import JSONDecodeError


def carregar_produtos():
    try:
        with open("dia21_json/produtos.json", "r") as arquivo:
            produtos = json.load(arquivo)

    except FileNotFoundError:
        return []

    except JSONDecodeError:
        return []
    
    return produtos

def salvar_produtos(produtos):
    try:
        with open("dia21_json/produtos.json", "w") as arquivo:
            json.dump(produtos, arquivo, indent=4)

    except FileNotFoundError:
        return "\nErro ao salvar os produtos!\n"
    
    return "\nProdutos salvos com sucesso!\n"

def carregar_vendas():
    try:
        with open("dia21_json/vendas.json", "r") as arquivo:
            vendas = json.load(arquivo)

    except FileNotFoundError:
        return []

    except JSONDecodeError:
        return []
    
    return vendas

def salvar_vendas(vendas):
    try:
        with open("dia21_json/vendas.json", "w") as arquivo:
            json.dump(vendas, arquivo, indent=4)

    except FileNotFoundError:
        return "\nErro ao salvar as vendas!\n"
    
    return "\nVendas salvas com sucesso!\n"

