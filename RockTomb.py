#PRECISA ANDAR JUNTO COM O SCROLLING
from PPlay.gameobject import *
from PPlay.sprite import *

import random
random.seed()

preda_speed = 0
preda_direction = 1
MAXSIZE = 5

class Rocha:
    GO = None
    coberto = False
    abaixo = False
    vacuo = True
    h = 0
    ox = 0
    oy = 0
    def __init__(self, pos, sprite, qual):

        self.GO = Sprite(sprite[qual])
        self.GO.set_position(pos[0],pos[1])
        self.coberto = False
        self.abaixo = False
        if qual == 0:
            self.vacuo = False


    def colisao(self, player):
        if self.collided_perfect(self, player) == True:
            self.coberto = True
    def draw(self):
        self.GO.draw()

    def set_position(self, x, y):
        self.ox = x
        self.oy = y
        self.GO.x = x
        self.GO.y = y



def vazio(vet):
    for i in range(4):
        if vet[i] == False:
            vet[1].append(sprite[0])

'''def ult_fil(matriz):
    n = 0.0
    r = 0
    for x in range(4):
        for y in range(3):
            r = matriz[x][y].h
            print(r)
            print(n)

            if n < r:
                n = matriz[x][y]'''


def vetor(j, janela):
    imagem = ["imagens/jogo/pedra1-2.png", "imagens/jogo/vazio.png"]

    dividi = janela.width/7
    vet = []
    i = 0
    n = 1
    while(i < 3):
        w = random.randint(0, 1)
        posicao = [((i+n)*dividi)-30, j]
        pedra = Rocha(posicao, imagem, w)
        if ((i+n)*dividi) > pedra.h:
            pedra.h = ((i+n)*dividi)

        n+=1

        vet.append(pedra)
        i+=1
    return vet

def matriz(janela):
    j = 0
    mat =[]
    for j in range(4):
        altura = (j - 1) * 135
        mat.append(vetor(altura, janela))

    return mat

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







