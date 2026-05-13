maior_idade = 0
qtd_especial = 0

olhos_azuis = 0
olhos_verdes = 0
olhos_castanhos = 0

cabelos_loiros = 0
cabelos_castanhos = 0
cabelos_pretos = 0

masculino = 0
feminino = 0

for i in range(15):
    sexo = input("Digite o sexo (M/F): ").upper()
    olhos = input("Digite a cor dos olhos (A/V/C): ").upper()
    cabelos = input("Digite a cor dos cabelos (L/C/P): ").upper()
    idade = int(input("Digite a idade: "))

    if idade > maior_idade:
        maior_idade = idade

    if 18 <= idade <= 35 and olhos == "V" and cabelos == "P":
        qtd_especial += 1

    if olhos == "A":
        olhos_azuis += 1
    elif olhos == "V":
        olhos_verdes += 1
    elif olhos == "C":
        olhos_castanhos += 1

    if cabelos == "L":
        cabelos_loiros += 1
    elif cabelos == "C":
        cabelos_castanhos += 1
    elif cabelos == "P":
        cabelos_pretos += 1

    if sexo == "M":
        masculino += 1
    elif sexo == "F":
        feminino += 1

print("Maior idade do grupo:", maior_idade)
print("Quantidade entre 18 e 35 anos com olhos verdes e cabelos pretos:", qtd_especial)

print("Porcentagem olhos azuis:", (olhos_azuis / 15) * 100, "%")
print("Porcentagem olhos verdes:", (olhos_verdes / 15) * 100, "%")
print("Porcentagem olhos castanhos:", (olhos_castanhos / 15) * 100, "%")

print("Porcentagem cabelos loiros:", (cabelos_loiros / 15) * 100, "%")
print("Porcentagem cabelos castanhos:", (cabelos_castanhos / 15) * 100, "%")
print("Porcentagem cabelos pretos:", (cabelos_pretos / 15) * 100, "%")

print("Porcentagem masculino:", (masculino / 15) * 100, "%")
print("Porcentagem feminino:", (feminino / 15) * 100, "%")
