import pygame

class Obstacle:
    def __init__(self, position, image_path="Games/BowlDozer/src/assets/wall.png", size=(100, 100)):
        # Load and resize the obstacle image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=position)  # Create a rect for collision detection

    def move(self, speed):
        # Move the obstacle leftwards
        self.rect.x -= speed

    def check_collision(self, player_rect):
        # Check if the player collides with the obstacle
        return self.rect.colliderect(player_rect)

    def is_collected(self, player):
        # Check if the player has "collected" the obstacle (e.g., overlaps with it)
        return self.rect.colliderect(player.rect)

    def draw(self, screen):
        # Draw the obstacle on the screen
        screen.blit(self.image, self.rect.topleft)