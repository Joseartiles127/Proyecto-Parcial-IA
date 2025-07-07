import pygame

def select_character(screen):
    bg = pygame.image.load("assets/images/player_select.jpg").convert()
    font = pygame.font.SysFont("Arial", 30)
    clock = pygame.time.Clock()

    selected = 0  # 0: Zeke, 1: Julie
    running = True

    while running:
        screen.blit(bg, (0, 0))

        # Mostrar opciones con selector
        zeke_color = (255, 255, 0) if selected == 0 else (255, 255, 255)
        julie_color = (255, 255, 0) if selected == 1 else (255, 255, 255)

        zeke_text = font.render("Zeke", True, zeke_color)
        julie_text = font.render("Julie", True, julie_color)

        screen.blit(zeke_text, (100, 400))
        screen.blit(julie_text, (400, 400))

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    selected = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    selected = 1
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    return "zeke" if selected == 0 else "julie"
