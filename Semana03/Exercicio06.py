altura = float(input("Digite sua altura: "))
sexo = (input("Digite seu sexo: H ou M: ")).upper()

if sexo == "H":
    peso_homem = 72.7 * altura - 58
    print("Peso ideal", peso_homem)
if sexo == "M":
    peso_muie = 62.1 * altura - 44.7
    print("Peso ideal", peso_muie)
