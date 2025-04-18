import pygame
import sys

class MainMenu:
    def __init__(self, screen):
        """Initialize the main menu."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.Font(None, 42)  # Font for the menu title
        self.options = ["Space Invaders", "Atomic Cookie", "Coming Soon", "Coming Soon", "Coming Soon", "Coming Soon"]  # Add more games here
        self.option_rects = []  # Store the rects for each option
        self.placeholder_images = []  # Store placeholder images for buttons

        # Load the menu wallpaper
        self.menu_wallpaper = pygame.image.load("images/menuwallpaper.jpg")
        self.menu_wallpaper = pygame.transform.scale(self.menu_wallpaper, (self.screen_rect.width, self.screen_rect.height))

        # Load placeholder images
        for index, option in enumerate(self.options):
            if option == "Space Invaders":
                # Load and scale the background image for the Space Invaders button
                background_image = pygame.image.load("SpaceInvaders/images/background.jpg")
                background_image = pygame.transform.scale(background_image, (250, 250))  # Scale to button size
                self.placeholder_images.append(background_image)
            elif option == "Atomic Cookie":
                # Create a surface with the background color
                button_surface = pygame.Surface((250, 250))
                button_surface.fill((254, 208, 136))  # Fill with #FED088

                # Load and scale the cookie image
                cookie_image = pygame.image.load("AtomicCookie/images/cookie.png")
                cookie_image = pygame.transform.scale(cookie_image, (200, 200))  # Scale the image slightly smaller

                # Blit the cookie image onto the button surface
                cookie_rect = cookie_image.get_rect(center=button_surface.get_rect().center)
                button_surface.blit(cookie_image, cookie_rect)

                self.placeholder_images.append(button_surface)
            else:
                # Use a blue placeholder image for other buttons
                placeholder_image = pygame.Surface((250, 250))  # Placeholder image size
                placeholder_image.fill((100, 100, 255))  # Fill with a blue color
                self.placeholder_images.append(placeholder_image)

    def display_menu(self):
        """Display the main menu."""
        # Blit the menu wallpaper as the background
        self.screen.blit(self.menu_wallpaper, (0, 0))

        # Display the title with a black outline
        title_text = self.font.render("Caleb's Coding Collection", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.screen_rect.centerx, 50))
        outline_color = (0, 0, 0)  # Black outline color
        offsets = [(-2, -2), (-2, 2), (2, -2), (2, 2)]  # Offsets for the outline

        for offset in offsets:
            outline_text = self.font.render("Caleb's Coding Collection", True, outline_color)
            outline_rect = outline_text.get_rect(center=(title_rect.centerx + offset[0], title_rect.centery + offset[1]))
            self.screen.blit(outline_text, outline_rect)

        # Render the main title text in white
        self.screen.blit(title_text, title_rect)

        # Display the game options in a 3x2 grid
        self.option_rects = []  # Clear the rects list before rendering
        grid_rows, grid_cols = 2, 3  # Define the grid dimensions
        button_width, button_height = 250, 250  # Button dimensions
        padding_x, padding_y = 25, 25  # Padding between buttons
        start_x = (self.screen_rect.width - (grid_cols * button_width + (grid_cols - 1) * padding_x)) // 2
        start_y = 150

        for index, option in enumerate(self.options):
            row = index // grid_cols
            col = index % grid_cols
            button_x = start_x + col * (button_width + padding_x)
            button_y = start_y + row * (button_height + padding_y)

            # Draw the placeholder image
            self.screen.blit(self.placeholder_images[index], (button_x, button_y))

            # Create a rect for the button
            option_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            self.option_rects.append(option_rect)

            # Render the option text with a black outline
            option_text = self.font.render(option, True, (255, 255, 255))
            outline_color = (0, 0, 0)  # Black outline color
            offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Offsets for the outline

            for offset in offsets:
                outline_text = self.font.render(option, True, outline_color)
                outline_rect = outline_text.get_rect(center=(option_rect.centerx + offset[0], option_rect.centery + offset[1]))
                self.screen.blit(outline_text, outline_rect)

            # Render the main text in white
            option_text_rect = option_text.get_rect(center=option_rect.center)
            self.screen.blit(option_text, option_text_rect)

        pygame.display.flip()

    def run(self):
        """Run the main menu loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        for index, option_rect in enumerate(self.option_rects):
                            if option_rect.collidepoint(mouse_pos):
                                if index == 0:  # Space Invaders selected
                                    return "space_invaders"
                                elif index == 1:  # Atomic Cookie selected
                                    return "atomic_cookie"
                                else:
                                    print(f"Game {index + 1} selected!")  # Placeholder for other games

            self.display_menu()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))  # Create a window with a fixed size
    pygame.display.set_caption("Main Menu")  # Set the window title

    while True:
        main_menu = MainMenu(screen)  # Create an instance of the MainMenu
        selected_game = main_menu.run()  # Run the main menu

        if selected_game == "space_invaders":
            print("Launching Space Invaders...")
            from SpaceInvaders.game import SpaceInvaders  # Import here to avoid circular import
            game = SpaceInvaders()  # Create an instance of the Space Invaders game
            game.run_game()
        elif selected_game == "atomic_cookie":
            print("Launching Atomic Cookie...")
            from AtomicCookie.game import run_atomic_cookie  # Import the function
            run_atomic_cookie()  # Run the Atomic Cookie game