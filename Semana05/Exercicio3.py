litros = float(input("Quantidade de litros abastecidos: "))
valor_total = float(input("Valor total da compra: "))


desconto = 0

if litros >= 20 and valor_total > 100:
    desconto = valor_total * 0.10  
elif litros >= 20 and valor_total <= 100:
    desconto = valor_total * 0.05 
else:
    desconto = 0  


valor_final = valor_total - desconto


print("Desconto aplicado: R$", round(desconto, 2))
print("Valor final a pagar: R$", round(valor_final, 2))
