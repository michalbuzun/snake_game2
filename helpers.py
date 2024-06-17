from const import WIDTH, HEIGHT


def draw_game_over_screen(
    font,
    font_small,
    screen,
):
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


def draw_game_won_screen(font, font_small, screen, snake):
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


def draw_next_level_screen(font, font_small, screen, snake):
    next_level_message = font_small.render(
        f"Next level: {snake.level}", False, (0, 0, 0)
    )
    next_level_message_rect = next_level_message.get_rect(
        center=(WIDTH / 2, HEIGHT / 2)
    )
    screen.blit(next_level_message, next_level_message_rect)


def draw_game_information(font, font_small, screen, snake):
    game_information = font_small.render(
        f"Level: {snake.level} ({len(snake.previous_positions)}/{snake.level_length})",
        False,
        (0, 0, 0),
    )
    game_information_rect = game_information.get_rect(center=(WIDTH - 150, 0 + 20))
    screen.blit(game_information, game_information_rect)
