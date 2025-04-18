import pygame.font
import os
from pygame.sprite import Group
from SpaceInvaders.ship import Ship
from SpaceInvaders.settings import Settings


class Scoreboard:
    """A class to display the player's score."""

    def __init__(self, ai_game):
        """Initialize score-keeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Dynamically construct the path to the ship image
        base_path = os.path.dirname(__file__)  # Get the directory of the current file
        image_path = os.path.join(base_path, "images", "ship.png")

        # Load and scale the ship image
        self.ship_image = pygame.image.load(image_path)
        self.ship_image = pygame.transform.scale(self.ship_image, (20, 20))

        # Font settings for score display
        self.text_color = (0, 0, 0)   # white
        self.font = pygame.font.SysFont(None, 36)

        # Prepare the initial score display
        self.prep_score()

        # Prepare level display
        self.prep_level()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = f"Score: {self.stats.score}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.background_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)  # draw current score
        self.screen.blit(self.level_image, self.level_rect)
        self.show_health()

    def prep_level(self):
        """Turn the current level the player is on into an image."""
        level_str = f"Level: {str(self.stats.level)}"
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.background_color)

        # Position the level below the current score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right  # aligns level to the right of the score
        self.level_rect.top = self.score_rect.bottom + 10   # 10 pixels below the score
        
    def show_health(self):
        """Draw health points as ship sprites on the screen."""
        for i in range(self.stats.ships_left):
            x_position = 10 + i * (self.ship_image.get_width() + 10)  # 10px margin between each sprite
            self.screen.blit(self.ship_image, (x_position, 10))  # 10px from the top of the screen

    def show_level(self):
        """Draw the level on screen."""
        self.screen.blit(self.level_image, self.level_rect)