valor = float(input("Digite o valor: "))
opcao = int(input("1-à vista, 2-2x, 3-3x: "))

if opcao == 1:
    print("Pagamento à vista: R$", valor)
elif opcao == 2:
    parcela = valor / 2
    print("2 parcelas de: R$", parcela)
elif opcao == 3:
    parcela = valor / 3
    print("3 parcelas de: R$", parcela)
else:
    print("Opção invalida")
