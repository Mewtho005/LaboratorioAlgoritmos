valor = float(input("Digite o valor do combustível: "))

distribuicao = valor * 0.17
etanol = valor * 0.12
icms = valor * 0.28
impostos = valor * 0.07

refinaria = valor - (distribuicao + etanol + icms + impostos)

print("+ Valor na bomba: R$", valor)
print("- Distribuição e Revenda (17%): R$", distribuicao)
print("- Custo Etanol Anidro (12%): R$", etanol)
print("- ICMS (28%): R$", icms)
print("- CIDE, PIS/PASEP e COFINS (7%): R$", impostos)
print("= Valor da refinaria: R$", refinaria)
