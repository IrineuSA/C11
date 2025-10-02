#1. Por meio do dataset paises.csv, trace dois gráficos de linhas em
# um mesmo plano cartesiano, um mostrando a taxa de mortalidade
#(Deathrate) e outro a taxa de natalidade (Birthrate) dos países da
#América do Norte;

import pandas as pd
import matplotlib.pyplot as plt

dPaises = pd.read_csv('C:\\Users\\Irineu\\Documents\\Projetos\\C11\\Cap-6\\Data\\paises.csv',delimiter=';')
dPaisesNA = dPaises[dPaises["Region"].str.contains("NORTHERN AMERICA")]

plt.plot(dPaisesNA["Country"], dPaisesNA["Birthrate"], marker='o', label="Taxa de Natalidade")
plt.plot(dPaisesNA["Country"], dPaisesNA["Deathrate"], marker='s', label="Taxa de Mortalidade")
plt.title("Taxa de Natalidade e Mortalidade - América do Norte")
plt.xlabel("Países")
plt.ylabel("Taxa (%)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()