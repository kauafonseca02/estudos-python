# ============================================================
# DIA 13 - TRATAMENTO DE ERROS (TRY\EXCEPT)
# ============================================================

# try:
#     idade = int(input("Digite sua idade: "))
#     print(f"Você tem {idade} anos.")

# except ValueError:
#     print("Você precisa digitar um número inteiro.")

## VALIDAR A QUANTIDADE ANTES DE COMEÇAR O CADASTRO.

# qt_valida = False

# while not qt_valida:
#     try:
#         qt = int(input("\nQuantos números deseja cadastrar? "))

#         if qt > 0:
#             qt_valida = True
#         else:
#             print("\nDigite uma quantidade maior que zero. ")

#     except ValueError:
#         print("\nVocê precisa digitar um número inteiro. ")

## ETAPA 2 - CADASTRAR OS NÚMEROS_

qt_valida = False

while not qt_valida:
    try:
        qt = int(input("\nQuantos números deseja cadastrar? "))

        if qt > 0:
            qt_valida = True
        else:
            print("\nDigite uma quantidade maior que zero. ")


    except ValueError:
        print("\nVocê precisar digitar um número inteiro. ")

numeros = []
c = 0

while c < qt:
    try:
        numero = int(input("Digite um número: "))
        numeros.append(numero)
        c += 1


    except ValueError:
        print("Você precisa digitar um número inteiro. ")

print(numeros)
print(sum(numeros))