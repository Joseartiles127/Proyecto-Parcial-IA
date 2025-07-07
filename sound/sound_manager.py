import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {
            "attack": pygame.mixer.Sound("assets/sounds/attack.wav"),
            "shoot": pygame.mixer.Sound("assets/sounds/shoot.wav"),
            "pickup": pygame.mixer.Sound("assets/sounds/pickup.wav"),
            "scream": pygame.mixer.Sound("assets/sounds/scream.wav"),
            "zombie": pygame.mixer.Sound("assets/sounds/zombie_growl.wav"),
            "menu_select": pygame.mixer.Sound("assets/sounds/menu_select.wav"),
            "menu_start": pygame.mixer.Sound("assets/sounds/menu_start.wav"),
            "hurt": pygame.mixer.Sound("assets/sounds/hurt.wav"),
            "game_over": pygame.mixer.Sound("assets/sounds/game_over.wav")
        }

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()
