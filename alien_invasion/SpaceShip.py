import pygame
from pygame.sprite import Sprite

class SpaceShipAlien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load the ship image
        self.image = pygame.image.load('aliens_game/space_ship/spiked ship 3. small.blue_.PNG')
        self.rect = self.image.get_rect()

        #start the each ship at the button of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # rect object is working with integers we have to do this
        self.x = float(self.rect.x)

        # a Flag that show the player is stile presing right key
        self.moving_right = False
        self.moving_left = False

    def Update(self):
        # moving the space ship to the right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object
        self.rect.x = self.x

    def center_ship(self):
        #Center the ship on the screens
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        #draw the schip at the current location
        self.screen.blit(self.image, self.rect)
