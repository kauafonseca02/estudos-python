# ============================================================
# DIA 08 & 09 — ENUMERATE, ZIP E SORTED
# ============================================================

# Análise de Reposição de Estoque com Enumerate
estoque = [
    {"item": "Palete PBR", "quantidade": 150},
    {"item": "Caixa de Papelão", "quantidade": 40},
    {"item": "Filme Stretch", "quantidade": 12},
    {"item": "Fita Zepelim", "quantidade": 85},
    {"item": "Empilhadeira Elétrica", "quantidade": 3}
]

def analisar_reposicao(estoque):
    quantidade_repor = 0
    for indice, item in enumerate(estoque):
        if item['quantidade'] < 20:
            quantidade_repor += 1
            print(f"{indice} - {item['item']} - Quantidade: {item['quantidade']} - ⚠️ REPOSIÇÃO URGENTE")
        else:
            print(f"{indice} - {item['item']} - Quantidade: {item['quantidade']} - OK")
    return quantidade_repor

resultado = analisar_reposicao(estoque)
print(f"Total de itens críticos para reposição: {resultado}")

# Análise com Zip
nomes = ["Carlos", "Ana", "Bruno", "Marina", "João"]
tempos = [45.2, 52.8, 43.7, 48.5, 46.1]

menor_tempo = tempos[0]
nome_menor_tempo = nomes[0]
maior_tempo = tempos[0]
nome_maior_tempo = nomes[0]
contador = 0
soma = 0

for nome, tempo in zip(nomes, tempos):
    if tempo < menor_tempo:
        menor_tempo = tempo
        nome_menor_tempo = nome
    if tempo > maior_tempo:
        maior_tempo = tempo
        nome_maior_tempo = nome
    if tempo < 48:
        contador += 1
        soma += tempo

print(f"\nMelhor tempo: {nome_menor_tempo} - {menor_tempo:.2f} minutos")
print(f"Pior tempo: {nome_maior_tempo} - {maior_tempo:.2f} minutos")
print(f"Corredores abaixo de 48 minutos: {contador}")
print(f"Soma dos tempos abaixo de 48 minutos: {soma:.2f} minutos")