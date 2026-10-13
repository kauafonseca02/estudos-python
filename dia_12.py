# ============================================================
# DIA 10 — WHILE + def + for
# ============================================================

# # Exercício 1: Cadastro e análise de números
# numeros = []
# contador = 0

# while contador < 5:
#     input_user = int(input("Digite um número: "))
#     numeros.append(input_user)
#     contador += 1

# def analisar_numeros(numeros):
#     soma = 0
#     qtd_par = 0
#     impar_qtd = 0

#     for numero in numeros:
#         soma += numero

#         if numero % 2 == 0:
#             qtd_par += 1
#         else:
#             impar_qtd += 1

#     maior = numeros[0]
#     menor = numeros[0]

#     for numero in numeros:

#         if numero > maior:
#             maior = numero

#         if numero < menor:
#             menor = numero

#     media = soma / len(numeros)

#     print(f"Números digitados: {numeros}")
#     print(f"A soma desses números: {soma:.2f}")
#     print(f"A média entre esses números: {media:.2f}")
#     print(f"O maior número: {maior}")
#     print(f"O menor número: {menor}")
#     print(f"Quantidade de pares: {qtd_par} - Quantidade de ímpares: {impar_qtd}")

# analisar_numeros(numeros)

## Exercício 2: Análise de vendas por função
# vendas = []
# contador = 0
# input_user = int(input("Quantas vendas serão registradas? "))

# if input_user != 0:
#     while contador < input_user:
#         input_valor = float(input("Valor da venda: "))
#         vendas.append(input_valor)
#         contador += 1

#     def analisar_vendas(vendas):
#         soma = 0
#         qtd_acima_500 = 0
#         qtd_menor_500 = 0

#         for venda in vendas:
#             soma += venda
#             if venda > 500:
#                 qtd_acima_500 += 1
#             if venda < 500:
#                 qtd_menor_500 += 1
            
#         maior = vendas[0]
#         menor = vendas[0]

#         for venda in vendas:
#             if venda > maior:
#                 maior = venda
#             if venda < menor:
#                 menor = venda
        
#         media = soma / len(vendas)

#         print(f"O total vendido foi: R$ {soma:.2f}")
#         print(f"A média das vendas: R$ {media:.2f}")
#         print(f"Maior venda: R$ {maior:.2f} - Menor venda: R$ {menor:.2f}")
#         print(f"Quantidade de vendas maior que R$ 500.00: {qtd_acima_500}")
#         print(f"Quantidade de vendas menor que R$ 500.00: {qtd_menor_500}")

#     analisar_vendas(vendas)
# else:
#     print("\nNenhum venda foi registrada.\n")

# produtos = []
# contador = 0
# input_user = int(input("Quantos produtos serão cadastrados? "))

# while contador < input_user:
#     produto = str(input("Nome do produto: "))
#     produtos.append(produto)
#     contador +=1

# def buscar_produto(produtos):
#     produto_digitado = input("Informe o nome do produto que deseja encontrar: ")

#     encontrado = False
#     posicao = 0

#     for produto in produtos:

#         if produto_digitado == produto:
#             encontrado = True
#             print(f"Produto encontrado na posição {posicao}! ")

#             break

#         posicao += 1

#     if not encontrado:
#         print("Produto não encontrado.")

# buscar_produto(produtos)

## Exercício 4 — Análise de notas

# notas = []
# cont = 0

# qtd_notas = int(input("\nQuantas notas serão cadastradas? "))

# def analisar_notas(notas):
#         soma = 0
#         maiorIgual_7 = 0
#         menor_7 = 0
#         for nota in notas:
#             soma += nota
            
#             if nota >= 7:
#                 maiorIgual_7 += 1

#             if nota < 7:
#                 menor_7 +=1 

#         maior = notas[0]
#         menor = notas[0]
#         for nota in notas:
#             if nota > maior:
#                 maior = nota

#             if nota < menor:
#                 menor = nota

#         media = soma / len(notas)

#         print(f"\nNotas cadastradas: {notas}")
#         print(f"Média: {media:.2f}")
#         print(f"Maior nota: {maior:.2f} - Menor nota: {menor:.2f}")
#         print(f"Notas iguais ou superiores a 7: {maiorIgual_7}")
#         print(f"Notas menor que 7: {menor_7}\n")

# if qtd_notas != 0:
#     print("\n")
#     while cont < qtd_notas:
#         nota = float(input("Nota: "))
#         notas.append(nota)
#         cont += 1
#         print("\n")

#     analisar_notas(notas)

# else:
#     print("\nNão há notas para validação.\n")

## Exercício 5: Aprovação de alunos

# soma = 0

# nome = str(input("\nQual é o seu nome? "))
# nota1 = float(input("\nInforme a 1º nota: "))
# nota2 = float(input("Informe a 2º nota: "))
# notas = [nota1, nota2]

# def calcular_media(nota1, nota2):
#     soma = nota1 + nota2

#     med = soma / len(notas)

#     return med

# media = calcular_media(nota1, nota2)

# if media >= 7:
#     result = "Aprovado."
# elif media > 5:
#     result = "Recuperação."
# else:
#     result = "Reprovado."
# print(f"Nome do aluno: {nome}")
# print(f"Média: {media:.2f}")
# print(f"Resultado: {result}")

## Exercício 6 — Somar números com uma função

# numeros = []
# cont = 0
# quantidade = int(input("\nQuantos números deseja cadastrar? "))

# while cont < quantidade:
#     numero = float(input("Digite o número: "))
#     numeros.append(numero)
#     cont += 1

# def somar_numeros(numeros):
#     soma = 0

#     for numero in numeros:
#         soma += numero

#     return soma

# total = somar_numeros(numeros) 

# print(numeros)
# print(total)

## Exercício 7: Somar apenas os números positivos

# numeros = []
# cont = 0

# numero = int(input("\nQuantos números deseja cadastrar? "))
# while cont < numero:
#     n = int(input("\nDigite o número: "))
#     numeros.append(n)
#     cont += 1

# def somar_positivos(numeros):
#     soma = 0
#     for n in numeros:
#         if n > 0:
#             soma += n

#     return soma

# result = somar_positivos(numeros)
            
# print(f"\nNúmeros cadastrados: {numeros}")
# print(f"Soma dos números positivos: {result}")

## Exercício 8 — Encontrar o maior número com uma função

# numeros = []
# cont = 0

# numero = int(input("Quantos números deseja cadastrar? "))

# while cont < numero:
#     n = int(input("Digite o número: "))
#     numeros.append(n)
#     cont += 1

# def encontrar_maior(numeros):
#     maior = numeros[0]
#     for n in numeros:
#         if n > maior:
#             maior = n

#     return maior

# result = encontrar_maior(numeros)

# print(f"\nNúmeros cadastrados: {numeros}")
# print(f"Maior número: {result}")

## Exercício 9 — Encontrar o menor número com uma função

# numeros = []
# cont = 0

# numero = int(input("Quantos números deseja cadastrar? "))

# while cont < numero:
#     n = int(input("Digite o número: "))
#     numeros.append(n)
#     cont += 1

# def encontrar_menor(numeros):
#     menor = numeros[0]
#     for n in numeros:
#         if n < menor:
#             menor = n

#     return menor

# result = encontrar_menor(numeros)

# print(f"\nNúmeros cadastrados: {numeros}")
# print(f"Menor número: {result}")

## Exercício 10 — Análise completa de números

# numeros = []
# cont = 0

# numero = int(input("Quantos números desejar cadastrar? "))

# while cont < numero:
#     n = int(input("Digite o número: "))
#     numeros.append(n)
#     cont += 1

# def analisar_numeros(numeros):
#     soma = 0
#     for n in numeros:
#         soma += n

#     media = soma / len(numeros)

#     maior = numeros[0]
#     menor = numeros[0]

#     for n in numeros:
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n

#     return (soma, media, maior, menor)

# soma, media, maior, menor = analisar_numeros(numeros)

# print(f"Números cadastrados: {numeros}")
# print(f"Soma: {soma}")
# print(f"Média: {media}")
# print(f"Maior número: {maior}")
# print(f"Menor número: {menor}")    

## Exercício 11 — Análise de notas

# notas = []
# cont = 0

# qt = int(input("\nInforme a quantidade de notas: "))

# while cont < qt:
#     nota = float(input("\nDigite a nota: "))
#     notas.append(nota)
#     cont += 1

# def analisar_notas(notas):
#     soma = 0
#     maior = notas[0]
#     menor = notas[0]
#     maior_igual_7 = 0
#     for nota in notas:
#         soma += nota

#         if nota >= 7:
#             maior_igual_7 += 1

#         if nota > maior:
#             maior = nota
#         if nota < menor:
#             menor = nota

#     media = soma / len(notas)

#     return (media, maior, menor, maior_igual_7)

# media, maior, menor, maior_igual_7 = analisar_notas(notas)

# print(f"\nMédia: {media:.2f}")
# print(f"Maior nota: {maior:.2f}")
# print(f"Menor nota: {menor:.2f}")
# print(f"Quantidade de notas iguais ou superiores a 7: {maior_igual_7}")

## Exercício 12 — Cadastro de produtos

# produtos = []
# cont = 0

# qt = int(input("Quantos produtos serão cadastrados? "))

# while cont < qt:
#     nome_produto = str(input("Digite o nome: "))
#     produtos.append(nome_produto)
#     cont += 1

# def buscar_produto(produtos, nome_busca):
#     for nome_produto in produtos:
#         if nome_busca == nome_produto:
#             return  True

#     return False

# if qt > 0:
#     busca = input("\nBusque um produto: ")
#     res = buscar_produto(produtos, busca)

#     if res:
#         print("Produto encontrado!")
#     else:
#         print("Produto não encontrado.")

# else:
#     print("Nenhum produto cadastrado.")

## Exercício 13: Contar ocorrências de um produto

# produtos = []
# c = 0

# qt = int(input("\nQuantos produtos serão cadastrados? "))

# while c < qt:
#     nome_produto = str(input("\nDigite o nome do produto: "))
#     produtos.append(nome_produto)
#     c += 1

# nome_busca = input("\nQual produto deseja pesquisar?: ")

# def contar_produtos(produtos, nome_busca):
#     reps = 0
#     for nome_produto in produtos:
#             if nome_busca == nome_produto:
#                 reps += 1

#     return reps

# quantidade_encontrada = contar_produtos(produtos, nome_busca)

# if quantidade_encontrada == 0:
#     result = f"\nO produto {nome_busca} não foi cadastrado."
# elif quantidade_encontrada == 1:
#     result = f"\nO produto {nome_busca} aparece 1 vez."
# else:
#     result = f"\nO produto {nome_busca} aparece {quantidade_encontrada} vezes."

# print(result)