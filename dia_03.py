# ============================================================
# DIA 03 — REPETIÇÃO E CONSOLIDAÇÃO
# ============================================================

# While simples
contador = 1
while contador <= 10:
    print(contador)
    contador = contador + 1

# While com condição de parada
numero = float(input("Digite um número: "))
while numero != 0:
    numero = float(input("Digite um número: "))
print("Programa encerrado!")

# While + soma + quantidade
soma = 0
quantidade = 0
numero = float(input("Digite um número: "))

while numero != 0:
    soma = soma + numero
    quantidade = quantidade + 1
    numero = float(input("Digite um número: "))

print(f"Soma: {soma:.2f}")
print(f"Quantidade: {quantidade}")

# For + range
for numero in range(1, 11):
    print(numero)

# For + range + passo
for numero in range(2, 21, 2):
    print(numero)

# For + if + %
for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)

# For + acumulador
soma = 0
for numero in range(1, 101):
    soma = soma + numero
print(f"Soma: {soma}")

# Entrada de vários números + contador
contador_positivo = 0
contador_negativo = 0
contador_zero = 0

for _ in range(5):
    numero = float(input("Digite um número: "))
    if numero > 0:
        contador_positivo += 1
    elif numero < 0:
        contador_negativo += 1
    else:
        contador_zero += 1

print(f"Positivos: {contador_positivo}")
print(f"Negativos: {contador_negativo}")
print(f"Zeros: {contador_zero}")

# Maior, menor, soma e média
numero = float(input("Digite um número: "))
soma = numero
maior = numero
menor = numero

for _ in range(4):
    numero = float(input("Digite um número: "))
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

media = soma / 5
print(f"Maior: {maior:.2f}")
print(f"Menor: {menor:.2f}")
print(f"Soma: {soma:.2f}")
print(f"Média: {media:.2f}")