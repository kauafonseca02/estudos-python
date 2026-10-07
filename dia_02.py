# ============================================================
# DIA 02 — ESTRUTURAS CONDICIONAIS
# ============================================================

# Exercício 1 - Verificando se a pessoa é maior ou menor de idade
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exercício 2 - Verificando se um número é negativo, zero ou positivo
numero = float(input("Digite um número: "))
if numero < 0:
    print("O número é negativo")
elif numero == 0:
    print("O número é zero")
else:
    print("O número é positivo")

# Exercício 3 - Verificando se um número é par ou ímpar usando o operador %
numeroA = int(input("Digite um número: "))
if numeroA % 2 == 0:
    print("O número é par.")
else:
    print("O número é impar.")

# Exercício 4 - Comparando dois números
numero_A = float(input("Digite o primeiro número: "))
numero_B = float(input("Digite o segundo número: "))
if numero_A == numero_B:
    print("Os números são iguais.")
elif numero_A > numero_B:
    print("O primeiro número é maior.")
else:
    print("O segundo número é maior.")

# Exercício 5 - Verificando e classificando nota
nota = float(input("Nota: "))
if nota < 0 or nota > 10:
    print("Nota inválida.")
elif nota < 5:
    print("Reprovado.")
elif nota < 7:
    print("Recuperação.")
else:
    print("Aprovado.")

# Exercício 6 - Classificação combinada de idade e nota
nome = input("Nome: ")
idade = int(input("Idade: "))
nota = float(input("Nota: "))

if idade < 18:
    situacao = "Menor de idade"
else:
    situacao = "Maior de idade"
print(f"Situação: {situacao}")

if nota < 0 or nota > 10:
    resultado = "Nota inválida"
elif nota < 5:
    resultado = "Reprovado"
elif nota < 7:
    resultado = "Recuperação"
else:
    resultado = "Aprovado"
print(f"Resultado: {resultado}")

# Exercício 7 - Calculando desconto e preço final
preco = float(input("Preço: R$ "))
desconto = float(input("Desconto: "))

if desconto < 0 or desconto > 100:
    print("Desconto inválido")
else:
    valor_desconto = (desconto / 100) * preco
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    preco_final = preco - valor_desconto
    print(f"Preço final: R$ {preco_final:.2f}")

# Exercício 8 - Verificando duas condições com operador and
idade = int(input("Idade: "))
salario = float(input("Salário: "))

if idade >= 18 and salario >= 2000:
    status = "Financiamento aprovado!"
else:
    status = "Financiamento reprovado."
print(f"Status: {status}")