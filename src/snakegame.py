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
    direction = 'RIGHT'
    change_direction = direction

    apple_pos = [random.randrange(1, (resolution[0]//cell)) * cell, 
                 random.randrange(1, (resolution[1]//cell)) * cell]
    apple_spawn = True

    # 2. Game Loop
    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Keyboard inputs for snake movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    change_direction = 'UP'
                if event.key == pygame.K_s:
                    change_direction = 'DOWN'
                if event.key == pygame.K_a:
                    change_direction = 'LEFT'
                if event.key == pygame.K_d:
                    change_direction = 'RIGHT'
        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= cell
        if direction == 'DOWN':
            snake_pos[1] += cell
        if direction == 'LEFT':
            snake_pos[0] -= cell
        if direction == 'RIGHT':
            snake_pos[0] += cell
        # Handles error, snake can't move in 2 directions at once
        if change_direction == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_direction == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_direction == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_direction == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

            
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
            apple_spawn = False
        else:
            snake_body.pop()
        if not apple_spawn:
            apple_pos = [random.randrange(1, (resolution[0]//cell)) * cell, 
                        random.randrange(1, (resolution[1]//cell)) * cell]
            apple_spawn = True
        
        screen.fill(black)
        for segment in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(
                segment[0], segment[1], cell, cell))
        
        pygame.draw.rect(screen, red, pygame.Rect(
            apple_pos[0], apple_pos[1], cell, cell))
        
        if snake_pos[0] < 0 or snake_pos[0] > resolution[0] - cell:
            running = False
        if snake_pos[1] < 0 or snake_pos[1] > resolution[1] - cell:
            running = False

        pygame.display.flip()
        fps.tick(game_speed)
    # 3. Quit
    pygame.quit()

if __name__ == "__main__":
    main()
