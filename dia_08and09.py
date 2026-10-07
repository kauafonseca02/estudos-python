# nomes = ["Kadu", "Mila", "Rochelle", "Ichigo"]

# for indice, nome in enumerate(nomes):
#     print(f"{indice} - {nome}")

#     if indice == 1 or indice == 2:
#         print(f"{indice} - {nome}")

#     if indice % 2 == 0:
#         print(f"{indice} - {nome}")

#     if indice % 2 == 1:
#             print(f"{indice} - {nome}")

# ---------------------------------------------------------------------------------------

# produtos = [
#     {"nome": "Notebook", "preco": 3500},
#     {"nome": "Mouse", "preco": 150},
#     {"nome": "Teclado", "preco": 300},
#     {"nome": "Monitor", "preco": 1200}
# ]

# for indice, produto in enumerate(produtos):
#     print(f"{indice} - {produto['nome']}")

#     if indice % 2 == 0:
#          print(f"{indice} - {produto['nome']}")

# ---------------------------------------------------------------------------------------

# pedidos = [
#     {"produto": "Empilhadeira Toyota", "valor": 120000, "status": "entregue"},
#     {"produto": "Palete de Cerveja Lata", "valor": 4500, "status": "pendente"},
#     {"produto": "Leitor de Código de Barras", "valor": 800, "status": "entregue"},
#     {"produto": "Filme Stretches", "valor": 1200, "status": "pendente"}
# ]

# quantidade_pedidos_pendentes = 0
# total_monetario_pendente = 0
# valor_mais_caro = 0
# nome_mais_caro = ""  # ou None

# for indice, pedido in enumerate(pedidos):

#     if pedido['status'] ==  'pendente':
#         quantidade_pedidos_pendentes += 1
#         total_monetario_pendente += pedido['valor']

#         if pedido['valor'] > valor_mais_caro:
#             valor_mais_caro = pedido['valor']
#             nome_mais_caro = pedido['produto']

#     if pedido['status'] == 'pendente' and pedido['valor'] < 2000:
#         pedido['status'] = 'entregue'
        

# print(f"Total pendente: R$ {total_monetario_pendente:.2f}")

# print(f"Quantidade de pedidos pendentes: {quantidade_pedidos_pendentes}")

# print(f"Produto pendente mais caro: {nome_mais_caro} (R$ {valor_mais_caro:.2f})")

# print("\n--- Lista de Pedidos Atualizada ---")

# for pedido in pedidos:
#     print(f"{pedido['produto']} - status: {pedido['status']}")

    # if pedido['status'] ==  'pendente':
    #     print(f"{indice} - {pedido['produto']} - R$ {pedido['valor']:.2f} - {pedido['status']} - ⚠️  ATENÇÃO")
    # else:
    #     print(f"{indice} - {pedido['produto']} - R$ {pedido['valor']:.2f} - {pedido['status']}")



#     total_geral = total_geral + pedido['valor']

#     if pedido['status'] == "pendente":
#         print(f"ALERTA - O pedido: {indice} - {pedido['produto']} está pendente!")

#         total_pendentes = total_pendentes + pedido['valor']


# print("-" * 40)
# print(f"Valor total geral: R$ {total_geral:.2f}")
# print(f"Valor total pendente: R$ {total_pendentes:.2f}")

# ---------------------------------------------------------------------------------------


estoque = [
    {"item": "Palete PBR", "quantidade": 150},
    {"item": "Caixa de Papelão", "quantidade": 40},
    {"item": "Filme Stretch", "quantidade": 12},
    {"item": "Fita Zepelim", "quantidade": 85},
    {"item": "Empilhadeira Elétrica", "quantidade": 3}
]

def analisar_reposicao(estoque):

    quantidade_repor = 0

    for indice, item in enumerate(estoque):

        # if item['quantidade'] < 50 and indice % 2 == 0:
        #     print(f"{indice} - {item['item']} - Quantidade: {item['quantidade']}")

        # if item['quantidade'] < 50:
        #     print(f"{indice} - {item['item']} - Quantidade: {item['quantidade']} - ESTOQUE BAIXO.")
        # else: 
        #     print(f"{indice} - {item['item']} - Quantidade: {item['quantidade']} - ESTOQUE OK.")

        if item['quantidade'] < 20:
            quantidade_repor += 1
            print(f"{indice} - {item['item']} - Quantidade: {item['quantidade']} - ⚠️  REPOSIÇÃO URGENTE")
        else:
            print(f"{indice} - {item['item']} - Quantidade: {item['quantidade']} - OK")

    return quantidade_repor

resultado = analisar_reposicao(estoque)

print(f"Total de itens críticos para reposição: {resultado}")
