def load_image(filepath):
    import pygame
    try:
        image = pygame.image.load(filepath)
        return image
    except pygame.error as e:
        print(f"Unable to load image at {filepath}: {e}")
        return None

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def reset_game_state():
    return {
        'score': 0,
        'player_position': (100, 300),
        'game_over': False
    }