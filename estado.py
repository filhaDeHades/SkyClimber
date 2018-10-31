from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.keyboard import *
from PPlay.sound import *
from time import sleep

roxo = [190, 117, 216]
vermelho = [234, 148, 124]
azul = [27, 110, 193]
laranja = [232, 144, 90]

n = 0.2 #tempo de delay dos botoes
posF = 0
borda = 10
velocFundo = 3
nuvem = velocFundo/0.8

rato = Mouse()
tecla = Keyboard()

janela = Window(500, 700)
janela.set_background_color(roxo)

texto = ["Créditos:", "Música:", "...", "...", "...", "Bibliotecas:", "PPlay", "Pygame"]
inimigos = []


def rolar1(bg1, bg2, bg3, bg4, fv, windows):
    bg1.y -= fv * (windows.delta_time()+0.5)
    bg2.y -= fv * (windows.delta_time()+0.5)
    bg3.y -= fv * (windows.delta_time()+0.5)
    bg4.y -= fv * (windows.delta_time()+0.5)

    if bg4.y <= 0:
        bg1.y = bg1.height
        bg2.y = 2 * bg1.height
        bg3.y = 3 * bg1.height
        if (bg4.y + bg4.height) <= 0:
            bg4.y = 4 * bg1.height

    bg4.draw()
    bg3.draw()
    bg2.draw()
    bg1.draw()

def rolar2(bg1, bg2, fv, windows):
    bg1.y += fv * (windows.delta_time() + 0.5)
    bg2.y += fv * (windows.delta_time() + 0.5)

    if bg2.y <= 0:
        bg1.y = posF
        bg2.y = bg1.height

    bg2.draw()
    bg1.draw()

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

    mont = GameImage("imagens/fundo/fundoMontanha.png")
    mont.y = posF

    grad1 = GameImage("imagens/fundo/gradiente2.png")
    grad1.y = posF

    grad2 = GameImage("imagens/fundo/gradiente4.png")
    grad2.y = posF + grad1.height

    grad3 = GameImage("imagens/fundo/gradiente3.png")
    grad3.y = posF + 2 * grad1.height

    grad4 = GameImage("imagens/fundo/gradiente1.png")
    grad4.y = posF + 3 * grad1.height

    nuvem1 = GameImage("imagens/fundo/nuvens.png")
    nuvem1.y = posF

    nuvem2 = GameImage("imagens/fundo/nuvens.png")
    nuvem2.y = nuvem1.height

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
        rolar1(grad1, grad2, grad3, grad4, velocFundo, windows)
        mont.draw()
        rolar2(nuvem1, nuvem2, velocFundo - nuvem, windows)
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

    mont = GameImage("imagens/fundo/fundoMontanha.png")
    mont.x = posF
    mont.y = posF

    grad1 = GameImage("imagens/fundo/gradiente1.png")
    grad1.x = posF
    grad1.y = posF

    grad2 = GameImage("imagens/fundo/gradiente3.png")
    grad2.x = posF
    grad2.y = posF + grad1.height

    grad3 = GameImage("imagens/fundo/gradiente4.png")
    grad3.x = posF
    grad3.y = posF + 2 * grad1.height

    grad4 = GameImage("imagens/fundo/gradiente2.png")
    grad4.x = posF
    grad4.y = posF + 3 * grad1.height

    nuvem = GameImage("imagens/fundo/nuvens.png")
    nuvem.x = posF
    nuvem.y = posF

    voltar = GameObject()
    voltar = Sprite("imagens/voltar2.png", frames=2)
    voltar.set_position((windows.width/2)-(voltar.width/2), (windows.height - voltar.height)-borda)

    while(1):
        grad2.draw()
        mont.draw()
        nuvem.draw()
        Texto(texto, windows)
        voltar.draw()
        if Clique(voltar) == 0:
            sleep(n)
            return 1


        windows.update()

def Jogo(windows):
    windows.set_background_color(laranja)

    mont = GameImage("imagens/fundo/fundoMontanha.png")
    mont.x = posF
    mont.y = posF

    grad1 = GameImage("imagens/fundo/gradiente1.png")
    grad1.x = posF
    grad1.y = posF

    grad2 = GameImage("imagens/fundo/gradiente3.png")
    grad2.x = posF
    grad2.y = posF + grad1.height

    grad3 = GameImage("imagens/fundo/gradiente4.png")
    grad3.x = posF
    grad3.y = posF + 2 * grad1.height

    grad4 = GameImage("imagens/fundo/gradiente2.png")
    grad4.x = posF
    grad4.y = posF + 3 * grad1.height

    nuvem = GameImage("imagens/fundo/nuvens.png")
    nuvem.x = posF
    nuvem.y = posF

    while(1):
        if tecla.key_pressed("esc"):
            return 1
        grad2.draw()
        mont.draw()
        nuvem.draw()
        windows.update()
