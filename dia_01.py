# ============================================================
# DIA 01 — FUNDAMENTOS DO PYTHON
# ============================================================

# EXERCÍCIO 1 — PRIMEIROS COMANDOS
print("Olá, mundo!")
print("Meu nome é Kauã")
print("Estou aprendendo Python")
print("Meu objetivo é conseguir um estágio em tecnologia")

# EXERCÍCIO 2 — VARIÁVEIS E TIPOS DE DADOS
nome = "Kauã"           # str → texto
idade = 23              # int → número inteiro
altura = 1.80           # float → número decimal
estudando = True        # bool → verdadeiro ou falso
cidade = "Jaguariúna"   # str → texto

print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudando))
print(type(cidade))

# EXERCÍCIO 3 — OPERAÇÕES MATEMÁTICAS
print(10 + 5)  # soma
print(10 - 5)  # subtração
print(10 * 5)  # multiplicação
print(10 / 5)  # divisão

# EXERCÍCIO 4 — CÁLCULO DE SALÁRIO
salario = 2690
contas = 1500
saldo = salario - contas
print(saldo)

# EXERCÍCIO 5 — ENTRADA DE DADOS
nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura:.2f}")

# EXERCÍCIO 6 — CADASTRO DE PESSOA
nomeA = input("Nome: ")
idadeA = int(input("Idade: "))
alturaA = float(input("Altura: "))
pesoA = float(input("Peso: "))

print("Olá,", nomeA, "!")
print("Você tem", idadeA, "anos.")
print(f"Sua altura é {alturaA:.2f} m.")
print(f"Seu peso é {pesoA:.2f} kg.")