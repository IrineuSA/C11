#6. Utilizando do DataFrame, calcule a
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
df = pd.DataFrame(np.random.randint(10, 50, size=(5, 4)), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])
print('DataFrame:')
print(df)