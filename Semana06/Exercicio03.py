soma = 0
menos30 = 0
entre30e60 = 0

for i in range(7):
    tempo = float(input("Digite o tempo do corredor em minutos: "))
    
    soma = soma + tempo

    if tempo < 30:
        menos30 = menos30 + 1

    if tempo >= 30 and tempo <= 60:
        entre30e60 = entre30e60 + 1

media = soma / 7
porcentagem = (entre30e60 / 7) * 100

print("Tempo médio dos corredores:", media)
print("Corredores com menos de 30 minutos:", menos30)
print("Porcentagem entre 30 e 60 minutos:", porcentagem, "%")
