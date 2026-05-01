soma_salarios = 0
mais_novo = 0
mais_velho = 0
atacantes_10000 = 0
qtd_atacantes = 0
qtd_defensores = 0

for i in range(10):
    idade = int(input("Digite a idade do jogador: "))
    posicao = input("Digite a posição (A para atacante / D para defensor): ")
    salario = float(input("Digite o salário do jogador: "))

    soma_salarios = soma_salarios + salario

    if i == 0:
        mais_novo = idade
        mais_velho = idade
    else:
        if idade < mais_novo:
            mais_novo = idade

        if idade > mais_velho:
            mais_velho = idade

    if posicao == "A":
        qtd_atacantes = qtd_atacantes + 1

        if salario <= 10000:
            atacantes_10000 = atacantes_10000 + 1

    elif posicao == "D":
        qtd_defensores = qtd_defensores + 1

media_salarios = soma_salarios / 10

print("Média dos salários:", media_salarios)
print("Jogador mais novo:", mais_novo)
print("Jogador mais velho:", mais_velho)
print("Atacantes com salário até R$10.000,00:", atacantes_10000)
print("Quantidade de atacantes:", qtd_atacantes)
print("Quantidade de defensores:", qtd_defensores)
