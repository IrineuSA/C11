#Crie uma matriz de tamanho 4x4 formada por números aleatórios inteiros
#entre 1 e 50 (use seed = 10 antes)
#a) Mostre o resultado da média de cada linha e cada coluna da matriz
#gerada
#b) Apresente o maior valor das médias das linhas e também das colunas
#c) Mostre a quantidade de aparições de cada um dos números gerados na
#matriz. Em seguida, mostre apenas os números que aparecem 2 vezes

import numpy as np

np.random.seed(10)
mtz = np.random.randint(1, 51, size=(4, 4))
# a) Cálculo da média de cada linha e cada coluna
mediaLinhas = np.mean(mtz, axis=1)
mediaColunas = np.mean(mtz, axis=0)
# b) Apresentando o maior valor das médias das linhas e colunas
MaxMediaLinhas = np.max(mediaLinhas)
MaxMediaColunas = np.max(mediaColunas)
print("Matriz:", mtz)
print("Média de cada linha:", MaxMediaLinhas)
print("Média de cada coluna:", MaxMediaColunas)
print("Maior média das linhas:", MaxMediaLinhas)
print("Maior média das colunas:", MaxMediaColunas)
# c) Contagem de aparições de cada número na matriz
unicos, contagem = np.unique(mtz, return_counts=True)
aparicoes = dict(zip(unicos, contagem))
# Mostrando apenas os números que aparecem 2 vezes
numAgain = {num: count for num, count in aparicoes.items() if count == 2}
print("Aparições de cada número:", aparicoes)
print("Números que aparecem 2 vezes:", numAgain)
