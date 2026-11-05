from arquivos import carregar_vendas


def faturamento_total():
    vendas = carregar_vendas()
    total = 0

    for venda in vendas:
        total += venda['total']

    return total

def exibir_faturamento():
    print(f"\nFaturamento total: R$ {faturamento_total():.2f}")

def total_unidades_vendidas():
    vendas = carregar_vendas()
    total = 0

    for venda in vendas:
        total += venda['quantidade']

    return total

def exibir_total_unidades():
    print(f"\nTotal de unidades vendidas: {total_unidades_vendidas()}")

def produto_mais_vendido():
    vendas = carregar_vendas()
    produto_vendidos = {}

    if not vendas:
        return None, 0
    
    for venda in vendas:
        nome = venda['produto']
        quantidade = venda['quantidade']
    
        if nome not in produto_vendidos:
            produto_vendidos[nome] = quantidade
        else:
            produto_vendidos[nome] = produto_vendidos[nome] + quantidade

    maior_quantidade = 0
    nome_mais_vendido = ""

    for nome, quantidade in produto_vendidos.items():

        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            nome_mais_vendido = nome

    return nome_mais_vendido, maior_quantidade
        
def exibir_produto_mais_vendido():
    nome, quantidade = produto_mais_vendido()

    if nome is None:
        print("\nNenhuma venda registrada! ")
        return

    print(f"Produto mais vendido: {nome} | Unidades: {quantidade}")

def total_vendas():
    vendas = carregar_vendas()
    return len(vendas)
 
def relatorio_geral_vendas():
    faturamento = faturamento_total()
    total_unidades = total_unidades_vendidas()
    nome_produto, quantidade_produto = produto_mais_vendido()
    quantidade_vendas = total_vendas()

    print("\n===== RELATÓRIO GERAL DE VENDAS =====")
    print(f"\n  Faturamento total: R$ {faturamento:.2f}")
    print(f"    Unidades vendidas: {total_unidades}")

    if nome_produto is None:
        print("\nNenhuma venda registrada ")
    else:
        print(f"    Produto mais vendido: {nome_produto}, Quantidade: {quantidade_produto}")

    print(f"    Total de vendas realizadas: {quantidade_vendas}")    
