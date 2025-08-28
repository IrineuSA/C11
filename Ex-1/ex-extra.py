#Faça um slicing no dataset para mostrar apenas o País (Country), Região
#(Region), População (Population) e Area (Area (sq. mi.)) dos países contidos
#nele;

#Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo
#este dataset;

#Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo
#este dataset

#Conte quantos países são da América do Norte (NORTHERN AMERICA)
#segundo este dataset;

#Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB)
#possui a maior renda per capita (GDP ($ per capita));

import numpy as np
ds = np.loadtxt('Ex-1/Data/paises.csv',delimiter=';',dtype=str,encoding='utf-8')

#1.
ds_slice = ds[1:,[0,1,2,3]]
print('País | Região | População | Área')
print(ds_slice)

#2.
ds_reg = ds[1:,1]
reg, count = np.unique(ds_reg, return_counts=True)
print(f'Diferentes Regiões: {reg.shape[0]}')
print(reg)

#3.
ds_lit = ds[1:,5].astype(float)
print(f'Taxa média de alfabetização: {ds_lit.mean():.2f}%')

#4.
ds_na = ds[1:,1]
ds_count = np.char.count(ds_na, 'NORTHERN AMERICA')
print(f'Países da América do Norte: {np.sum(ds_count)}')

#5.
ds_sa = np.char.strip(ds[1:,1]) == 'LATIN AMER. & CARIB'
gdp = ds[1:,8].astype(float)
gdp_sa = gdp[ds_sa]
ds_sa_max = ds[1:,0][ds_sa]
max_gdp = np.argmax(gdp_sa)
print(f'país da América do Sul e Caribe c/ maior GDP: {ds_sa_max[max_gdp].strip()} ({gdp_sa[max_gdp]:.2f})')