import pygame
import math
from scripts.behavior_tree import *

class Zombie:
    def __init__(self, x, y):
        # Cargar sprite y preparar animación
        sprite_sheet = pygame.image.load("assets/images/zombie.png").convert()
        sprite_sheet.set_colorkey((255, 0, 255))  # Fondo fucsia

        self.frames = []
        frame_width = 34
        frame_height = 51

        for i in range(8):  # 8 frames de movimiento
            frame = sprite_sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
            self.frames.append(frame)

        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 10  # Velocidad de animación

        self.rect = pygame.Rect(x, y, frame_width, frame_height)
        self.speed = 1.5
        self.patrol_points = [(x, y), (x + 100, y + 100)]
        self.patrol_index = 0

        self.behavior = Selector([
            Sequence([IsPlayerNear(), AttackPlayer()]),
            Sequence([IsPlayerVisible(), ChasePlayer()]),
            PatrolArea()
        ])

    def update(self, player):
        self.behavior.run(self, player)
        self.animate()

    def animate(self):
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def attack(self, player):
        print("💥 Zombi ataca al jugador")

    def chase(self, player):
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y
        distance = math.hypot(dx, dy)
        if distance != 0:
            self.rect.x += (dx / distance) * self.speed
            self.rect.y += (dy / distance) * self.speed

    def patrol(self):
        target_x, target_y = self.patrol_points[self.patrol_index]
        dx = target_x - self.rect.x
        dy = target_y - self.rect.y
        distance = math.hypot(dx, dy)

        if distance < 5:
            self.patrol_index = (self.patrol_index + 1) % len(self.patrol_points)
        else:
            self.rect.x += (dx / distance) * self.speed
            self.rect.y += (dy / distance) * self.speed

    def draw(self, screen):
        frame = self.frames[self.current_frame]
        screen.blit(frame, self.rect.topleft)

    def attack(self, player):
    self.sound_manager.play("attack")  # si pasas sound_manager al zombie

    from scripts.behavior_tree import Selector, Sequence, Condition, Action

def setup_behavior(zombie, player):
    def can_see_player():
        return zombie.distance_to(player) < 200

    def is_close():
        return zombie.distance_to(player) < 40

    def patrol():
        zombie.patrol()
        return True

    def chase():
        zombie.chase(player)
        return True

    def attack():
        zombie.attack(player)
        return True

    return Selector([
        Sequence([
            Condition(can_see_player),
            Condition(is_close),
            Action(attack)
        ]),
        Sequence([
            Condition(can_see_player),
            Action(chase)
        ]),
        Action(patrol)
    ])


    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
