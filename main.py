import pygame
import config
from random import randrange

screen = pygame.display.set_mode((config.SCREEN_SIZE, config.SCREEN_SIZE))
clock = pygame.time.Clock()

running = True
begin = True
time = None

snake_rect = None
snake_lenght = None
snake_parts = None
snake_direction = None

while running:
    if begin:
        begin = False
        time = 0
        snake_rect = pygame.rect.Rect(randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE), 
                                      randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE), 
                                      config.SNAKE_PART_SIZE, 
                                      config.SNAKE_PART_SIZE)
        snake_lenght = 1
        snake_parts = []
        snake_direction = pygame.Vector2(config.SNAKE_MOVE_LENGHT, 0)
        
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            running = False
        if(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_UP:
                snake_direction = pygame.Vector2(0, -config.SNAKE_MOVE_LENGHT)
            elif event.key == pygame.K_DOWN:
                snake_direction = pygame.Vector2(0, config.SNAKE_MOVE_LENGHT)
            elif event.key == pygame.K_RIGHT:
                snake_direction = pygame.Vector2(config.SNAKE_MOVE_LENGHT, 0)
            elif event.key == pygame.K_LEFT:
                snake_direction = pygame.Vector2(-config.SNAKE_MOVE_LENGHT, 0)
            print(snake_direction)
            
    time_now = pygame.time.get_ticks()

    screen.fill(config.BG_COLOR)
    for i in range(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOR, (i, 0), (i, config.SCREEN_SIZE))
        pygame.draw.line(screen, config.GRID_COLOR, (0, i), (config.SCREEN_SIZE, i))
        
    if ((time_now - time) > config.DELAY):
        time = time_now
        snake_rect.move_ip(snake_direction)    
        snake_parts.append(snake_rect.copy())
        snake_parts = snake_parts[-snake_lenght:]
    
    for part in snake_parts:
        pygame.draw.rect(screen, config.SNAKE_COLOR, snake_rect)

    pygame.display.flip()

    clock.tick(config.FPS)

pygame.quit()