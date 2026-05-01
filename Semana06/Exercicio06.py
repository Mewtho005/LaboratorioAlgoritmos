contador = 0
i = 1

while i <= 10:
    temperatura = float(input("Digite a temperatura da cidade: "))

    if temperatura >= 15 and temperatura <= 25:
        contador = contador + 1

    i = i + 1

print("Quantidade de cidades com temperatura entre 15°C e 25°C:", contador)
