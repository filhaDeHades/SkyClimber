from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.keyboard import *
from PPlay.animation import *
from PPlay.sound import *
from time import sleep
import random
import RockTomb

random.seed()
preda_speed = 0
preda_direction = 1
MAXSIZE = 5

# Numero de linhas da matriz
matrix_x = 3

# Numero de coluna da matriz
matrix_y = 4





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

bola = janela.width/2
quad = ((janela.height/3)*2)+50
posIni1 = janela.width/2
posIni2 = ((janela.height/3)*2)+50


texto = ["Créditos:", "Música:", "...", "...", "...", "Bibliotecas:", "PPlay", "Pygame"]

def somClique(botao, arquivo):
    if botao.is_button_pressed(1):
        som = Sound(arquivo)
        som.play()

def rolar1(bg1, bg2, bg3, bg4, fv, windows):
    bg1.y -= fv * (windows.delta_time()+0.5)
    bg2.y -= fv * (windows.delta_time()+0.5)
    bg3.y -= fv * (windows.delta_time()+0.5)
    bg4.y -= fv * (windows.delta_time()+0.5)

    if bg4.y <= 0:
        bg1.y = bg4.y + bg4.height
        bg2.y = bg1.y + bg1.height
        bg3.y = bg2.y + bg2.height
        #bg2.y = 2 * bg1.height
        #bg3.y = 3 * bg1.height
        if (bg4.y + bg4.height) <= 0:
            bg4.y = bg3.y + bg3.height

    bg4.draw()
    bg3.draw()
    bg2.draw()
    bg1.draw()

def rolar2(bg1, bg2, fv, windows):
    bg1.y -= fv * (windows.delta_time() + 0.5)
    bg2.y -= fv * (windows.delta_time() + 0.5)

    if bg2.y >= posF:
        bg1.y = posF
        bg2.y = posF - bg1.height

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
    titulo = Sprite("imagens/menu/titulo1.png")
    titulo.set_position(windows.width - titulo.width, borda)

    play = GameObject()
    play = Sprite("imagens/menu/play2.png", frames=2)
    play.set_position(bola-(play.width/2), (windows.height/2)-(play.height/2))

    creditos = GameObject()
    creditos = Sprite("imagens/menu/creditos2.png", frames=2)
    creditos.set_position((bola)-(creditos.width/2), (windows.height - creditos.height)-borda)

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

    voltar = GameObject()
    voltar = Sprite("imagens/menu/voltar2.png", frames=2)
    voltar.set_position((bola)-(voltar.width/2), (windows.height - voltar.height)-borda)

    credito = Sprite("imagens/menu/creditoss.png")

    while(1):
        rolar1(grad1, grad2, grad3, grad4, velocFundo, windows)
        mont.draw()
        rolar2(nuvem1, nuvem2, velocFundo - nuvem, windows)
        credito.draw()
        #Texto(texto, windows)
        voltar.draw()
        if Clique(voltar) == 0:
            sleep(n)
            return 1


        windows.update()

def Jogo(windows):
    grau = -10
    predas = []
    ff = 0
    var1 = var2 = False
    term1 = term2 = False
    desPedra = True
    desSeta = True


    windows.set_background_color(laranja)

    mont = GameImage("imagens/fundo/fundoMontanha.png")
    mont.x = posF
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

    #Oq realmente vai ser o jogador por enquanto
    jogador = GameObject()
    jogador = Sprite("imagens/jogo/bola.png", frames=1)
    jogador.set_position(bola, quad)

    #personagem puramente grafico por enquanto

    jog1 = GameObject()
    jog1 = Sprite("imagens/jogo/psc1.png")
    unha = windows.height - (jog1.height - 40) + 50
    posIni2 = unha
    dedo = bola - jog1.width / 2
    jog1.set_position(dedo, unha)



    seta = Animation("imagens/jogo/seta.png", total_frames=9, loop=True)
    seta.set_position((jogador.x+jogador.width/2) - seta.width/2, (jogador.y -seta.height))
    seta.set_sequence_time(0, 8, 100, loop=True)
    seta.play()

    predas = RockTomb.matriz(janela)


    while(1):
        if tecla.key_pressed("esc"):
            return 1
        if rato.is_button_pressed(1):
            sleep(0.2)
            desSeta = False
            somClique(rato, "som.ogg")

            var1 = True
            var2 = True
            n = seta.get_curr_frame()
            seta.set_initial_frame(n)
            seta.stop()
            if n == 0 or n == 8:
                grau = -35
            elif n == 1 or n == 7:
                grau = -18
            elif n == 2 or n == 6:
                grau = 0
            elif n == 3 or n == 5:
                grau = 18
            elif n == 4:
                n = 35
        if var1 == True:

            if unha > bola+50:
                unha = unha -2
                jogador.set_position(bola, quad-100)
                jog1.set_position(bola - jog1.width / 2, unha)
            else:
                var1 = False
                term1 = True
        if var2 == True:
            for i in range(5):
                for j in range(3):
                    if ff < 150:
                        predas[i][j].set_position(predas[i][j].GO.x, predas[i][j].GO.y+2)
                    else:
                        var2 = False
                        term2 = True
                    ff += 1
        #quando os dois terminam
        if (term1 == True) and (term2 == True):
            if unha < posIni2:
                unha += +2
                #jogador.set_position(bola, quad-100)
                jog1.set_position(bola-(jog1.width/2), unha)

            else:
                term1 = term2 = False
                desSeta = True
                var1 = var2 = False
                desPedra = True
                unha = 300
                ff = 0
                predas = RockTomb.atualizaMatVert(predas, windows)

            for i in range(5):
                for j in range(3):
                    if predas[0][0].GO.y < 10:
                        predas[i][j].set_position(predas[i][j].GO.x, predas[i][j].GO.y+2)
                    else:
                        desPedra = False



        janela.set_background_color(laranja)
        rolar1(grad1, grad2, grad3, grad4, velocFundo, windows)
        mont.draw()
        if tecla.key_pressed("up"):
            rolar2(nuvem1, nuvem2, velocFundo - nuvem, windows)
        nuvem1.draw()
        nuvem2.draw()

        for x in range (5):
            for y in range (3):
                predas[x][y].draw()

        #jogador.draw()
        jog1.draw()
        seta.update()
        if desSeta == True:
            seta.play()
            seta.draw()

        #RockTomb.ult_fil(predas)

        windows.update()
