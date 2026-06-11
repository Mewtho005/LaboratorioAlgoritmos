def inverterLotes(lotes):
    for i in range(len(lotes) - 1, -1, -1):
        print(lotes[i])

def main():
    lotes = []

    for i in range(10):
        codigo = int(input("Digite o código do lote: "))
        lotes.append(codigo)

    print("Lotes em ordem inversa:")
    inverterLotes(lotes)

main()
