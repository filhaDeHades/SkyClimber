import estado
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sound import *
from PPlay.mouse import *

estadoJogo = 1

roxo = [190, 117, 216]

fundo = roxo

rato = Mouse()

janela = Window(500, 700)
janela.set_background_color(roxo)


pygame.mixer.music.load("jogo.ogg")
pygame.mixer.music.play(300)
pygame.mixer.music.set_volume(0.1)



while(1):
    if estadoJogo == 1:
        estadoJogo = estado.Menu(janela)
    elif estadoJogo == 2:
        estadoJogo = estado.Creditos(janela)
    elif estadoJogo == 3:
        estadoJogo = estado.Jogo(janela)

    estado.somClique(rato, "som.ogg")
    #if rato.is_button_pressed(1):
        #som.play()


    janela.update()