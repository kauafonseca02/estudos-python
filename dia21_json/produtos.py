from arquivos import carregar_produtos, salvar_produtos


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
