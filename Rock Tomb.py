#PRECISA ANDAR JUNTO COM O SCROLLING
from PPlay.gameobject import *
from PPlay.sprite import *

import random
random.seed()

preda_speed = 0
preda_direction = 1
MAXSIZE = 5

# Numero de linhas da matriz
matrix_x = [int(random.uniform(1,MAXSIZE))]

# Numero de coluna da matriz
matrix_y = [3]


predas = [[0 for x in range(5)] for x in range(3)] #armazena as preda


def preda(i, j, rock_matriz):


    i = 3 #linhas
    # for x e for y percorrem cada elemento da matriz
    for x in range(i):
        for y in range(j):
            # Cria o Sprite
            preda = Sprite(imagens/jogo/pedra.png);
            # Define a posição
            preda.set_position(x * preda.width, y * preda.height)
            # Define a direção do movimento, no caso para baixo
            preda.direction = 1  # 1 = para baixo


            # Coloca preda recém criada na matriz
            rock_matriz[x][y] = preda
