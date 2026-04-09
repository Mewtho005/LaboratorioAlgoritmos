morango = float(input("Digite a quantidade de morangos (Kg): "))
maca = float(input("Digite a quantidade de maçãs (Kg): "))


if morango <= 5:
    preco_morango = morango * 2.5
else:
    preco_morango = morango * 2.2

if maca <= 5:
    preco_maca = maca * 1.8
else:
    preco_maca = maca * 1.5

total = preco_morango + preco_maca
peso_total = morango + maca

if peso_total > 8 or total > 25:
    total = total * 0.9

print("Valor a pagar: R$", total)
