#6. Utilizando do DataFrame exemplo do tópico 5.3 deste material, calcule a
#média dos elementos da coluna X que são menores que 30;
#7. Utilizando do mesmo DataFrame, apresente a média dos elementos da
#linha D usando a função loc() como base e a soma dos elementos da linha E
#usando a função iloc() como base;
#8. Faça um Slicing na matriz mostrando apenas as linhas A, C e E
#juntamente com as colunas X e Y. Em seguida, mostre qual seria a soma dos
#elementos de cada uma destas linhas e cada uma destas colunas.

import pandas as pd
import numpy as np

#6.
df = pd.DataFrame(index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'],data=([10, 37, 16, 1], [29, 26, 30, 49],[30, 9, 10, 1],[43, 41, 37, 17],[37, 48, 12, 25]))
print('DataFrame')
print(df)
medMenor30 = df[df['X'] < 30]['X'].mean()
print(f'\nMedia dos elementos da coluna X menores que 30: {medMenor30}')

#7.
mediaD = df.loc['D'].mean()
somaE = df.iloc[4].sum()
print(f'\nMédia dos elementos da linha D: {mediaD}')
print(f'Soma dos elementos da linha E: {somaE}')

#8.
slicing = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print('\nSlicing das linhas A C e E com colunas X e Y')
print(slicing)
somaLinhas = slicing.sum(axis=1)
somaColunas = slicing.sum(axis=0)
print('\nSoma dos elementos das linhas:')
print(somaLinhas)
print('\nSoma dos elementos das colunas:')
print(somaColunas)
