import pygame
import random
import time
      

def main():
    # 1. Initialize
    pygame.init()
    pygame.display.set_caption('Snake Game')
    resolution = (800, 600)
    game_speed = 15
    cell = 10
    score = 0
    black = pygame.Color(0, 0, 0)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    screen = pygame.display.set_mode((resolution))
    fps = pygame.time.Clock()

    snake_body = [[100,50], [90,50], [80,50], [70,50]]
    snake_pos = snake_body[0]


    # 2. Game Loop
    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(black)
        for segment in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(
                segment[0], segment[1], cell, cell))

        pygame.display.flip()
        fps.tick(game_speed)
    # 3. Quit
    pygame.quit()

if __name__ == "__main__":
    main()
