opcao = int(input("Escolha o kit (1-Básico, 2-Plus, 3-Premium): "))
valor = float(input("Digite o valor entregue: "))

if opcao == 1:
    preco = 100
    nome = "Kit Básico"

elif opcao == 2:
    preco = 120
    nome = "Kit Plus"

elif opcao == 3:
    preco = 150
    nome = "Kit Premium"

else:
    print("Opção inválida")
    preco = 0

if valor >= preco:
    troco = valor - preco
    print("Você escolheu:", nome)
    print("Pagamento suficiente")
    print("Troco:", troco)
else:
    falta = preco - valor
    print("Valor insuficiente")
    print("Falta:", falta)
