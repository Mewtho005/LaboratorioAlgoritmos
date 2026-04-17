chute = float(input("Digite seu chute: "))
numero = 67

if chute == numero:
    print("Parabéns! Você descobriu a quantidade de oliveiras!")
elif chute > numero:
    print("Há menos oliveiras, tente um número menor")
elif chute < numero:
    print("Há mais oliveiras, tente um número maior")
