# ============================================================
# DIA 05 — DICIONÁRIOS
# ============================================================

# 1. CRIAR E ACESSAR
pessoa = {
    "nome": "Kauã",
    "idade": 23,
    "cidade": "Jaguariúna",
    "cargo": "Estagiário"
}

print(pessoa["nome"])
print(pessoa["cargo"])


# 2. ADICIONAR E ALTERAR CHAVES
pessoa["salario"] = 2500.00   # Adiciona uma nova chave
pessoa["idade"] = 24          # Altera o valor de uma chave existente

print(pessoa)


# 3. VERIFICAR SE UMA CHAVE EXISTE
if "salario" in pessoa:
    print(f"Salário cadastrado: R$ {pessoa['salario']:.2f}")


# 4. REMOVER CHAVES
pessoa.pop("cidade")
print(pessoa)


# 5. PERCORRER CHAVES E VALORES (keys, values, items)
print("--- Chaves ---")
for chave in pessoa.keys():
    print(chave)

print("\n--- Valores ---")
for valor in pessoa.values():
    print(valor)

print("\n--- Chave e Valor ---")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


# 6. LISTA DE DICIONÁRIOS (ESTRUTURA MUITO USADA EM BANCOS)
clientes = [
    {"nome": "Ana", "conta": 1001, "saldo": 1500.00},
    {"nome": "Carlos", "conta": 1002, "saldo": 450.00},
    {"nome": "Mariana", "conta": 1003, "saldo": 3200.00}
]

# Percorrendo a lista de dicionários
for cliente in clientes:
    print(f"Cliente: {cliente['nome']} | Conta: {cliente['conta']} | Saldo: R$ {cliente['saldo']:.2f}")


# 7. FILTRAR E SOMAR DADOS EM LISTA DE DICIONÁRIOS
total_saldos = 0
clientes_VIP = 0

for cliente in clientes:
    total_saldos += cliente["saldo"]
    if cliente["saldo"] >= 1000:
        clientes_VIP += 1

print(f"\nTotal sob custódia: R$ {total_saldos:.2f}")
print(f"Quantidade de clientes VIP (saldo >= R$ 1000): {clientes_VIP}")