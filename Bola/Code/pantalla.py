import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moviendo un círculo")

# Definir las coordenadas y la velocidad del círculo
circle_radius = 20
circle_x = SCREEN_WIDTH // 2
circle_y = SCREEN_HEIGHT // 2
move_speed = 1

# Cargar la imagen de fondo
background_image = pygame.image.load("../imagenes/fondo.png")
background_rect = background_image.get_rect()  

# Bucle principal
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Manejo de teclas para mover el círculo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= move_speed
    if keys[pygame.K_RIGHT]:
        circle_x += move_speed
    if keys[pygame.K_UP]:
        circle_y -= move_speed
    if keys[pygame.K_DOWN]:
        circle_y += move_speed

    # Mover el círculo a través de los bordes de la pantalla
    circle_x = circle_x % SCREEN_WIDTH
    circle_y = circle_y % SCREEN_HEIGHT

    # Dibujar la imagen de fondo
    screen.blit(background_image, background_rect)

    # Dibujar el círculo en su nueva posición
    pygame.draw.circle(screen, WHITE, (circle_x, circle_y), circle_radius)

    # Actualizar la pantalla
    pygame.display.flip()
