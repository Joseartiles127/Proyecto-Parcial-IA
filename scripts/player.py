import pygame

class Player:
    def __init__(self, x, y, character="zeke", controls="wasd"):
        self.x = x
        self.y = y
        self.speed = 3
        self.character = character
        self.controls = controls

        # Cargar sprite según personaje
        if character == "zeke":
            self.image = pygame.image.load("assets/images/zeke.png").convert_alpha()
        else:
            self.image = pygame.image.load("assets/images/julie.png").convert_alpha()

        # Tamaño de frame del sprite (ajústalo si es necesario)
        self.frame_width = 32
        self.frame_height = 48
        self.current_frame = 0
        self.direction = 'down'

        # Crear rectángulo para colisiones y dibujo
        self.rect = pygame.Rect(self.x, self.y, self.frame_width, self.frame_height)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx = dy = 0

        if self.controls == "wasd":
            if keys[pygame.K_w]:
                dy = -self.speed
                self.direction = 'up'
            if keys[pygame.K_s]:
                dy = self.speed
                self.direction = 'down'
            if keys[pygame.K_a]:
                dx = -self.speed
                self.direction = 'left'
            if keys[pygame.K_d]:
                dx = self.speed
                self.direction = 'right'

        elif self.controls == "arrows":
            if keys[pygame.K_UP]:
                dy = -self.speed
                self.direction = 'up'
            if keys[pygame.K_DOWN]:
                dy = self.speed
                self.direction = 'down'
            if keys[pygame.K_LEFT]:
                dx = -self.speed
                self.direction = 'left'
            if keys[pygame.K_RIGHT]:
                dx = self.speed
                self.direction = 'right'

        self.rect.x += dx
        self.rect.y += dy

        # Animación básica por movimiento
        if dx != 0 or dy != 0:
            self.current_frame = (self.current_frame + 1) % 4  # Suponiendo 4 frames por dirección

    def draw(self, screen):
        # Determina la fila según la dirección
        direction_map = {
            'down': 0,
            'left': 1,
            'right': 2,
            'up': 3
        }

        row = direction_map.get(self.direction, 0)
        frame = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
        frame.blit(self.image, (0, 0), (self.current_frame * self.frame_width, row * self.frame_height, self.frame_width, self.frame_height))
        screen.blit(frame, self.rect.topleft)

