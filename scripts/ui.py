import pygame
import sys

def draw_text(screen, text, size, x, y, color=(255, 255, 255)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, rect)

def show_menu(screen):
    clock = pygame.time.Clock()
    while True:
        screen.fill((10, 10, 30))
        draw_text(screen, "ZOMBIES ATE MY NEIGHBOURS", 50, screen.get_width() // 2, 150)
        draw_text(screen, "Presiona ENTER para empezar", 30, screen.get_width() // 2, 300)
        draw_text(screen, "Jugador 1: WASD | Jugador 2: Flechas", 24, screen.get_width() // 2, 400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return False  # Sal del menú y comienza el juego

        pygame.display.flip()
        clock.tick(60)

def show_game_over(screen):
    clock = pygame.time.Clock()
    while True:
        screen.fill((50, 0, 0))
        draw_text(screen, "GAME OVER", 60, screen.get_width() // 2, 200)
        draw_text(screen, "Presiona R para reiniciar o ESC para salir", 30, screen.get_width() // 2, 320)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return False  # Reinicia el juego
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)

konami_logo = pygame.image.load("assets/images/screenshot_00.png").convert()

def show_intro(screen):
    clock = pygame.time.Clock()
    logo = pygame.image.load("assets/images/screenshot_00.png").convert()
    screen.blit(logo, (0, 0))
    pygame.display.flip()
    pygame.time.delay(2000)  # Mostrar 2 segundos

# En tu main.py antes de entrar al menú:
show_intro(screen)

import pygame

def show_intro(screen):
    clock = pygame.time.Clock()
    logo = pygame.image.load("assets/images/screenshot_00.png").convert()
    
    # Reproducir música de intro (una vez)
    pygame.mixer.music.load("assets/music/konami_intro.flac")
    pygame.mixer.music.play()

    screen.blit(logo, (0, 0))
    pygame.display.flip()
    
    # Esperar que la música termine o 5 segundos
    pygame.time.wait(5000)
