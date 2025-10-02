#2. Por meio do dataset space.csv, trace um gráfico em barras
#mostrando quantas empresas espaciais diferentes os EUA e a CHINA
#possuem;
#Dica: não se esqueça de retirar os resultados repetidos

import pandas as pd
import matplotlib.pyplot as plt

dSpace = pd.read_csv('F:\\Users\\Rockmore\\Documentos\\Inatel\\25-2\\C11\\Cap-6\\Data\\space.csv',delimiter=';')

dUS = dSpace[dSpace['Location'].str.contains(" USA")]
dCN = dSpace[dSpace['Location'].str.contains(" China")]

empresasUS = dUS["Company Name"].nunique()
empresasCN = dCN["Company Name"].nunique()

dados = pd.DataFrame({
    "Country": ["USA", "China"],
    "Companies": [empresasUS, empresasCN]
})
plt.bar(dados["Country"], dados["Companies"], color=["blue","red"])
plt.title("Numero de Empresas Espaciais Distintas")
plt.ylabel("Empresas")
plt.xlabel("País")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()
