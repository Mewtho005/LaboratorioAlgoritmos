plantacao_A = 80000
plantacao_B = 200000

taxa_A = 0.03      
taxa_B = 0.015     

anos = 0

while plantacao_A < plantacao_B:
    plantacao_A *= (1 + taxa_A)
    plantacao_B *= (1 + taxa_B)
    anos += 1

print ("Anos necessários:", anos)
print ("Plantação A: ", plantacao_A)
print ("Plantação B: ", plantacao_B)
