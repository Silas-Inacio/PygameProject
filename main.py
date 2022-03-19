import pygame
from sys import exit

pygame.init()  # apenas inicia o jogo, primeira coisa do pygame
screen = pygame.display.set_mode((800, 400))  # definindo o tamanho da janela
pygame.display.set_caption('Runner')  # nome do jogo na janela
clock = pygame.time.Clock()

while True:  # serve pra que o display não feche e que o jogo fique sempre atualizando
    for event in pygame.event.get():  # pega todos os eventos pra verificar as ações que foram feitas
        if event.type == pygame.QUIT:  # verifica se o tipo de evento foi clicar no "X" no topo da janela
            pygame.quit()  # chama um metodo que fecha o pygame
            exit()  # fecha o codigo inteiramente e evita erros porque o while ainda esta em execução
    # draw all our elements
    # update everything
    pygame.display.update()  # mantem a janela aberta, necessario como o pygame.init()
    clock.tick(60)  # diz ao objeto clock para rodar no maximo 60x por segundo