# importando numpy
import numpy as np

# slicing em np arrays
# criando array 2D
#mtz = np.arange(1,10,1).reshape(3,3)
#print(mtz)
# extraindo uma linha (3a linha)
#print(mtz[2])
# extraindo apenas uma coluna (2a e 3a coluna)
#print(mtz[:,1:])

# condicionais no np array
#print(mtz>5)
#print(mtz[mtz>5])
#print(mtz[mtz%2==0])

# tratamento textual (subpacote char)
#arr = np.array(['Goku','Goten','Gohan','Trunks','Bulma'])
#print(arr)
#print(np.char.find(arr,'Go'))
#print(np.char.find(arr,'ha'))
#print(np.char.find(arr,'Go')>=0)
#print(arr[np.char.find(arr,'Go')>=0])
#arr = np.char.upper(arr)
#print(np.char.find(arr,'Go'))
#print(np.char.find(arr,'GO'))

# importando datasets np 
ds = np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')
#print(ds)
# colunas do dataset
print(ds[0,:])

# calculando media de uma missao
#slicing p extrair a coluna custo
ds_cost = ds[1:,6]
# transformando os valores em float
ds_cost = ds_cost.astype(float)
print(ds_cost.mean())
