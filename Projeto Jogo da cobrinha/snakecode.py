# Importação das bibliotecas
import pygame
from pygame.locals import *
from sys import exit
from random import *



# Inicializar as funções na biblioteca pygame
pygame.init() 

# musicas/ som do jogo
pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer.music.load('BoxCat Games - Victory.mp3')
pygame.mixer.music.play(-1)
som_colisão = pygame.mixer.Sound('smw_fireball.wav')
som_colisão.set_volume(1)

# Definição das variáveis

# Tamanho da tela
largura = 640
altura = 480

# Tamanho da cobra
a_cobra = 20
c_cobra = 20

# Posição da cobra na tela
x_cobra = int(largura/ 2 - c_cobra)
y_cobra = int(altura/ 2 - a_cobra)

# Variáveis de controle
x_controle = 20
y_controle = 0

# Tamanho do rato
a_rato = 20
c_rato = 20

# Posição do rato na tela
x_rato = randint(20, 620)
y_rato = randint(20, 460)

# Variáveis extras
velocidade = 5
lista_corpo = list()
comprimento_inicial = 3
frames = 20
fonte = pygame.font.SysFont('arial', 25, True, True)
pontos = 0
gameover = False

# Definição da tela
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()


# FUNÇÕES
# função para a cobrinha crescer
def cresce_cobra(lista_corpo):
    for posicao_xy in lista_corpo:
        pygame.draw.rect(tela, (0, 255, 0), (posicao_xy[0], posicao_xy[1], 20, 20))


# Função que define as ações caso o jogador perca
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_corpo, lista_cabeça, x_rato, y_rato, velocidade, frames, gameover
    pontos = 0
    comprimento_inicial = 3
    x_cobra = int(largura / 2 - c_cobra)  # posição x da cobra
    y_cobra = int(altura / 2 - a_cobra)  # posição y da cobra
    lista_corpo = list()
    lista_cabeça = list()
    x_rato = randint(20, 620)
    y_rato = randint(20, 460)
    velocidade = 5
    frames = 20
    gameover = False


# Nome do jogo
pygame.display.set_caption('Jogo da Cobrinha')

# Programação principal do Jogo da Cobrinha
while True:
    # Fluidez do jogo
    relogio.tick(frames)

    # Preenchimento da tela com a cor preta
    tela.fill((0, 0, 0))

    #Formatação do texto Pontos na tela
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (255, 255, 255))

    # Detecção se alguma ação do jogador ocorreu
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Controle da cobrinha
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = - velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == - velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
    x_cobra += x_controle
    y_cobra += y_controle

    # Criação do design da cobrinha
    cobra = pygame.draw.rect(tela, (255, 0, 0), (x_cobra, y_cobra, c_cobra, a_cobra))

    # Criação do design do rato
    rato = pygame.draw.rect(tela, (255, 255, 0), (x_rato, y_rato, c_rato, a_rato))

    # Condição de colisão entre cobra e rato
    if cobra.colliderect(rato):
        x_rato = randint(40, 600)
        y_rato = randint(40, 440)
        pontos += 1
        som_colisão.play()
        comprimento_inicial += 1
        if velocidade < 20:
            velocidade += 0.25
            frames += 0.25

    # Definindo o corpo da cobra
    lista_cabeça = list()
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    lista_corpo.append(lista_cabeça)

# Condição de colisão da cobra com ela mesma (Game Over)
    if lista_corpo.count(lista_cabeça) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem1 = f'GAME OVER!'
        mensagem2 = f'Sua pontuação foi: {pontos}'
        mensagem3 = f'Pressione ESPAÇO para recomeçar!'
        texto1 = fonte2.render(mensagem1, True, (255, 255, 255))
        texto2 = fonte2.render(mensagem2, True, (255, 255, 255))
        texto3 = fonte2.render(mensagem3, True, (255, 255, 255))
        gameover = True
        while gameover:
            tela.fill((255, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        reiniciar_jogo()
            tela.blit(texto1, (230, 200))
            tela.blit(texto2, (190, 240))
            tela.blit(texto3, (130, 280))
            pygame.display.update()

    # Crescimento da cobra
    if len(lista_corpo) > comprimento_inicial:
        del lista_corpo[0]
    cresce_cobra(lista_corpo)

    #Impressão dos Pontos na tela
    tela.blit(texto, (250, 10))

    # Código que permite a cobra atravessar a tela
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura

    # Atualização da tela do jogo
    pygame.display.update()
