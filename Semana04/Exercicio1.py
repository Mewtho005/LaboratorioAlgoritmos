valor_compra = float(input("Valor da compra: "))
print("1 - A vista (4 porcento de desconto)")
print("2 - Em 12x (2 porcento de juros)")
print("3 - Em 24x (7 porcendo de juros)")
print("4 - em 36x (15 porcento de juros)")
opcao = int(input("Digite a opção: "))

if opcao == 1:
    valor_final = valor_compra * 0.96
    #valor_final = valor_final - (valor_final * 0.25)
    print("Valor da compra:", valor_compra,"Valor com desconto: ", valor_final)
elif opcao == 2:
    valor_final = valor_compra * 1.02
    parcela = valor_final / 12
    print("Valor da compra:", valor_compra,"Valor final:", valor_final, "Valor da parcela:", parcela)
elif opcao == 3:
    valor_final = valor_compra * 1.07
    parcela = valor_final / 24
    print("Valor da compra:", valor_compra, "Valor final:", valor_final, "Valor da parcela:", parcela)
elif opcao == 4:
    valor_final = valor_compra * 1.15
    parcela = valor_final / 36
    print("Valor da compra:", valor_compra, "Valor final:", valor_final, "Valor da parcela:", parcela)
else:
    print("Opção inválida!")
  
