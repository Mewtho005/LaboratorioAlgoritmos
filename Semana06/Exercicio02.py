contador = 0
codigo = -1

while codigo != 0:
    codigo = int(input("Digite o código do brinquedo (0 para encerrar): "))

    if codigo == 1040:
        contador = contador + 1

print("O código 1040 foi digitado", contador, "vezes.")
