#Faça um programa que leia o nome e peso de 3 pessoas e no final
#mostre o nome da pessoa mais pesada e a mais leve

pessoas = []
for i in range(3):
    nome = input(f"Nome da pessoa {i + 1}: ")
    peso = float(input(f"Peso da pessoa {i + 1} (kg): "))
    pessoas.append({'nome': nome, 'peso': peso})

maisPesada = max(pessoas, key=lambda x: x['peso'])
maisLeve = min(pessoas, key=lambda x: x['peso'])
print(f"\nPessoa mais pesada: {maisPesada['nome']}")
print(f"Pessoa mais leve: {maisLeve['nome']}")