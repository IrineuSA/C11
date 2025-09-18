import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#x = np.array([1,2,3,4,5])
#y = x*2
#plt.plot(x,y)
#plt.show

# Novo eixo y
#y2 = x*x

# Explicando os eixos x e y
#plt.xlabel('Valores de x')
#plt.ylabel('Valores de y')

# Formatando o estilo dos plots
#plt.plot(x,y, 'r-',x,y2,'b--',linewidth=5,markersize=20)

# Plots multiplos
#x=np.array([1,2,3,4,5])
#y=x*2
#y2=x*x

# Criando a matriz de subplots
#plt.subplot(1,2,1)
#plt.title('Linear')
#plt.plot(x,y,'r-')

#plt.subplot(1,2,2)
#plt.title('Exponencial')
#plt.plot(x,y2,'b--')

# Grafico de Dispersao (scatter plot)
dPaises = pd.read_csv('C:\\Users\\Irineu\\Documents\\Projetos\\C11\\Cap-6\\Data\\paises.csv',delimiter=';')

#print(dPaises.head(3))
#dPaises2 = dPaises.nlargest(6,'Area (sq. mi.)')

#plt.scatter(dPaises2['Country'], dPaises2['GDP ($ per capita)'], s=dPaises2['Area (sq. mi.)']/10000)

# Grafico em barras (bar plot)
#dfBiggestGDP = dPaises.nlargest(5,'GDP ($ per capita)')
#dfBiggestGDP_country = dfBiggestGDP['Country']
#dfBiggestGDP_gdp = dfBiggestGDP['GDP ($ per capita)']
#plt.bar(dfBiggestGDP_country,dfBiggestGDP_gdp,color='green')

# Grafico em torta (pie plot)
dfPaisesNoCoast = dPaises[dPaises['Coastline (coast/area ratio)'] ==0]
qtPaisesNoCoast = len(dfPaisesNoCoast)
qtPaisesCoast = len(dPaises) - qtPaisesNoCoast
plt.pie(x=[qtPaisesCoast, qtPaisesNoCoast],labels=['% Paises Com Costa', '%Paises Sem Costa'],autopct='%1.1f%%')
