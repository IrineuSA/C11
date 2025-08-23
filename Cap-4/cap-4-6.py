#1. Apresente a porcentagem de missões que deram certo
#2. Qual a media de gastos de uma missão especial se baseando em
#missões que possuam valores disponíveis (> 0)?
#3. Encontre quantas missões espaciais neste Dataset foram realizadas
#pelos Estados Unidos (EUA)
#4. Encontre qual foi a missão mais cara realizada pela empresas
#“SpaceX”
#5. Mostre o nome das empresas que já realizaram missões espaciais,
#juntamente com suas respectivas quantidades de missões (use o for
#no final para mostrar as informações)

import numpy as np
ds = np.loadtxt('Cap-4/Data/space.csv',delimiter=';',dtype=str,encoding='utf-8')

#1.
totalMissoes = ds.shape[0]-1
porcentagem_sucesso = (np.sum(ds[1:,7] == 'Success') / totalMissoes) * 100
print(f'Porcentagem de missões que deram certo: {porcentagem_sucesso:.2f}%')

#2.
ds_cost = ds[1:,6].astype(float)
ds_cost_pos = ds_cost[ds_cost>0]
print(f'Média de gastos de uma missão especial: {ds_cost_pos.mean():.2f}M')

#3.
ds_country = ds[1:,4]
ds_count = np.char.count(ds_country, ' USA')
print(f'Missões realizadas por EUA: {np.sum(ds_count)}')

#4.
ds_empresa = ds[1:,1]
ds_spacex = ds_cost[ds_empresa=='SpaceX']
print(f'Missão mais cara da SpaceX: {ds_spacex.max():.2f}M')

#5.
empresas, count = np.unique(ds_empresa, return_counts=True)
for i in range(empresas.shape[0]):
    print(f'Empresa: {empresas[i]} - Quantidade de missões: {count[i]}')
