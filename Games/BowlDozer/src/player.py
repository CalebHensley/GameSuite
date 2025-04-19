import pygame

class Player:
    def __init__(self, x=60, y=650):  # Accept x and y as arguments with default values
        self.x = x
        self.y = y
        self.original_x = x  # Store the original x position
        self.original_y = y  # Store the original y position
        self.width = 60  # Example width
        self.height = 60  # Example height
        self.color = (0, 0, 255)  # Example color (blue)
        self.score = 0
        self.is_jumping = False
        self.jump_height = 16  # Adjust jump height as needed
        self.gravity = 0.7
        self.jump_velocity = 0
        self.ground_y = y  # Store the ground level (initial y position)

        # Load the player image
        self.image = pygame.image.load("Games/BowlDozer/src/assets/grey.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))  # Create a rect for collision detection

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
        else:
            # Ensure the player stays at the original x and y when not jumping
            self.x = self.original_x
            self.y = self.ground_y

        # Update the rect position
        self.rect.topleft = (self.x, self.y)

    def hit_collectible(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def draw(self, screen):
        # Draw the player image
        screen.blit(self.image, (self.x, self.y))