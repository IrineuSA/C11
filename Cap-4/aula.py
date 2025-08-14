# importando numpy
import numpy as np

# array unidimensional
arr = np.array([10, 20, 30])

#print(arr)
#print(type(arr))

# array bidimensional (matriz)
mtz = np.array([[10, 20, 30], [40, 50, 60]])
#print(mtz)

# funções p estruturar numpy array
# array 1D de 1s
arr = np.ones(10)
#print(arr)

# array 2D de 0s com reshape
#mtz = np.zeros(10).reshape(5,2)
mtz = np.zeros([5,2])

#print(mtz)

# arange
arr = np.arange(10, 101, 10)
#print(arr)
# menor valor
#print(arr.min())
# maior valor
#print(arr.max())
# media
#print(arr.mean())
# indice do maior
#print(arr.argmax())

# operações com np
arr1 = np.arange(1,10,1)
arr2 = np.arange(9, 0, -1)
#print(arr1)
#print(arr2)
#print(arr1 + arr2)

# concatenar
#print(np.concatenate([arr1, arr2]))

# operações com matrizes
mtz = np.array([50, 10, 100, 60, 25, 100, 75, 80, 100]).reshape(3,3)
#print(mtz)

#print(mtz.sum(axis=1).reshape(3,1))
#print(mtz.sum(axis=0).reshape(1,3))
#print(mtz.sum(axis=0)[2])

# broadcasting
#print(mtz/10)

# semente aleatoria
np.random.seed(10)
arr = np.random.randint(1, 10, 10)
print(arr)
print(np.unique(arr, return_counts = True))
