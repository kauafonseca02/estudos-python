# ============================================================
# DIA 07 — COMPOSIÇÃO DE FUNÇÕES
# ============================================================

def dobro(numero):
    return numero * 2

def mostrar_dobro(numero):
    resultado = dobro(numero)
    return f"O dobro é {resultado}"

print(mostrar_dobro(10))

# Média e classificação
numeros = [1, 1, 1, 1]

def calcular_media(numeros):
    soma = sum(numeros)
    return soma / len(numeros)

def classificar_media(media):
    if media < 5:
        return "Reprovado"
    elif media < 7:
        return "Recuperação"
    return "Aprovado"

print(classificar_media(calcular_media(numeros)))

# Média de salários
def calcular_media_salarios(pessoas):
    soma = sum(pessoa["salario"] for pessoa in pessoas)
    return soma / len(pessoas)

def classificar_salario(media):
    if media < 0:
        return "Salário inválido."
    elif media < 2500:
        return "Salário baixo."
    elif media < 5000:
        return "Salário médio."
    return "Salário alto."

print(classificar_salario(calcular_media_salarios(pessoas)))

# Analisar pessoas
def analisar_pessoas(pessoas):
    contador = 0
    soma = 0
    for pessoa in pessoas:
        if pessoa["idade"] >= 18:
            contador += 1
            soma += pessoa["salario"]
    media = soma / contador if contador > 0 else 0
    return contador, soma, media

contador, soma, media = analisar_pessoas(pessoas)
print(f"Maiores de idade: {contador}")
print(f"Soma dos salários: {soma}")
print(f"Média salarial: {media}")