nome = input("Seu nome: ")
salario = float(input("Digite seu salario: "))
anos_servico = int(input("Tempo de serviço: "))

if anos_servico >= 5 and salario <= 2000:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05
salario_final = salario + aumento
print("Nome:", nome)
print("Aumento:", aumento)
print("Anos de serviço:", anos_servico)
print("Salario Final:", salario_final)
