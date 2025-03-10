import pygame

import config

screen = pygame.display.set_mode((config.SCREEN_SIZE, config.SCREEN_SIZE))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            running = False

    screen.fill('orange')

    pygame.display.flip()

    clock.tick(config.FPS)

pygame.quit()