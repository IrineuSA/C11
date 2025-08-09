#Desenvolva um programa que leia o nome, idade e sexo de n pessoas.
#No final, mostre: A média de idade do grupo; Quantas mulheres têm menos de 20 anos.

pessoas = []
while True:
    nome = input("Nome da pessoa (ou 'FIM' para sair): ")
    if nome.upper() == 'FIM':
        break
    idade = int(input("Idade da pessoa: "))
    sexo = input("Sexo da pessoa (M/F): ").upper()
    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})
    
mediaIdade = sum(p['idade'] for p in pessoas) / len(pessoas) if pessoas else 0
print(f"\nMédia de idade do grupo: {mediaIdade:.2f} anos")
mulheres20 = sum(1 for p in pessoas if p['sexo'] == 'F' and p['idade'] < 20)
print(f"Mulheres com menos de 20 anos: {mulheres20}")
