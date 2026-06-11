def main():
    lotes = []

    for i in range(5):
        codigo = int(input("Digite o código do lote: "))
        lotes.append(codigo)

    if len(lotes) == len(set(lotes)):
        print("Distintos")
    else:
        print("Há duplicatas")

main()
