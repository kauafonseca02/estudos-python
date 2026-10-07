# # # ###Provao 3 dias - Cadastro e classificação - Nome, idade, salario, situação

# # # nome = input("Nome: ")
# # # idade = int(input("Idade: "))
# # # salario = float(input("Salário: "))

# # # if idade < 18:
# # #     situacao = "Menor de idade"
# # # else:
# # #     situacao = "Maior de idade"

# # # if salario < 2000:
# # #     classif = "Salário baixo"
# # # elif salario < 3000:
# # #     classif = "Salário médio"
# # # else:
# # #     classif = "Salário alto"

# # # print(f"Nome: {nome}")
# # # print(f"Idade: {idade}")
# # # print(f"Salário: {salario:.2f}")
# # # print(f"Situação: {situacao}")
# # # print(f"Classificação: {classif}")


# # ### Contador positivos, negativos, zeros, soma e média

# # soma = 0
# # contador_positivos = 0
# # contador_negativos = 0
# # contador_zeros = 0

# # for reps in range(7):
# #     numero = float(input("Digite um número: "))

# #     if numero < 0:
# #         contador_negativos = contador_negativos + 1
# #     elif numero > 0:
# #         contador_positivos = contador_positivos + 1
# #     else:
# #         contador_zeros = contador_zeros + 1

# #     soma = soma + numero

# # media = soma / 7

# # print(f"Positivos: {contador_positivos}")
# # print(f"Negativos: {contador_negativos}")
# # print(f"Zeros: {contador_zeros}")
# # print(f"Soma: {soma:.2f}")
# # print(f"Média: {media:.2f}")


# ### 

# soma = 0
# contador_par = 0
# contador_impar = 0

# numero_um = int(input("Digite um número: "))

# if numero_um % 2:
#         contador_impar = contador_impar + 1
# else:
#         contador_par = contador_par + 1

# menor = numero_um
# maior = numero_um

# soma = soma + numero_um

# for reps in range(4):
#     numero = int(input("Digite um número: "))

#     soma = soma + numero

#     if numero % 2:
#         contador_impar = contador_impar + 1
#     else:
#         contador_par = contador_par + 1

#     if numero < menor:
#         menor = numero
#     elif numero > maior:
#         maior = numero

# media = soma / 5

# print(f"Maior: {maior:.2f}")
# print(f"Menor: {menor:.2f}")
# print(f"Soma: {soma:.2f}")
# print(f"Média: {media:.2f}")
# print(f"Quantidade de Pares: {contador_par}")
# print(f"Quantidade de Ímpares: {contador_impar}")