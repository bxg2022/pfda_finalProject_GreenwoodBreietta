import pygame
import random
import time

def main():
    # 1. Initialize
    pygame.init()
    pygame.display.set_caption('Snake Game')
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    # 2. Game Loop
    running = True
    while running:
        # Game Logic

        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('Black')
        pygame.display.flip()
    # 3. Quit
    pygame.quit()

if __name__ == "__main__":
    main()