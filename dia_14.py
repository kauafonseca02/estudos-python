# def calcular_media(n1, n2, n3, nota_minima):
#     soma = n1 + n2 + n3
#     media = soma / 3

#     if media >= nota_minima:
#         mensagem = "Aprovado."
#     else:
#         mensagem = "Reprovado."

#     return media, mensagem

# media, mensagem = calcular_media(6, 8, 1, 6)

# print(f"\nMédia: {media:.1f}.")
# print(f"Resultado: {mensagem}\n")

# produto = {
#     "nome": "Teclado",
#     "preco": 120.50,
#     "estoque": 10,
# }

# print(f"\nNome: {produto['nome']} - preço: R$ {produto['preco']:.2f} - quantidade: {produto['estoque']}.\n")

# produto['estoque'] += 5

# print(f"Quantidade: {produto['estoque']}.\n")

# produto = {
#     "nome": "Mouse",
#     "preco": 80.00,
#     "estoque": 12
# }

# print(f"\nPreço atual: {produto['preco']:.2f}. \n")

# produto['preco'] += 10
# produto['estoque'] -= 3

# print(f"Nome: {produto['nome']} - Preço: R$ {produto['preco']:.2f} - Quantidade atualizada: {produto['estoque']}.\n")

# produto = {
#     "nome": "Monitor",
#     "preco": 750.00,
#     "estoque": 2
# }

# if produto['estoque'] <= 0:
#     print("\nProduto indisponível. \n")
# else:
#     print("\nProduto disponível. \n")

# produto = {
#     "nome": "Rádio",
#     "preco": 120.00,
#     "estoque": 7
# }

# qt_valida = False

# while not qt_valida:
#     try:
#         qt = int(input("\nQual a quantidade que você deseja comprar? "))

#         if qt <=  0:
#             print("Você precisa digitar uma quantidade maior que zero. ")
            
#         elif qt <= produto['estoque']:
#             produto['estoque'] -= qt

#             print("\nCompra realizada! ")
#             print(f"Produto: {produto['nome']}. ")
#             print(f"Estoque atualizado: {produto['estoque']}. ")

#             qt_valida = True

#         else:
#             print("Estoque insuficiente. ")
    

#     except ValueError:
#         print("\nVocê precisa digitar um número inteiro. ")

produto = {
    "nome": "Fone Bluetooth",
    "preco": 85.00,
    "estoque": 10
}

while True:
    try:
        q = int(input("\nQual quantidade deseja comprar? "))

        if q <= 0:
            print("A quantidade deve ser maior que 0. ")

        elif q > produto['estoque']:
            print("Estoque insuficiente! ")

        else:
            produto['estoque'] -= q

            total = q * produto['preco']

            print(f"\nValor total da venda: R$ {total:.2f} ")
            print(f"\nNome do produto: {produto['nome']} - Quantidade em estoque: {produto['estoque']}")
            break

    except ValueError:
        print("A quantidade deve ser um número inteiro. ")