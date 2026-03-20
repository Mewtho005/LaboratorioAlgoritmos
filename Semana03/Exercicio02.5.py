nasceu_em = int(input("Nasceu que ano:"))

idade = 2026 - nasceu_em
print("Nasceu em que ano:", idade)
if idade > 16:
    print("Pode votar")
else:
    print("Não pode votar")
