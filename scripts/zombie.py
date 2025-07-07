import pygame
import math

class Zombie:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/zombie.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.damage_cooldown = 0  # Para evitar daño continuo cada frame

    def update(self, player):
        # Movimiento simple hacia el jugador
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)

        if distance > 0:
            dx /= distance
            dy /= distance

        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        # Reducir cooldown de daño
        if self.damage_cooldown > 0:
            self.damage_cooldown -= 1

    def check_collision(self, player):
        # Detecta colisión con el jugador
        if self.rect.colliderect(player.rect):
            if self.damage_cooldown == 0:
                print("¡Zombie atacó al jugador!")
                self.damage_cooldown = 60  # 1 segundo a 60 FPS
                return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
