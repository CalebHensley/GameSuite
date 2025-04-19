import pygame
import math

class Player:
    def __init__(self, x=60, y=675):  
        self.x = x
        self.y = y
        self.width = 60
        self.height = 60
        self.score = 0
        self.is_jumping = False
        self.jump_height = 18  # Adjust jump height as needed
        self.gravity = 1
        self.jump_velocity = 0
        self.ground_y = y  # Store the ground level (initial y position)
        self.rotation_angle = 0  # Track the current rotation angle

        # Load the player image
        self.original_image = pygame.image.load("Games/BowlDozer/src/assets/grey.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (self.width, self.height))
        self.image = self.original_image  # Start with the original image
        self.rect = self.image.get_rect(center=(self.x, self.y))  # Create a rect for collision detection

    def move(self, dx):
        self.x += dx
        self.rect.x = self.x  # Update the rect position

    def jump(self):
        if not self.is_jumping:  # Only allow jumping if the player is on the ground
            self.is_jumping = True
            self.jump_velocity = self.jump_height

    def update(self):
        if self.is_jumping:
            self.y -= self.jump_velocity  # Move the player upward
            self.jump_velocity -= self.gravity  # Apply gravity

            # Ensure the player doesn't go below the ground level
            if self.y >= self.ground_y:
                self.y = self.ground_y  # Reset to ground level
                self.is_jumping = False  # Stop jumping
        
        self.rect.center = (self.x, self.y)

        # Rotate the player image around its center
        self.rotation_angle = (self.rotation_angle - 6) % 360  # Increment the angle and keep it within 0-359
        rotated_image = pygame.transform.rotate(self.original_image, self.rotation_angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)  # Keep the center consistent
        self.image = rotated_image
        self.rect = rotated_rect

    def hit_collectible(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def draw(self, screen):
        # Draw the rotated player image
        screen.blit(self.image, self.rect.topleft)