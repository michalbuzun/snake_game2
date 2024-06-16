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

font = pygame.font.SysFont("ubuntu", 30)
font_small = pygame.font.SysFont("ubuntu", 20)

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
            ...

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

        game_information = font_small.render(
            f"Level: {snake.level} ({len(snake.previous_positions)}/{snake.level_length})",
            False,
            (0, 0, 0),
        )
        game_information_rect = game_information.get_rect(center=(WIDTH - 150, 0 + 20))
        screen.blit(game_information, game_information_rect)

        colided_sprite = pygame.sprite.groupcollide(
            snake_group, obstacle_group, False, True
        )

        for piece_mob, static_mob in colided_sprite.items():
            snake.extend_snake(static_mob[0].rect.bottomleft)

            obstacle = Obstacle(screen)
            obstacle_group.add(obstacle)

        game_active = snake.is_game_active()

    else:
        screen.fill((145, 129, 162))

        if snake.game_won:
            game_win_message = font.render("Game win", False, (0, 0, 0))
            game_win_message_rect = game_win_message.get_rect(
                center=(WIDTH / 2, HEIGHT / 2 - 50)
            )
            screen.blit(game_win_message, game_win_message_rect)

            your_score_message = font_small.render(
                f"Your score: {snake.score}", False, (0, 0, 0)
            )
            your_score_message_rect = your_score_message.get_rect(
                center=(WIDTH / 2, HEIGHT / 2 + 20)
            )
            screen.blit(your_score_message, your_score_message_rect)

        else:
            gameover_message = font.render("Game over", False, (0, 0, 0))
            gameover_message_rect = gameover_message.get_rect(
                center=(WIDTH / 2, HEIGHT / 2 - 50)
            )
            screen.blit(gameover_message, gameover_message_rect)

            play_again_message = font_small.render(
                "Press space to start again", False, (0, 0, 0)
            )
            play_again_message_rect = play_again_message.get_rect(
                center=(WIDTH / 2, HEIGHT / 2 + 20)
            )
            screen.blit(play_again_message, play_again_message_rect)

    pygame.display.update()
    clock.tick(60)
