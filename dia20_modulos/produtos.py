produtos = [
    {"nome": "Fone", "preco": 85.00, "estoque": 10},
    {"nome": "Mouse", "preco": 60.00, "estoque": 0},
    {"nome": "Teclado", "preco": 120.00, "estoque": 8},
    {"nome": "Monitor", "preco": 700.00, "estoque": 3}
]

def listar_produtos(produtos):
    for produto in produtos:
        print(f"Nome do produto: {produto['nome']} - Preço: R$ {produto['preco']:.2f}")