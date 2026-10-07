# i = 1

# while i < 6:
#     print(i)
#     i += 1


# numero = 10

# while numero > 0:
#     print(numero)
#     numero -= 1

# numero = 2

# while numero < 21:
#     print(numero)
#     numero += 2 

# numero = 2

# while numero % 2 == 0 and numero < 21:
#     print(numero)
#     numero += 2

# numero = 1

# while numero < 11:
#     print(numero)
#     numero += 1

# numero = 10

# while numero > 0:
#     print(numero)
#     numero -= 1 

# print("Fim!")

# numero = 2

# while numero < 21:
#     print(numero)
#     numero += 2

# numero = 1

# while numero < 20:
#     print(numero)
#     numero += 2

# numero = 1

# while numero < 21:
#     if numero % 2 == 0:
#         print(f"{numero} é par")
#     else:
#         print(f"{numero} é ímpar")
#     numero += 1    

# numero = 1
# soma = 0

# while numero < 101:
#     soma += numero
#     numero += 1

# print(f"A soma é: {soma}")

# numero = 1
# soma = 0

# while numero < 101:
#     if numero % 2 == 0:
#         soma += numero
#     numero += 1

# print(f"A soma dos pares é: {soma}")

# input_usuario = int(input("Digite um número: "))

# while input_usuario != 0:
#     input_usuario = int(input("Digite um número: "))

# print("Programa finalizado com sucesso!")

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

input_user = int(input("Digite um número: "))
maior = input_user
menor = input_user
contador = 0
soma = 0
while input_user != 0:
    contador += 1
    soma += input_user

    if input_user > maior:
        maior = input_user

    if input_user < menor:
        menor = input_user

    input_user = int(input("Digite um número: "))
    
if contador > 0:
    media = soma / contador

    print(f"Quantidade de números digitados: {contador}")
    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media}")
    print(f"Maior número digitado: {maior}")
    print(f"Menor número digitado: {menor}")
else:
    print("Nenhum número foi digitado.")