import pygame
from sys import exit
from const import WIDTH, HEIGHT
from snake import Snake
from obstacle import Obstacle
from helpers import (
    draw_game_over_screen,
    draw_game_won_screen,
    draw_next_level_screen,
    draw_game_information,
)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()
game_active = True

font = pygame.font.SysFont("ubuntu", 30)
font_small = pygame.font.SysFont("ubuntu", 20)

snake = Snake(screen)
snake_group = pygame.sprite.GroupSingle()
snake_group.add(snake)

obstacle = Obstacle(screen, snake)
obstacle_group = pygame.sprite.Group()
obstacle_group.add(obstacle)

next_level_screen_display_start = None

while True:
    screen.fill((145, 129, 162))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            ...

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if snake.game_won:
                        snake.restart_full_game()
                    else:
                        snake.restart_level()

                    game_active = True

    if game_active:
        if snake.next_level_state:
            if not next_level_screen_display_start:
                next_level_screen_display_start = pygame.time.get_ticks()
            draw_next_level_screen(
                font=font,
                font_small=font_small,
                screen=screen,
                snake=snake,
            )

            if (
                next_level_screen_display_start
                and pygame.time.get_ticks() - next_level_screen_display_start >= 1000
            ):
                next_level_screen_display_start = None
                snake.next_level_state = False

        else:
            snake_group.draw(screen)
            snake_group.update()

            obstacle_group.draw(screen)
            obstacle_group.update()

            draw_game_information(
                font=font,
                font_small=font_small,
                screen=screen,
                snake=snake,
            )

            colided_sprite = pygame.sprite.groupcollide(
                snake_group, obstacle_group, False, True
            )

            for piece_mob, static_mob in colided_sprite.items():
                snake.extend_snake(static_mob[0].rect.bottomleft)

                obstacle = Obstacle(screen, snake)
                obstacle_group.add(obstacle)

            game_active = snake.is_game_active()

    else:
        if snake.game_won:
            draw_game_won_screen(
                font=font,
                font_small=font_small,
                screen=screen,
                snake=snake,
            )

        else:
            draw_game_over_screen(
                font=font,
                font_small=font_small,
                screen=screen,
            )

    if next_level_screen_display_start:
        time_since_next_level_screen_dispalys = (
            pygame.time.get_ticks() - next_level_screen_display_start
        )

    pygame.display.update()
    clock.tick(60)
