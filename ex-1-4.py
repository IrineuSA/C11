#Desenvolva um script que pergunte a distância de uma viagem em
#Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens
#até 200Km e R$0.45 para viagens mais longas

import math

dist = int(input("Distância da viagem em Km: "))
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print(f"Preço da passagem: R$ {preco:.2f}")
