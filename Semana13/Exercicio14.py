def main():
    etiquetas = []

    while len(etiquetas) < 15:
        codigo = int(input("Digite o código da etiqueta/RFID: "))

        if codigo in etiquetas:
            print("Código já cadastrado! Digite outro.")
        else:
            etiquetas.append(codigo)

    print("Etiquetas cadastradas:")
    print(etiquetas)

main()
