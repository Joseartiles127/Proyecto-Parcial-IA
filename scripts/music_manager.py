self.tracks = {
    "main": "assets/music/main_theme.ogg",
    "intro": "assets/music/konami_intro.flac",
    "zombie_panic": "assets/music/zombie_panic.ogg",
    "game_over": "assets/music/game_over.ogg",
    "victory": "assets/music/victory.ogg",
    "finish_level": "assets/music/finish_level.ogg"
}

music.stop()
music.play("finish_level", loop=False)

def show_level_complete(screen):
    font = pygame.font.SysFont("Arial", 40)
    text = font.render("¡Nivel Completado!", True, (255, 255, 0))
    screen.fill((0, 0, 0))
    screen.blit(text, (150, 200))
    pygame.display.flip()
    pygame.time.wait(3000)

if all(n.rescued for n in neighbors):
    music.stop()
    music.play("finish_level", loop=False)
    show_level_complete(screen)
    # Luego: cargar siguiente nivel o volver al menú
