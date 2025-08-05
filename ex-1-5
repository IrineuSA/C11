#Faça um programa que leia um número entre 1000 e 9999 e mostre na tela
#• qual o número da unidade
#• número da dezena
#• número da centena
#• E número do milhar

import math

num = int(input("Entre com um número entre 1000 e 9999: "))
while num < 1000 or num > 9999:
    num = int(input("Número invalido. Entre com um número entre 1000 e 9999: "))
    
unidade = num % 10
print(f"Unidade: {unidade}")
dezena = (num // 10) % 10
print(f"Dezena: {dezena}")
centena = (num // 100) % 10
print(f"Centena: {centena}")
milhar = (num // 1000) % 10
print(f"Milhar: {milhar}")