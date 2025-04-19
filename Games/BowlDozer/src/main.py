import pygame
import sys
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Endless Runner Game")
    
    game = Game(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        game.update()
        game.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()