import pygame

class Button:
    def __init__(self, ai_game, msg, y_offset=0):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 600, 70  # Fixed button dimensions
        self.button_color = (0, 0, 139, 150)  # Soft transparent dark blue (RGBA)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.screen_rect.centerx, self.screen_rect.centery + y_offset)

        # The button message needs to be prepped only once.
        self.msg = msg
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button with rounded corners and the message."""
        # Create a surface for the button with transparency
        button_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, self.button_color, button_surface.get_rect(), border_radius=15)

        # Blit the button surface onto the main screen
        self.screen.blit(button_surface, self.rect.topleft)

        # Draw the message on top of the button
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
    def check_click(self, mouse_pos, mouse_button):
        """Check if the button is clicked."""
        return self.rect.collidepoint(mouse_pos) and mouse_button == 1