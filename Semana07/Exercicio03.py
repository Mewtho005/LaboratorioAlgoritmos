total_oliveiras = int(input("Digite o número total de oliveiras: "))
fileiras = int(input("Digite o número de fileiras: "))

oliveiras_por_fileira = total_oliveiras // fileiras
sobra = total_oliveiras % fileiras

print("Oliveiras por fileira: ", oliveiras_por_fileira)
print("Sobra de mudas:", sobra)
