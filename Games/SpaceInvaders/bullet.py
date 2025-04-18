import pygame
import os
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Dynamically construct the path to the bullet image
        base_path = os.path.dirname(__file__)  # Get the directory of the current file
        image_path = os.path.join(base_path, "images", "bullet.png")

        # Load the bullet image and get its rect
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (20, 40))
        self.rect = self.image.get_rect()

        # Start each new bullet at the top center of the ship
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def blitme(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)