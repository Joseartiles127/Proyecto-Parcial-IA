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
    # Cargar recursos
    konami_logo = pygame.image.load("assets/images/screenshot_00.png").convert()
    press_start = pygame.image.load("assets/images/press_start.png").convert_alpha()
    press_start_rect = press_start.get_rect(center=(screen.get_width() // 2, 350))

    # Música de introducción
    pygame.mixer.music.load("assets/music/konami_intro.flac")
    pygame.mixer.music.play()

    # Mostrar logo primero
    screen.blit(konami_logo, (0, 0))
    pygame.display.flip()
    pygame.time.wait(3000)

    clock = pygame.time.Clock()
    blink = True
    blink_timer = 0

    running = True
    while running:
        screen.blit(konami_logo, (0, 0))

        # Parpadeo del texto
        blink_timer += 1
        if blink_timer >= 30:
            blink = not blink
            blink_timer = 0

        if blink:
            screen.blit(press_start, press_start_rect)

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False
            if event.type == pygame.KEYDOWN or event.type == pygame.JOYBUTTONDOWN:
                pygame.mixer.music.stop()
                return True  # Continuar al juego

