import pygame
import random

pygame.init()

width = 600
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змійка")

snake_x = 300
snake_y = 200
snake_size = 20
snake_speed = 20
dx = 0
dy = 0

food_x = random.randrange(0, width - snake_size, snake_size)
food_y = random.randrange(0, height - snake_size, snake_size)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -snake_speed
                dy = 0
            if event.key == pygame.K_RIGHT:
                dx = snake_speed
                dy = 0
            if event.key == pygame.K_UP:
                dy = -snake_speed
                dx = 0
            if event.key == pygame.K_DOWN:
                dy = snake_speed
                dx = 0

    snake_x += dx
    snake_y += dy

    # обмеження екрану
    if snake_x < 0:
        snake_x = 0
    if snake_x > width - snake_size:
        snake_x = width - snake_size
    if snake_y < 0:
        snake_y = 0
    if snake_y > height - snake_size:
        snake_y = height - snake_size

    # перевірка їжі
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(0, width - snake_size, snake_size)
        food_y = random.randrange(0, height - snake_size, snake_size)

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (snake_x, snake_y, snake_size, snake_size))
    pygame.draw.rect(window, (0, 255, 0), (food_x, food_y, snake_size, snake_size))

    pygame.display.update()
    clock.tick(10)  # FPS (кадри на секунду)

pygame.quit()
