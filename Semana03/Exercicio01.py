salaro = float(input("Tempo de trabaio:"))

valor = salaro * 35
if salaro < 1000:
    salaro_ajustado = valor + 300
    print(salaro_ajustado)
else:
    print(valor)
