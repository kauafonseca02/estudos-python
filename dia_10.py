# ============================================================
# DIA 10 — WHILE
# ============================================================

# Exercício 1 — Contador de 1 a 5
# i = 1

# while i < 6:
#     print(i)
#     i += 1


# Exercício 2 — Contagem regressiva de 10 a 1
# numero = 10

# while numero > 0:
#     print(numero)
#     numero -= 1


# Exercício 3 — Números pares de 2 a 20
# numero = 2

# while numero < 21:
#     print(numero)
#     numero += 2


# Exercício 4 — Números pares usando condição
# numero = 2

# while numero % 2 == 0 and numero < 21:
#     print(numero)
#     numero += 2


# Exercício 5 — Números de 1 a 10
# numero = 1

# while numero < 11:
#     print(numero)
#     numero += 1


# Exercício 6 — Contagem regressiva com mensagem final
# numero = 10

# while numero > 0:
#     print(numero)
#     numero -= 1

# print("Fim!")


# Exercício 7 — Números pares de 2 a 20
# numero = 2

# while numero < 21:
#     print(numero)
#     numero += 2


# Exercício 8 — Números ímpares de 1 a 19
# numero = 1

# while numero < 20:
#     print(numero)
#     numero += 2


# Exercício 9 — Identificando números pares e ímpares
# numero = 1

# while numero < 21:
#     if numero % 2 == 0:
#         print(f"{numero} é par")
#     else:
#         print(f"{numero} é ímpar")
#     numero += 1


# Exercício 10 — Soma de 1 a 100
# numero = 1
# soma = 0

# while numero < 101:
#     soma += numero
#     numero += 1

# print(f"A soma é: {soma}")


# Exercício 11 — Soma dos números pares de 1 a 100
# numero = 1
# soma = 0

# while numero < 101:
#     if numero % 2 == 0:
#         soma += numero
#     numero += 1

# print(f"A soma dos pares é: {soma}")


# Exercício 12 — Repetição até o usuário digitar 0
# input_usuario = int(input("Digite um número: "))

# while input_usuario != 0:
#     input_usuario = int(input("Digite um número: "))

# print("Programa finalizado com sucesso!")


# Exercício 13 — Contagem e soma dos números digitados
# input_usuario = int(input("Digite um número: "))
# contador = 0
# soma = 0

# while input_usuario != 0:
#     contador += 1
#     soma += input_usuario
#     input_usuario = int(input("Digite um número: "))

# print(f"Quantidade de números: {contador}")
# print(f"Soma: {soma}")
# print("Programa finalizado!")


# Exercício 14 — Análise de números positivos e negativos
# input_user = int(input("Digite um número: "))
# qtd_positivo = 0
# qtd_negativo = 0
# soma_positivo = 0
# soma_negativo = 0

# while input_user != 0:
#     if input_user > 0:
#         qtd_positivo += 1
#         soma_positivo += input_user
#     else:
#         qtd_negativo += 1
#         soma_negativo += input_user

#     input_user = int(input("Digite um número: "))

# print(f"\nQuantidade de números positivos: {qtd_positivo}")
# print(f"Quantidade de números negativos: {qtd_negativo}")
# print(f"Soma dos números positivos: {soma_positivo}")
# print(f"Soma dos números negativos: {soma_negativo}\n")


# Exercício 15 — Maior, menor e quantidade de números
# input_user = int(input("Digite um número: "))
# maior = input_user
# menor = input_user
# contador = 0

# while input_user != 0:
#     contador += 1

#     if input_user > maior:
#         maior = input_user

#     if input_user < menor:
#         menor = input_user

#     input_user = int(input("Digite um número: "))

# print(f"Maior número digitado: {maior}")
# print(f"Menor número digitado: {menor}")
# print(f"Quantidade de números digitados: {contador}")


# Exercício 16 — Análise completa com média e tratamento do 0
# input_user = int(input("Digite um número: "))
# maior = input_user
# menor = input_user
# contador = 0
# soma = 0

# while input_user != 0:
#     contador += 1
#     soma += input_user

#     if input_user > maior:
#         maior = input_user

#     if input_user < menor:
#         menor = input_user

#     input_user = int(input("Digite um número: "))

# if contador > 0:
#     media = soma / contador

#     print(f"Quantidade de números digitados: {contador}")
#     print(f"Soma dos números: {soma}")
#     print(f"Média dos números: {media}")
#     print(f"Maior número digitado: {maior}")
#     print(f"Menor número digitado: {menor}")
# else:
#     print("Nenhum número foi digitado.")  