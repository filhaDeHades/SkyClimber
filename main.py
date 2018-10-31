import estado
from PPlay.window import *
from PPlay.keyboard import *
estadoJogo = 1

roxo = [190, 117, 216]

fundo = roxo

janela = Window(500, 700)
janela.set_background_color(roxo)

while(1):
    if estadoJogo == 1:
        estadoJogo = estado.Menu(janela)
    elif estadoJogo == 2:
        estadoJogo = estado.Creditos(janela)
    elif estadoJogo == 3:
        estadoJogo = estado.Jogo(janela)
    janela.update()