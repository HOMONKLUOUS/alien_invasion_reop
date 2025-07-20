import pygame
from pygame.sprite import Sprite

class Aliens(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.image = pygame.image.load('aliens_game/space_ship/skull_in_a_ufo_spacecraft.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        # return True if aiens is at the edge of the screen
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        self.x += self.setting.alien_speed * self.setting.fleet_direction
        self.rect.x = self.x