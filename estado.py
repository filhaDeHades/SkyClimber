from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.keyboard import *
from time import sleep

roxo = [190, 117, 216]
vermelho = [234, 148, 124]
azul = [27, 110, 193]
laranja = [232, 144, 90]

n = 0.2 #tempo de delay dos botoes
borda = 10
rato = Mouse()
tecla = Keyboard()

texto = ["Créditos:", "Música:", "...", "...", "...", "Bibliotecas:", "PPlay", "Pygame"]
inimigos = []


def Texto(frase, windows):
    j = 0
    for i in frase:
        windows.draw_text(i, (windows.width / 2)-(len(i)*11), borda+j, size=50, color=azul, font_name="Arial",
                          bold=True, italic=False)
        j+=70

def Clique(botao):
    if rato.is_over_object(botao):
        botao.set_curr_frame(1)
        if rato.is_button_pressed(1):
            return 0
    else:
        botao.set_curr_frame(0)

def Menu(windows):
    windows.set_background_color(roxo)

    titulo = GameObject()
    titulo = Sprite("imagens/titulo1.png")
    titulo.set_position(windows.width - titulo.width, borda)

    play = GameObject()
    play = Sprite("imagens/play2.png", frames=2)
    play.set_position((windows.width/2)-(play.width/2), (windows.height/2)-(play.height/2))

    creditos = GameObject()
    creditos = Sprite("imagens/creditos2.png", frames=2)
    creditos.set_position((windows.width/2)-(creditos.width/2), (windows.height - creditos.height)-borda)

    while(1):
        titulo.draw()
        play.draw()
        creditos.draw()
        if Clique(play) == 0:
            sleep(n)
            return 3
        if Clique(creditos) == 0:
            sleep(n)
            return 2
        windows.update()

def Creditos(windows):
    windows.set_background_color(vermelho)

    voltar = GameObject()
    voltar = Sprite("imagens/voltar2.png", frames=2)
    voltar.set_position((windows.width/2)-(voltar.width/2), (windows.height - voltar.height)-borda)

    while(1):
        Texto(texto, windows)
        voltar.draw()
        if Clique(voltar) == 0:
            sleep(n)
            return 1


        windows.update()

def Jogo(windows):
    windows.set_background_color(laranja)
    if tecla.key_pressed("esc") == 1:
        exit()
    while(1):
        windows.update()