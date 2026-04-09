positivas = 0


resposta = input("Você treinou regularmente nas últimas semanas? (Sim/Não): ")
if resposta == "Sim" or "sim":
    positivas += 1

resposta = input("Participou de treinos longos (acima de 10 km)? (Sim/Não): ")
if resposta == "Sim" or "sim":
    positivas += 1

resposta = input("Seguiu uma dieta especial para a corrida? (Sim/Não): ")
if resposta == "Sim" or "sim":
    positivas += 1

resposta = input("Já competiu em provas oficiais neste ano? (Sim/Não): ")
if resposta == "Sim":
    positivas += 1

resposta = input("Conta com acompanhamento de treinador ou equipe? (Sim/Não): ")
if resposta == "Sim" or "sim":
    positivas += 1

if positivas == 5:
    print("Classificação: Atleta de Elite (pronto para o pódio!)")
elif positivas == 3 or positivas == 4:
    print("Classificação: Atleta Competitivo (tem boas chances de se destacar)")
elif positivas == 2:
    print("Classificação: Participante Casual (ainda precisa de mais treino)")
else:
    print("Classificação: Não Preparado (talvez seja melhor assistir da arquibancada)")
