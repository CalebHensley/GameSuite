# This file contains the main game logic, including the game loop, score tracking, and collision detection.

import pygame
import random
from player import Player
from obstacles import Obstacle
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Game class
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Bowl Dozer")
        self.clock = pygame.time.Clock()
        self.player = Player(x=100, y=300)
        self.obstacles = []
        self.score = 0
        self.running = True
        
        # Place the player near the bottom of the screen
        self.player = Player(x=60, y=SCREEN_HEIGHT - 80)

        base_path = os.path.dirname(__file__)  # Get the directory of the current file
        images_path = os.path.join(base_path, "assets")
        
        # Load the background image
        street_image_path = os.path.join(images_path, "street.jpg")
        self.background = pygame.image.load(street_image_path).convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_x1 = 0  # First instance of the background
        self.background_x2 = self.background.get_width()  # Second instance starts right after the first

    def update_background(self):
        # Move both background instances to the left
        self.background_x1 -= 5  # Adjust speed as needed
        self.background_x2 -= 5

        # Reset positions when they move out of the frame
        if self.background_x1 <= -self.background.get_width():
            self.background_x1 = self.background_x2 + self.background.get_width()
        if self.background_x2 <= -self.background.get_width():
            self.background_x2 = self.background_x1 + self.background.get_width()

    def draw_background(self):
        # Draw both instances of the background
        self.screen.blit(self.background, (self.background_x1, 0))
        self.screen.blit(self.background, (self.background_x2, 0))

    def spawn_obstacle(self):
        # Limit the number of obstacles on screen
        if len(self.obstacles) >= 2:
            return

        # Enforce a minimum spawn interval of 2 seconds
        current_time = pygame.time.get_ticks()
        if hasattr(self, "last_spawn_time") and current_time - self.last_spawn_time < 2000:
            return

        # Spawn the obstacle at the right edge of the screen
        position = (SCREEN_WIDTH, SCREEN_HEIGHT - 100)  # Adjust y position as needed
        self.obstacles.append(Obstacle(position=position))

        # Update the last spawn time
        self.last_spawn_time = current_time

    def handle_collisions(self):
        for obstacle in self.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
                self.running = False  # End game on collision

    def update_score(self):
        for obstacle in self.obstacles:
            if obstacle.is_collected(self.player):
                self.score += 1
                self.obstacles.remove(obstacle)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quit event detected.")
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Check if the spacebar is pressed
                        self.player.jump()

            self.player.update()
            self.spawn_obstacle()
            self.handle_collisions()
            self.update_score()

            # Update and draw the background
            self.update_background()
            self.draw_background()

            # Draw the player and obstacles
            for obstacle in self.obstacles:
                obstacle.move(speed=5)  # Move leftwards at the same speed as the background
                obstacle.draw(self.screen)
                
            self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.rect.right > 0]
            
            self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        print("Exiting game loop.")
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()