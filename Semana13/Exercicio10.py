def main():
    lotes = []

    for i in range(5):
        codigo = int(input("Digite o código do lote: "))
        lotes.append(codigo)

    busca = int(input("Digite o código que deseja procurar: "))

    if busca in lotes:
        print("Encontrado")
    else:
        print("Não encontrado")

main()
