import pygame, sys

tamaño_pantalla = W, H = 900, 500 

screen = pygame.display.set_mode(tamaño_pantalla)
pygame.display.set_caption("Bola movible")

fondo = pygame.image.load("../imagenes/fondo.png")

#ciclo de pantalla
while True:
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    screen.blit(fondo, (0, 0))

    pygame.display.flip()