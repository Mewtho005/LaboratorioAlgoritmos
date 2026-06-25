def menu():
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Saldo")
    print("4 - Sair")

    return int(input("Escolha: "))

def main():
    while True:
        opcao = menu()

        if opcao == 1:
            print("Depositar")

        elif opcao == 2:
            print("Sacar")

        elif opcao == 3:
            print("Saldo")

        elif opcao == 4:
            print("Encerrando...")
            break

        else:
            print("Opção inválida")

main()
