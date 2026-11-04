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

def cadastrar_produto():
    
    produtos = carregar_produtos()

    nome = " ".join(input("\nNome do produto: ").split())

    if nome == "":
        print("\nO nome do produto não pode ficar vazio!")

    else:
        try:
            adicionar_produto = {
                "nome": nome,
                "preco": float(input("Preço: ")),
                "estoque": int(input("Estoque: "))
            }

        except ValueError:
            print("\nPreço ou estoque inválido!")

        else:
            produto_existe = False

            for produto in produtos:
                if nome.lower() == produto["nome"].strip().lower():
                    produto_existe = True

            if produto_existe:
                print("\nO produto já existe.")

            elif adicionar_produto["preco"] <= 0 or adicionar_produto["estoque"] < 0:
                print("\nPreço ou estoque inválido!")

            else:
                produtos.append(adicionar_produto)
                print(salvar_produtos(produtos))

def listar_produtos():
    produtos = carregar_produtos()
    

    if not produtos:
        print("\nNão existem produtos cadastrados! ")

    else:
        for produto in produtos:
            print(f"Nome: {produto['nome']} | "
                f"Preço: R$ {produto['preco']:.2f} | "
                f"Estoque: {produto['estoque']}")

def consultar_produto():
    produtos = carregar_produtos()

    nome_consulta = " ".join(input("\nNome para consultar: ").split())

    if nome_consulta == "":
        print("\nDigite um nome para consultar!")
        return

    produto_encontrado = False

    for produto in produtos:
        if nome_consulta.lower() == produto["nome"].lower():
            produto_encontrado = True
            print(f"Nome: {produto['nome']} | "
                  f"Preço: R$ {produto['preco']:.2f} | "
                  f"Estoque: {produto['estoque']}")

    if not produto_encontrado:
        print("\nProduto não encontrado! ")

def editar_produto():
    produtos = carregar_produtos()

    print("\n===== EDITAR PRODUTO =====\n")

    nome_editar = " ".join(input("\nNome do produto: ").split())

    if nome_editar == "":
        print("\nDigite um nome para editar! ")
        return

    produto_encontrado = False

    for produto in produtos:
        if nome_editar.lower() == produto["nome"].lower():
            produto_encontrado = True
            
            print("\nProduto encontrado! ")
            print(f"Preço atual: R$ {produto['preco']:.2f}")
            print(f"Estoque atual: {produto['estoque']}\n")
            
            try:
                novo_preco = float(input("Novo preço: "))
                novo_estoque = int(input("Novo estoque: "))

            except ValueError:
                print("\nPreço ou estoque inválido! ")
                return

            if novo_preco <= 0 or novo_estoque < 0:
                print("\nPreço ou estoque inválido! ")
                return
            
            produto["preco"] = novo_preco
            produto["estoque"] = novo_estoque

            salvar_produtos(produtos)
            print("\nProduto atualizado com sucesso! ")
            return

    if not produto_encontrado:
        print("\nProduto não encontrado! ")

def excluir_produto():
    produtos = carregar_produtos()

    nome_excluir = " ".join(input("\nNome do produto: ").split())

    if nome_excluir == "":
        print("\nDigite um nome para excluir! ")
        return

    produto_encontrado = False

    for produto in produtos:
        if nome_excluir.lower() == produto['nome'].lower():
            produto_encontrado = True

            produtos.remove(produto)
            salvar_produtos(produtos)

            print("\nProduto excluído com sucesso! ")
            return

    if not produto_encontrado:
        print("\nProduto não encontrado! ")

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

def faturamento_total():
    vendas = carregar_vendas()
    total = 0

    for venda in vendas:
        total += venda['total']

    return total

def exibir_faturamento():
    print(f"\nFaturamento total: R$ {faturamento_total():.2f}")

def total_unidades_vendidas():
    vendas = carregar_vendas()
    total = 0

    for venda in vendas:
        total += venda['quantidade']

    return total

def exibir_total_unidades():
    print(f"\nTotal de unidades vendidas: {total_unidades_vendidas()}")

def produto_mais_vendido():
    vendas = carregar_vendas()
    produto_vendidos = {}

    if not vendas:
        return None, 0

    for venda in vendas:
        nome = venda['produto']
        quantidade = venda['quantidade']
    
        if nome not in produto_vendidos:
            produto_vendidos[nome] = quantidade
        else:
            produto_vendidos[nome] = produto_vendidos[nome] + quantidade

    maior_quantidade = 0
    nome_mais_vendido = ""

    for nome, quantidade in produto_vendidos.items():

        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            nome_mais_vendido = nome

    return nome_mais_vendido, maior_quantidade
        
def exibir_produto_mais_vendido():
    nome, quantidade = produto_mais_vendido()

    if nome is None:
        print("\nNenhuma venda registrada! ")
        return

    print(f"Produto mais vendido: {nome} | Unidades: {quantidade}")
    
while True:
    print("\n===== SISTEMA DE ESTOQUE FK =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Consultar produto")
    print("4 - Editar produto")
    print("5 - Excluir produto")
    print("6 - Registrar venda")
    print("7 - Listar vendas")
    print("8 - Exibir faturamento")
    print("9 - Exibir total de unidades vendidas")
    print("10 - Exibir produto mais vendido")
    print("11 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        consultar_produto()

    elif opcao == "4":
        editar_produto()

    elif opcao == "5": 
        excluir_produto()

    elif opcao == "6":
        registrar_venda()

    elif opcao == "7":
        listar_vendas()

    elif opcao == "8":
        exibir_faturamento()

    elif opcao == "9":
        exibir_total_unidades()

    elif opcao == "10":
        exibir_produto_mais_vendido()

    elif opcao == "11":
        print("\nSistema se encerrando... FK ")
        break
    else:
        print("\nOpção inválida! ")
