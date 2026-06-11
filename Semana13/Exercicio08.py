def main():
    codigos = []

    while len(codigos) < 10:
        codigo = int(input("Digite um código RFID: "))

        if codigo > 1000:
            codigos.append(codigo)
        else:
            print("Código inválido! Digite um valor maior que 1000.")

    print("Códigos cadastrados:")
    print(codigos)

main()
