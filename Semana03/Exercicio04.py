nasceu_em = int(input("Nasceu que ano:"))

idade = 2026 - nasceu_em
print("Nasceu em que ano:", idade)
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
