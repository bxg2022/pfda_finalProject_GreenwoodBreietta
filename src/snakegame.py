import pygame
import random
import time


def display_score(current_score, surface):
    score_font = pygame.font.SysFont("impact", 20)
    score_surface = score_font.render(f'Score : {current_score}', True, 
                                      pygame.Color(255, 255, 255))
    surface.blit(score_surface, (0, 0))
    
def game_over(current_score, surface):
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render(f'Game Over! \n Your Score is : {current_score}', True, 
                                    pygame.Color(255, 255, 255))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (400, 200)
    surface.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

def main():
    # 1. Initialize
    pygame.init()
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    resolution = (800, 600)
    game_speed = 15
    cell = 10
    score = 0
    black = pygame.Color(0, 0, 0)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    white = pygame.Color(255, 255, 255)
    gold = pygame.Color(255, 200, 0)
    screen = pygame.display.set_mode((resolution))
    
    snake_body = [[100,50], [90,50], [80,50], [70,50]]
    snake_pos = [100,50]
    direction = 'RIGHT'
    change_direction = direction
   
    apple_pos = [random.randrange(1, (resolution[0]//cell)) * cell, 
                 random.randrange(1, (resolution[1]//cell)) * cell]
    apple_spawn = True

    golden_apple_pos = [random.randrange(1, (resolution[0]//cell)) * cell, 
                        random.randrange(1, (resolution[1]//cell)) * cell]
    golden_apple_spawn = False
    spawn_delay_event = pygame.USEREVENT + 1
    gold_interval = 5000
    pygame.time.set_timer(spawn_delay_event, gold_interval)



    # 2. Game Loop
    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == spawn_delay_event:
                golden_apple_spawn = True
                pygame.time.set_timer(spawn_delay_event, 0)
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
            score += 10
            apple_spawn = False
        else:
            snake_body.pop()
        if not apple_spawn:
            apple_pos = [random.randrange(1, (resolution[0]//cell)) * cell, 
                        random.randrange(1, (resolution[1]//cell)) * cell]
            apple_spawn = True
        
        if snake_pos[0] == golden_apple_pos[0] and snake_pos[1] == golden_apple_pos[1]:
            score += 30
            if len(snake_body) > 1:
                snake_body.pop()
            golden_apple_spawn = False
        else:
            snake_body.pop
        if not golden_apple_spawn:
            golden_apple_pos = [random.randrange(1, (resolution[0]//cell)) * cell, 
                        random.randrange(1, (resolution[1]//cell)) * cell]
            pygame.time.set_timer(spawn_delay_event, 5000)
            golden_apple_spawn = True
        
        screen.fill(black)
        for segment in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(
                segment[0], segment[1], cell, cell))
        
        pygame.draw.rect(screen, red, pygame.Rect(
            apple_pos[0], apple_pos[1], cell, cell))
        
        pygame.draw.rect(screen, gold, pygame.Rect(
            golden_apple_pos[0], golden_apple_pos[1], cell, cell))
        
        if snake_pos[0] < 0 or snake_pos[0] > resolution[0] - cell:
            game_over(score, screen)
        if snake_pos[1] < 0 or snake_pos[1] > resolution[1] - cell:
            game_over(score, screen)
        for segment in snake_body[1:]:
            if snake_pos[0] == segment[0] and snake_pos[1] == segment[1]:
                game_over(score, screen)

        display_score(score, screen)
        pygame.display.flip()
        clock.tick(game_speed)
    # 3. Quit
    pygame.quit()

if __name__ == "__main__":
    main()
