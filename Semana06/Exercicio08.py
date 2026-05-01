caixa = float(input("Digite o dinheiro atual em caixa: "))
opcao = 0

while opcao != 4:
    print("1 - Realizar venda")
    print("2 - Retirar dinheiro")
    print("3 - Dinheiro em caixa")
    print("4 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        venda = float(input("Digite o valor da venda: "))
        caixa = caixa + venda
        print("Venda realizada.")

    elif opcao == 2:
        retirada = float(input("Digite o valor da retirada: "))

        if retirada <= caixa:
            caixa = caixa - retirada
            print("Retirada realizada.")
        else:
            print("Dinheiro insuficiente no caixa.")

    elif opcao == 3:
        print("Dinheiro em caixa:", caixa)

    elif opcao == 4:
        print("Sistema encerrado.")

    else:
        print("Opção inválida.")
