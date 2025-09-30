#1. Por meio do dataset paises.csv, trace dois gráficos de linhas em
# um mesmo plano cartesiano, um mostrando a taxa de mortalidade
#(Deathrate) e outro a taxa de natalidade (Birthrate) dos países da
#América do Norte;

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dPaises = pd.read_csv('C:\\Users\\Irineu\\Documents\\Projetos\\C11\\Cap-6\\Data\\paises.csv',delimiter=';')
dPaises_NA = dPaises[dPaises['Region'] == 'NORTHERN AMERICA']
plt.plot(dPaises_NA['Country'], dPaises_NA['Deathrate'], 'r-', label='Taxa de Mortalidade')
plt.plot(dPaises_NA['Country'], dPaises_NA['Birthrate'], 'b--', label='Taxa de Natalidade')
plt.xlabel('Países da América do Norte')
