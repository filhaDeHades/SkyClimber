#PRECISA ANDAR JUNTO COM O SCROLLING


import random
random.seed()

preda_speed = 0
preda_direction = 1
MAXSIZE = 5

# Numero de linhas da matriz
matrix_x = 3

# Numero de coluna da matriz
matrix_y = int(random.uniform(1,MAXSIZE))


predas = [[0 for x in range(5)] for x in range(3)] #armazena as preda


def preda(i, j, rock_matriz):


    i = 3 #linhas
    # for x e for y percorrem cada elemento da matriz
    for x in range(i):
        for y in range(j):
            # Cria o Sprite
            preda = Sprite(preda_image);
            # Define a posição
            preda.set_position(x * preda.width, y * preda.height)
            # Define a direção do movimento, no caso para baixo
            preda.direction = 1  # 1 = para baixo


            # Coloca preda recém criada na matriz
            preda_matrix[x][y] = preda
