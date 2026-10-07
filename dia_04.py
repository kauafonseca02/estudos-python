# DIA 04 - LISTAS

# Criando e acessando uma lista
frutas = ["banana", "maçã", "laranja", "morango", "uva"]

print(frutas[0])
print(frutas[-1])
print(len(frutas))


# Adicionando elementos
frutas.append("melancia")
print(frutas)


# Percorrendo uma lista
for fruta in frutas:
    print(fruta)


# Filtrando elementos
for fruta in frutas:
    if len(fruta) > 5:
        print(fruta)


# Alterando elementos
numeros = [10, 20, 30, 40, 50]

numeros[1] = 200
numeros[4] = 500

print(numeros)


# Removendo elementos
numeros.remove(200)
numeros.pop()

print(numeros)


# Contando e somando elementos
numeros = [10, 25, 8, 42, 17, 30, 5]

contador_par = 0
contador_impar = 0
soma = 0

for numero in numeros:
    if numero % 2 == 0:
        contador_par = contador_par + 1
    else:
        contador_impar = contador_impar + 1

    soma = soma + numero

print(f"Pares: {contador_par}")
print(f"Ímpares: {contador_impar}")
print(f"Soma: {soma}")


# Maior, menor, soma e contagem
numeros = [12, -25, 27, 8, 31, 14, 20]

maior = numeros[0]
menor = numeros[0]
soma = 0
contador = 0

for numero in numeros:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    if numero > 15:
        contador = contador + 1

    soma = soma + numero

print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Soma: {soma}")
print(f"Maiores que 15: {contador}")


# Duas listas relacionadas por índice
nomes = ["Ana", "João", "Carlos", "Maria", "Pedro", "Lucas"]
idades = [17, 22, 16, 25, 19, 30]

contador = 0

for i in range(len(idades)):
    if idades[i] >= 18 and idades[i] <= 25:
        print(f"{nomes[i]} - {idades[i]} anos")
        contador = contador + 1

print(f"Quantidade: {contador}")