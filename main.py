import pygame
import sys

# Importar clases personalizadas
from scripts.player import Player
from scripts.zombie import Zombie
from scripts.ui import show_menu, show_game_over

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombies Ate My Neighbours")

# Reloj para FPS
clock = pygame.time.Clock()
FPS = 60

# Cargar fondo (puedes reemplazarlo por una imagen en assets)
background_color = (30, 30, 30)

# Crear jugador y enemigos
player = Player(100, 100)
zombies = [Zombie(400, 300), Zombie(600, 200)]

# Estados del juego
menu_active = True
game_over = False

# Música
pygame.mixer.music.load("assets/music/theme.mp3")
pygame.mixer.music.play(-1)

# Loop principal
while True:
    if menu_active:
        menu_active = show_menu(screen)
        continue

    if game_over:
        game_over = show_game_over(screen)
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar lógica
    player.handle_input()
    for zombie in zombies:
        zombie.update(player)

    # Dibujar todo
    screen.fill(background_color)
    player.draw(screen)
    for zombie in zombies:
        zombie.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

    # Verificar condiciones de derrota
    for zombie in zombies:
        if player.rect.colliderect(zombie.rect):
            game_over = True
