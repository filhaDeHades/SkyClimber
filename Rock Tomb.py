#PRECISA ANDAR JUNTO COM O SCROLLING
from PPlay.gameobject import *
from PPlay.sprite import *

import random
random.seed()

preda_speed = 0
preda_direction = 1
MAXSIZE = 5


predas = [[0 for x in range(5)] for x in range(3)] #armazena as pedras


def preda(i, j, rock_matriz):

    i = 3 #linhas
    pedra = GameObject()
    pedra = Sprite("imagens/jogo/pedra1-2.png")
    nada = GameObject()
    nada = Sprite("imagens/jogo/vazio.png")
    opcoes = (pedra, nada)

    # for x e for y percorrem cada elemento da matriz
    for x in range(i):
        for y in range(j):
            opcao = random.randint(0, 1)
            if x == 2:
                if rock_matriz[x][0] == opcoes[1] or rock_matriz[x][1] == opcoes[1]:
                    opcao = random.randint(0, 1)
                else:
                    opcao = 0
            # Cria o Sprite

            # Define a posição
            espaco = 500 / (opcoes[opcao].width)+(2 * (opcoes[opcao].width + 50))
            pedra.set_position(x * (opcoes[opcao].width+50), y * (opcoes[opcao].height+20)+50)
            # Define a direção do movimento, no caso para baixo
            pedra.direction = 1  # 1 = para baixo


            # Coloca preda recém criada na matriz
            rock_matriz[x][y] = opcoes[opcao]
