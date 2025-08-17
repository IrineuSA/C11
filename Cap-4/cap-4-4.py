#Crie uma matriz de tamanho qualquer. Extraia seu número de linhas e
#colunas, multiplique-os, e diga se esta matriz poderia se tornar um vetor
#unidimensional com número par ou ímpar de elementos

import numpy as np
# Criação de uma matriz de tamanho 3x4
matriz = np.random.randint(1, 10, size=(3, 4))
# Extração do número de linhas e colunas
num_linhas, num_colunas = matriz.shape
# Multiplicação do número de linhas e colunas
produto = num_linhas * num_colunas
# Verificação se o produto é par ou ímpar
if produto % 2 == 0:
    print(f"A matriz pode se tornar um vetor unidimensional com número par de elementos: {produto}.")
else:
    print(f"A matriz pode se tornar um vetor unidimensional com número ímpar de elementos: {produto}.")
    