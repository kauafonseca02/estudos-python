import json

try:
    arquivo = open("dia21_json/produtos.json", "r")
    produtos = json.load(arquivo)
    
    for produto in produtos:
        print(f"Nome: {produto['nome']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Estoque: {produto['estoque']}")

except FileNotFoundError:
    print("Arquivo de produtos não encontrado!")