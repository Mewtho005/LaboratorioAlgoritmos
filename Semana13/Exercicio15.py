lotes = []


def inserir_lote():

    codigo = int(input("Digite o código do lote: "))

    if codigo % 2 != 0:
        print("ERRO: Apenas códigos pares são permitidos!")

    else:
        lotes.append(codigo)
        print("Lote inserido com sucesso!")


def listar_lotes():

    if len(lotes) == 0:
        print("Nenhum lote cadastrado.")

    else:
        print("Lotes cadastrados:")

        for dois in range(len(lotes)):
            print(lotes[dois])


def retirar_lote():

    codigo = int(input("Digite o código do lote para remover: "))

    encontrado = False

    for sono in range(len(lotes)):

        if lotes[sono] == codigo:
            lotes.pop(sono)
            encontrado = True
            print("Lote removido com sucesso!")
            break

    if encontrado == False:
        print("Lote não encontrado.")


def limpar_lotes():

    while len(lotes) > 0:
        lotes.pop()

    print("Todos os lotes foram removidos.")


def contar_maiores():

    x = int(input("Digite o valor X: "))

    contador = 0

    for queijo in range(len(lotes)):

        if lotes[queijo] > x:
            contador += 1

    print(f"Quantidade de lotes maiores que {x}: {contador}")


def verificar_codigo():

    codigo = int(input("Digite o código para buscar: "))

    encontrado = False

    for trinca in range(len(lotes)):

        if lotes[trinca] == codigo:
            encontrado = True

    if encontrado:
        print("O código está presente no array.")

    else:
        print("O código NÃO está presente no array.")


def maior_menor():

    if len(lotes) == 0:
        print("O array está vazio.")

    else:

        maior = lotes[0]
        menor = lotes[0]

        for to in range(len(lotes)):

            if lotes[to] > maior:
                maior = lotes[to]

            if lotes[to] < menor:
                menor = lotes[to]

        print("Maior código:", maior)
        print("Menor código:", menor)


def menu():

    while True:

        print("=== MENU DE GERENCIAMENTO DE LOTES ===")
        print("1 - Inserir lote")
        print("2 - Listar lotes")
        print("3 - Retirar um lote")
        print("4 - Limpar todos os lotes")
        print("5 - Contar lotes maiores que X")
        print("6 - Verificar se um código está presente")
        print("7 - Encontrar maior e menor código")
        print("8 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_lote()

        elif opcao == "2":
            listar_lotes()

        elif opcao == "3":
            retirar_lote()

        elif opcao == "4":
            limpar_lotes()

        elif opcao == "5":
            contar_maiores()

        elif opcao == "6":
            verificar_codigo()

        elif opcao == "7":
            maior_menor()

        elif opcao == "8":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida!")


menu()
