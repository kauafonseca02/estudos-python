# ============================================================
# DIA 15 — LISTAS DE DICIONÁRIO
# ============================================================

# Exercício 1 — Catálogo de produtos

produtos = [
    {"nome": "Fone", "preco": 85.00, "estoque": 10},
    {"nome": "Mouse", "preco": 60.00, "estoque": 5},
    {"nome": "Teclado", "preco": 120.00, "estoque": 8}
]

for produto in produtos:
    print(f"\nProduto: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Estoque: {produto['estoque']}\n")


# Exercício 2 — buscar um produto

nome_busca = input("Digite o nome do produto: ").lower()

for produto in produtos:
    if nome_busca == produto['nome'].lower():
        print(f"\nNome do produto: {produto['nome']} - Preço: {produto['preco']:.2f} - Estoque: {produto['estoque']}")
        break
else:
    print("\nProduto não encontrado! ") 


# Exercício 3 — atualizar o estoque

nome_produto = input("Digite o nome do produto: ").lower()

for produto in produtos:
    if nome_produto == produto['nome'].lower():

        while True:
            try:
                quantidade_adicionar = int(input("Quantidade à ser adicionada: "))

                if quantidade_adicionar <= 0:
                    print("A quantidade deve ser maior que 0. ")
                else:
                    produto['estoque'] += quantidade_adicionar

                    print(f"\nProduto: {produto['nome']}")
                    print(f"Novo estoque: {produto['estoque']}")
                    break

            except ValueError:
                print("Digite uma quantidade em um número inteiro. ")

        break

else:
    print("Produto não encontrado! ")