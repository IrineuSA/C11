#a) Crie um NumPy Array 2x2 formado apenas por 0’s
#b) Em seguida, adicione um número 1 em uma posição aleatória desta matriz;
#c) Faça uma entrada de dados para solicitar o usuário que faça uma jogada
#(selecione uma posição da matriz)
#I. Se ele selecionar todas as posições em que o número 1 não se encontra, mostre a
#mensagem “Congratulations! You beat the game! :)”
#II. Senão, se dentro das 3 primeiras jogadas ele achar o número 1, mostre a mensagem
#“Game Over! :( Try Again!”

import numpy as np

# a) Crie um NumPy Array 2x2 formado apenas por 0’s
arr = np.zeros((2, 2))
# b) Em seguida, adicione um número 1 em uma posição aleatória desta matriz
pos = np.random.randint(0, 2, size=2)
arr[tuple(pos)] = 1
# c) Faça uma entrada de dados para solicitar o usuário que faça uma jogada
jogadas = 0
while jogadas < 3:
    linha = int(input("Selecione a linha (0 ou 1): "))
    coluna = int(input("Selecione a coluna (0 ou 1): "))
    if arr[linha, coluna] == 1:
        print("Game Over! :( Try Again!")
        break
    else:
        jogadas += 1
        if jogadas == 3:
            print("Congratulations! You beat the game! :)")