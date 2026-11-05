from arquivos import (
    carregar_produtos,
    salvar_produtos,
    carregar_vendas,
    salvar_vendas
)

def registrar_venda():
    produtos = carregar_produtos()
    vendas = carregar_vendas()

    nome_venda = " ".join(input("\nNome do produto: ").split())

    if nome_venda == "":
        print("\nDigite um nome para vender! ")
        return

    produto_encontrado = False

    for produto in produtos:
        if nome_venda.lower() == produto['nome'].lower():
            produto_encontrado = True
            try:
                quantidade_venda = int(input("\nQuantidade vendida: "))

            except ValueError:
                print("\nQuantidade inválida! ")
                return

            if quantidade_venda <= 0:
                print("\nQuantidade deve ser maior que zero. ")
                return
            
            if quantidade_venda > produto['estoque']:
                print("\nQuantidade insuficiente! ")
                return

            else:
                novo_estoque = produto['estoque'] - quantidade_venda
                produto['estoque'] = novo_estoque

                venda = {
                    "produto": nome_venda,
                    "quantidade": quantidade_venda,
                    "preco_unitario": produto['preco'],
                    "total": produto['preco'] * quantidade_venda
                }

                vendas.append(venda)

                salvar_vendas(vendas)

                salvar_produtos(produtos)

                print("\nVenda realizada com sucesso! ")
                return

            

    if not produto_encontrado:
        print("\nProduto não encontrado! ")

def listar_vendas():
    vendas = carregar_vendas()

    if not vendas:
        print("\nNenhuma venda registrada! ")
        return

    for venda in vendas:
        print(f"\nProduto: {venda['produto']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Preço unitário: R$ {venda['preco_unitario']:.2f}")
        print(f"Total: R$ {venda['total']:.2f}")
