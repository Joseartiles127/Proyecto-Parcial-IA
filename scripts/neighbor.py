import pygame

class Neighbor:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/barbecue_cook.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rescued = False

    def update(self, player):
        if self.rect.colliderect(player.rect):
            self.rescued = True
            return True  # Indica que fue rescatado
        return False

    def draw(self, screen):
        if not self.rescued:
            screen.blit(self.image, self.rect.topleft)
