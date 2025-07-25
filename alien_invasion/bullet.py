import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        self.settings.bullet_height)
        # midtop mach the bullets fire in the front of the ship
        self.rect.midtop = ai_game.SpaceShip.rect.midtop
        # Store the bullet's position as a float.
        self.y = float(self.rect.y)
        
    def update(self):
        """Move the bullet up the screen."""

        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet to the screen."""

        pygame.draw.rect(self.screen, self.color, self.rect)