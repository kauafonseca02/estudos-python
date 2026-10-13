# ============================================================
# DIA 10 — WHILE + if
# ============================================================

# numeros = []

# input_user = int(input("Digite um número: "))
# contador = 0
# soma = 0
# maior = input_user
# menor = input_user

# while input_user != 0:
#     contador += 1
#     soma += input_user
#     numeros.append(input_user)

#     if input_user > maior:
#         maior = input_user

#     if input_user < menor:
#         menor = input_user

#     input_user = int(input("Digite um número: "))

# if contador > 0:
#     print(numeros)
#     print(f"Quantidade: {contador}")
#     print(f"Soma: {soma}")
#     print(f"Maior: {maior}")
#     print(f"Menor: {menor}")
# else:
#     print("Nenhum número foi digitado.")

# numeros = []

# input_user = int(input("Digite um número: "))
# numeros_pares = 0
# numeros_impares = 0
# soma_pares = 0
# soma_impares = 0

# while input_user != 0:
#     numeros.append(input_user)

#     if input_user % 2 == 0:
#         numeros_pares += 1
#         soma_pares += input_user
#     else:
#         numeros_impares += 1
#         soma_impares += input_user

#     input_user = int(input("Digite um número: "))

# print(f"\n{numeros}")
# print(f"Quantidade de pares: {numeros_pares}")
# print(f"Quantidade de ímpares: {numeros_impares}")
# print(f"Soma dos pares: {soma_pares}")
# print(f"Soma dos ímpares: {soma_impares}")

# numeros = []

# input_user = int(input("Digite um número: "))
# contador = 0
# soma = 0
# maior = input_user
# menor = input_user  

# while input_user != 0:
#     numeros.append(input_user)
#     contador += 1
#     soma += input_user

#     if input_user > maior:
#         maior = input_user

#     if input_user < menor:
#         menor = input_user

#     input_user = int(input("Digite um número: "))

# if contador > 0:
#     media = soma / contador

#     print(numeros)
#     print(f"Maior: {maior}")
#     print(f"Menor: {menor}")
#     print(f"Quantidade: {contador}")  
#     print(f"Média: {media}")
#     
# else:
#     print("Nenhum número foi digitado.")  

# numeros = []

# contador = 0

# input_user = int(input("Digite um número: "))
# numeros.append(input_user)

# maior = input_user
# menor = input_user

# while contador < 4:
#     contador += 1
#     input_user = int(input("Digite um número: "))
#     numeros.append(input_user)

#     if input_user > maior:
#         maior = input_user

#     if input_user < menor:
#         menor = input_user

# numeros_crescente = sorted(numeros, reverse=False)
# numeros_decrescente = sorted(numeros, reverse=True)

# print(f"\n {numeros}")
# print(numeros_crescente)
# print(numeros_decrescente)
# print(maior)
# print(menor)

# vendas = []
# contador = 0
# total = 0
# contador_500 = 0


# input_user = int(input("\nQuantas vendas serão registradas? "))

# if input_user != 0 and input_user > 0:

#     while contador < input_user:
#         contador += 1
#         input_valor = int(input(f"\nValor da venda: "))
#         vendas.append(input_valor)
#         total += input_valor

#         if contador == 1:
#             maior = input_valor
#             menor = input_valor

#         if input_valor > 500:
#             contador_500 += 1

#         if input_valor > maior:
#             maior = input_valor

#         if input_valor < menor:
#             menor = input_valor
        
        
#     media = total / contador

#     print("\n--- RESULTADO DAS VENDAS ---")

#     print(f"Vendas: {vendas}")
#     print(f"Total vendido: R$ {total:.2f}")
#     print(f"Média por venda: R$ {media:.2f}")
#     print(f"Maior venda: R$ {maior:.2f}")
#     print(f"Menor venda: R$ {menor:.2f}")
#     print(f"Vendas acima de R$ 500: {contador_500}\n")

# else:
#     if input_user < 0:
#         print("\nVenda registrada incorretamente, menor que 0.\n")

#     if input_user == 0:
#         print("\nNenhuma venda registrada.\n")
        
# produtos = []
# contador = 0

# input_user = str(input("\nDigite um produto: "))
# produtos.append(input_user)

# while contador < 4:
#     contador += 1
#     input_user = str(input("Digite um produto: "))
#     produtos.append(input_user)
    
# input_produto = str(input("\nQual produto deseja buscar? "))

# if input_produto not in produtos:
#     print("\nProduto não encontrado!")
# else:
#     print("\nProduto encontrado!")

# nomes = []
# contador = 0

# input_user = str(input("\nDigite um nome: "))
# nomes.append(input_user)

# while contador < 4:
#     contador += 1
#     input_user = str(input("Digite um nome: "))
#     nomes.append(input_user)

# pesquisar = str(input("\nPesquise um nome: "))
# if pesquisar in nomes:
#     posicao = nomes.index(pesquisar)
#     posicao += 1
#     print(f"Nome encontrado na posicao: {posicao}")
# else:
#     print("Nome não encontrado!")

contador = 0
soma = 0
notas = []
qtd_nota_menor = 0
qtd_nota_maior = 0

while contador < 5:
    contador += 1

    input_user = float(input("Digite uma nota: "))    
    notas.append(input_user)
    soma += input_user

    if contador == 1:   
        maior_nota = input_user
        menor_nota = input_user

    if input_user > maior_nota:
        maior_nota = input_user
        
    if input_user < menor_nota:
        menor_nota = input_user

    if input_user >= 7:
        qtd_nota_maior += 1

    if input_user < 7:
        qtd_nota_menor += 1

media = soma / contador
    
print(notas)
print(f"Média: {media:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Alunos com nota >= 7: {qtd_nota_maior}")
print(f"Alunos com nota < 7: {qtd_nota_menor}")