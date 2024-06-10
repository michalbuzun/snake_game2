import pygame
from sys import exit
from snake import Snake
from obstacle import Obstacle

WIDTH = 800
HEIGHT = 400

# starts pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()
game_active = True


snake = Snake(screen)
snake_group = pygame.sprite.GroupSingle()
snake_group.add(snake)

obstacle = Obstacle(screen)
obstacle_group = pygame.sprite.Group()
obstacle_group.add(obstacle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True

    if game_active:
        screen.fill((145, 129, 162))
        snake_group.draw(screen)
        snake_group.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        colided_sprite = pygame.sprite.groupcollide(
            snake_group, obstacle_group, False, True
        )

        for piece_mob, static_mob in colided_sprite.items():
            snake.extend_snake(static_mob[0].rect.bottomleft)

            obstacle = Obstacle(screen)
            obstacle_group.add(obstacle)

        game_active = snake.is_alive()

    else:
        ...

    # update everything
    pygame.display.update()
    clock.tick(60)
