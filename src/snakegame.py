import pygame
import random
import time


def display_score(current_score, surface):
    score_font = pygame.font.SysFont("impact", 20)
    score_surface = score_font.render(f'Score: {current_score}', True, 
                                      pygame.Color(255, 255, 255))
    surface.blit(score_surface, (0, 0))

def save_highscore(highscore):
    with open("highscore.txt", 'w') as file:
        file.write(str(highscore))

def load_highscore():
    try:
        with open("highscore.txt", 'r') as file:
            hs = file.read().strip()
            if not hs:
                return 0
            return int(hs)
    except FileNotFoundError:
        return 0
    
def display_highscore(highscore, surface):
    hs_font = pygame.font.SysFont("impact", 20)
    hs_surface = hs_font.render(f'Highscore: {highscore}', True,
                                pygame.Color(255, 255, 255))
    surface.blit(hs_surface, (0, 25))
    
def game_over(current_score, surface):
    highscore = load_highscore()
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render(f'Game Over! \n Your Score is : {current_score}', True, 
                                    pygame.Color(255, 255, 255))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (400, 200)
    surface.blit(game_over_surface, game_over_rect)
    if current_score > highscore:
        save_highscore(current_score)
        hs_surf = font.render("!!!NEW HIGHSCORE!!!", True,
                                pygame.Color(255, 255, 0))
        hs_rect = hs_surf.get_rect()
        hs_rect = (150, 0)
        surface.blit(hs_surf, hs_rect)
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
    highscore = load_highscore()
    black = pygame.Color(0, 0, 0)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    white = pygame.Color(255, 255, 255)
    gold = pygame.Color(255, 200, 0)
    blue = pygame.Color(0, 0, 255)
    screen = pygame.display.set_mode((resolution))
    
    snake_body = [[100,50], [90,50], [80,50], [70,50]]
    snake_pos = [100,50]
    direction = 'RIGHT'
    change_direction = direction
   
    apple_pos = [random.randrange(1, (resolution[0]//cell)) * cell, 
                 random.randrange(1, (resolution[1]//cell)) * cell]
    apple_spawn = True

    golden_apple_pos = None
    golden_apple_spawn = False
    golden_apple_cooldown = 20
    golden_apple_available = 0


    speed_pos = None
    speed_spawn = False
    speed_slow = 0
    speed_cooldown = 5
    speed_available = 0


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
        # Handles error, snake can't move in 2 directions at once
        if change_direction == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_direction == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_direction == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_direction == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= cell
        if direction == 'DOWN':
            snake_pos[1] += cell
        if direction == 'LEFT':
            snake_pos[0] -= cell
        if direction == 'RIGHT':
            snake_pos[0] += cell

            
        snake_body.insert(0, list(snake_pos))
        #Snake eats apple
        if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
            score += 10
            apple_spawn = False
        else:
            snake_body.pop()
        if not apple_spawn:
            apple_pos = [random.randrange(1, (resolution[0]//cell)) * cell, 
                        random.randrange(1, (resolution[1]//cell)) * cell]
            apple_spawn = True
        #Snake eats golden apple
        if golden_apple_spawn and (snake_pos[0] == golden_apple_pos[0] and 
                                   snake_pos[1] == golden_apple_pos[1]):
            score += 30
            if len(snake_body) > 1:
                snake_body.pop()
            golden_apple_spawn = False
            golden_apple_available = time.time() + golden_apple_cooldown
        if not golden_apple_spawn and time.time() >= golden_apple_available:
            golden_apple_pos = [random.randrange(1, (resolution[0]//cell)) * cell, 
                        random.randrange(1, (resolution[1]//cell)) * cell]
            golden_apple_spawn = True
        #Snake eats speed pickup
        if speed_spawn and (snake_pos[0] == speed_pos[0] and snake_pos[1] == speed_pos[1]):
            if speed_slow < score:
                speed_slow += 50
            speed_spawn = False
            speed_pos = None
            speed_available = time.time() + speed_cooldown
        if not speed_spawn and time.time() >= speed_available:
            speed_pos = [random.randrange(1, (resolution[0]//cell)) * cell, 
                        random.randrange(1, (resolution[1]//cell)) * cell]
            speed_spawn = True
        
        #Draw everything
        screen.fill(black)
        for segment in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(
                segment[0], segment[1], cell, cell))
        
        pygame.draw.rect(screen, red, pygame.Rect(
            apple_pos[0], apple_pos[1], cell, cell))
        
        if golden_apple_spawn and golden_apple_pos:
            pygame.draw.rect(screen, gold, pygame.Rect(
                golden_apple_pos[0], golden_apple_pos[1], cell, cell))
        
        if speed_spawn and speed_pos:
            pygame.draw.rect(screen, blue, pygame.Rect(
                speed_pos[0], speed_pos[1], cell, cell))
        
        #Collision, game over conditions
        if snake_pos[0] < 0 or snake_pos[0] > resolution[0] - cell:
            game_over(score, screen)
        if snake_pos[1] < 0 or snake_pos[1] > resolution[1] - cell:
            game_over(score, screen)
        for segment in snake_body[1:]:
            if snake_pos[0] == segment[0] and snake_pos[1] == segment[1]:
                game_over(score, screen)

        display_score(score, screen)
        display_highscore(highscore, screen)
        pygame.display.flip()
        clock.tick(game_speed + ((score - speed_slow)//50))
    # 3. Quit
    pygame.quit()

if __name__ == "__main__":
    main()
