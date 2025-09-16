#1. Carregue o Dataset paises.csv e em seguida mostre:
#a.Quais são os países da OCEANIA;
#b.Quantos países são da OCEANIA;
#Dica: para busca de padrões textuais no Pandas, use métodos da subclasse str da
#Series. Ex: series.str.contains(‘texto’)
#2. Encontre o nome e a região do país que possui a maior população segundo este
#Dataset;
#3. Agrupe os países por Regiões. Em seguida, mostre a média de alfabetização
#(Literacy (%)) de cada região do planeta;
#4. Busque o nome de todos os países do Dataset que não possuem costa marítima
#(Coastline (coast/area ratio) == 0) e guarde-os em um novo arquivo chamado
#noCoast.csv;
#5. Faça uma função que receba a taxa de mortalidade de cada país (Deathrate) e
#retorne o texto ‘Balanced’ caso o valor seja < 9 e ‘Urgent’ caso contrário. Em
#seguida, crie um campo no Dataset chamado ‘Humanitarian Help’ que receba estes
#valores para cada país. No final, mostre o Dataset para verificar se a inserção da nova
#coluna foi feita com sucesso.

import pandas as pd
import numpy as np
#1.
dfPaises = pd.read_csv('Cap-5/Data/paises.csv',delimiter=';')
print(dfPaises.head())
dfOceania = dfPaises[dfPaises['Region'].str.contains('OCEANIA')]
print(dfOceania)
print(f'Quantidade de países na OCEANIA: {dfOceania.shape[0]}')
#2.
dfMaiorPop = dfPaises[dfPaises['Population'] == dfPaises['Population'].max()]
print(f'País com maior população: {dfMaiorPop[["Country","Region"]]}')
#3.
dfMediaAlf = dfPaises.groupby('Region')['Literacy (%)'].mean()
print(f'Media de alfabetização por região:\n{dfMediaAlf}')
#4.
dfLL = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]
dfLL.to_csv('Cap-5/Data/noCoast.csv',index=False)
print(f'Países sem costa marítima:\n{dfLL}')
#5.
def checaDr(deathrate):
    if deathrate < 9:
        return 'Balanced'
    else:
        return 'Urgent'
dfPaises['Humanitarian Help'] = dfPaises['Deathrate'].apply(checaDr)
print(dfPaises)
print(dfPaises['Humanitarian Help'].value_counts())
dfPaises.to_csv('Cap-5/Data/paises_atualizado.csv',index=False)
dfPaises = pd.read_csv('Cap-5/Data/paises_atualizado.csv',delimiter=';')
print(dfPaises)