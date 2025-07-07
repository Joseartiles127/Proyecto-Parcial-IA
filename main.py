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

player = Player(100, 100, character="zeke", controls="wasd")

player1 = Player(100, 100, character="zeke", controls="wasd")
player2 = Player(200, 100, character="julie", controls="arrows")

player1.handle_input()
player1.draw(screen)

player2.handle_input()
player2.draw(screen)

# Crear lista de zombis
zombies = [
    Zombie(400, 200),
    Zombie(600, 300),
]

# En el bucle principal del juego:
for zombie in zombies:
    zombie.update(player)
    zombie.draw(screen)

    menu_active = True
game_over = False

while True:
    if menu_active:
        menu_active = show_menu(screen)
        continue

    if game_over:
        game_over = show_game_over(screen)
        continue

    if player.lives <= 0 or all_neighbors_dead:
    game_over = True


    if zombie.check_collision(player):
        game_over = True  # O reducir vida del jugador

zombie = Zombie(400, 300)

zombie.update(player)
zombie.draw(screen)

background = pygame.image.load("assets/images/level01.png").convert()

screen.blit(background, (0, 0))

screen = pygame.display.set_mode((512, 448))
