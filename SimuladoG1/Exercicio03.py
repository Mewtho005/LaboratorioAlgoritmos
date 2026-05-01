opcao = 0

while opcao != 2:
    print("1 - Vender combustível")
    print("2 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        print("\n1 - Gasolina (R$ 6,89)")
        print("2 - Diesel (R$ 4,80)")

        tipo = int(input("Escolha o combustível: "))
        litros = float(input("Digite a quantidade de litros: "))
        pago = float(input("Digite o valor pago: "))

        if tipo == 1:
            total = litros * 6.89
            print("Combustível: Gasolina")

        elif tipo == 2:
            total = litros * 4.80
            print("Combustível: Diesel")

        else:
            print("Opção inválida.")
            continue

        print("Valor total do abastecimento: R$", total)

        if pago >= total:
            troco = pago - total
            print("Troco: R$", troco)
        else:
            falta = total - pago
            print("Faltam: R$", falta)

    elif opcao == 2:
        print("Sistema encerrado.")

    else:
        print("Opção inválida.")
