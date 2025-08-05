#1. Crie um programa que leia seu nome completo e mostre:
#• Seu nome com todas as letras maiúsculas
#• Seu nome com todas as letras minúsculas
#• Quantas letras ao todo tem seu nome
#• E como seria se trocássemos seu último nome para “do Inatel”

nome = input("Entre com seu nome: ")
print(f"Em maíusculas: {nome.upper()}")
print(f"Em minúsculas: {nome.lower()}")
print(f"Número de letras (sem espaços): {len(nome.replace(' ', ''))}")
nomeSep = nome.split()
if nomeSep:
    nomeSep[-1] = "do Inatel"
    nomeNovo = ' '.join(nomeSep)
    print(f"{nomeNovo}")
else:
    print("Entre também um sobrenome")