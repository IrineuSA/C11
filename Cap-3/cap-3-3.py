#Faça um programa que leia o nome e a média de um aluno e guarde-
#os em um dicionário. Em seguida, a partir da média (para ser
#aprovado deve ter média >=50), gere a situação final do aluno (‘AP’
#ou ‘RP’), que também deve ser guardada neste dicionário. No final,
#mostre todo o conteúdo deste dicionário;

aluno = {}
nome = input("Nome do aluno: ")
media = float(input("Média: "))
aluno['nome'] = nome
aluno['media'] = media
aluno['situacao'] = 'AP' if media >= 50 else 'RP'
print("\nDados do aluno:")
print(aluno.values())
