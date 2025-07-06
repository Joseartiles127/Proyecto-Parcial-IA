import pygame

class Player:
    def __init__(self, x, y, character="zeke", controls="wasd"):
        self.x = x
        self.y = y
        self.speed = 4
        self.character = character
        self.controls = controls

        # Cargar sprite según personaje
        if character == "zeke":
            self.image = pygame.image.load("assets/images/zeke.png").convert_alpha()
        else:
            self.image = pygame.image.load("assets/images/julie.png").convert_alpha()

        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def handle_input(self):
        keys = pygame.key.get_pressed()

        dx = dy = 0
        if self.controls == "wasd":
            if keys[pygame.K_w]: dy -= self.speed
            if keys[pygame.K_s]: dy += self.speed
            if keys[pygame.K_a]: dx -= self.speed
            if keys[pygame.K_d]: dx += self.speed
        elif self.controls == "arrows":
            if keys[pygame.K_UP]: dy -= self.speed
            if keys[pygame.K_DOWN]: dy += self.speed
            if keys[pygame.K_LEFT]: dx -= self.speed
            if keys[pygame.K_RIGHT]: dx += self.speed

        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
