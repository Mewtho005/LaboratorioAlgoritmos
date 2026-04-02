valor = float(input("Digite o valor do ingresso: "))
opcao = int(input("Escolha a opção (1-normal, 2-estudante, 3-criança, 4-idoso): "))

if opcao == 1:
    total = valor

elif opcao == 2:
    total = valor * 0.5

elif opcao == 3:
    total = valor * 0.4

elif opcao == 4:
    total = valor * 0.6

else:
    print("Opção inválida")
    total = 0

print("Valor a pagar:", total)
