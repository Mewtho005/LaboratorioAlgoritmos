ingressos = 100
opcao = 0

while opcao != 4:
    print("1 - Diminuir quantidade de ingressos")
    print("2 - Adicionar ingressos extras")
    print("3 - Mostrar ingressos disponíveis")
    print("4 - Encerrar")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        qtd = int(input("Quantos ingressos deseja diminuir? "))

        if qtd <= ingressos:
            ingressos = ingressos - qtd
            print("Ingressos restantes:", ingressos)
        else:
            print("Não há ingressos suficientes.")

    elif opcao == 2:
        qtd = int(input("Quantos ingressos extras deseja adicionar? "))
        ingressos = ingressos + qtd
        print("Total de ingressos agora:", ingressos)

    elif opcao == 3:
        print("Ingressos disponíveis:", ingressos)

    elif opcao == 4:
        print("Sistema encerrado.")

    else:
        print("Opção inválida.")
