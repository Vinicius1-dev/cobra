# jofo da cobra

import pygame
import random
import sys

pygame.init()

largura  = 600
altura = 400
tamanho_bloco = 20

preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo da cobra')
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont('arial', 25)

def desenha_cobra(cobra):
    for bloco in cobra:
        pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])
def monstra_pontuacao(pontos):
    texto = fonte.render(f'Pontuação: {pontos}', True, branco)
    tela.blit(texto,[10,10])
def mensagem_fim (pontos):
    texto1 = fonte.render(f'Game Over! Pontuação: {pontos}', True, vermelho)
    texto2 = fonte.render('Pressione Espaço para jogar novamente ou Esc para sair', True, branco)
    tela.blit(texto1, [largura // 2 - texto1.get_width() // 2, altura // 2 - 40])
    tela.blit(texto2, [largura // 2 - texto2.get_width() // 2, altura // 2])
def jogo():
    game_over = False
    game_close = False
    x = largura // 2
    y = altura // 2
    x_mudanca = 0
    y_mudanca = 0
    lista_cobra = []
    comprimento_cobra = 1
    def nova_comida():
        return random.randrange(0, largura - tamanho_bloco, tamanho_bloco), random.randrange(0, altura - tamanho_bloco, tamanho_bloco)
    comida_x, comida_y = nova_comida()
    while not game_over:
        while game_close:
            tela.fill(preto)
            mensagem_fim(comprimento_cobra - 1)
            pygame.display.update()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        jogo()
                        return
                    elif evento.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_mudanca == 0:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT and x_mudanca == 0:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_UP and y_mudanca == 0:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN and y_mudanca == 0:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0
        x += x_mudanca
        y += y_mudanca
        if x >= largura or x < 0 or y >= altura or y < 0:
            game_close = True
        tela.fill(preto)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cabeca_cobra = [x, y]
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]
        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                game_close = True
        desenha_cobra(lista_cobra)
        monstra_pontuacao(comprimento_cobra - 1)
        pygame.display.update()
        if x == comida_x and y == comida_y:
            comida_x, comida_y = nova_comida()
            comprimento_cobra += 1
        relogio.tick(15)
    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    jogo()
