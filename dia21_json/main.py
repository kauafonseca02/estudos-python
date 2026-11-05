from produtos import (
    cadastrar_produto,
    listar_produtos,
    consultar_produto,
    editar_produto,
    excluir_produto
)

from vendas import (
    registrar_venda,
    listar_vendas
)

from relatorios import (
    exibir_faturamento,
    exibir_total_unidades,
    exibir_produto_mais_vendido,
    relatorio_geral_vendas
)

while True:
    print("\n===== SISTEMA DE ESTOQUE FK =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Consultar produto")
    print("4 - Editar produto")
    print("5 - Excluir produto")
    print("6 - Registrar venda")
    print("7 - Listar vendas")
    print("8 - Exibir faturamento")
    print("9 - Exibir total de unidades vendidas")
    print("10 - Exibir produto mais vendido")
    print("11 - Relatório geral de vendas")
    print("12 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        consultar_produto()

    elif opcao == "4":
        editar_produto()

    elif opcao == "5": 
        excluir_produto()

    elif opcao == "6":
        registrar_venda()

    elif opcao == "7":
        listar_vendas()

    elif opcao == "8":
        exibir_faturamento()

    elif opcao == "9":
        exibir_total_unidades()

    elif opcao == "10":
        exibir_produto_mais_vendido()

    elif opcao == "11":
        relatorio_geral_vendas()

    elif opcao == "12":
        print("\nSistema se encerrando... FK ")
        break
    else:
        print("\nOpção inválida! ")
