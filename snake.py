import pygame
from enum import Enum, auto


SNAKE_SIZE = 50


LEVEL_SPEEDS = {
    1: 20,
    2: 10,
    3: 9,
    4: 8,
    5: 7,
    6: 6,
    7: 5,
    8: 4,
    9: 3,
    10: 2,
    11: 1,
}

TOP_LEVEL = max(LEVEL_SPEEDS.keys())


LEVEL_LENGTH = 10
START_LEVEL = 1
SNAKE_INITIAL_POSITIONS = [(250, 200), (300, 200), (350, 200), (400, 200)]
SNAKE_INITIAL_POSITIONS_TEST = [
    (100, 200),
    (150, 200),
    (200, 200),
    (250, 200),
    (300, 200),
    (350, 200),
    (400, 200),
]


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


class Snake(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.surface_width = surface.get_width()
        self.surface_height = surface.get_height()
        self.image = pygame.Surface((SNAKE_SIZE, SNAKE_SIZE))
        self.image.fill((195, 226, 162))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (400, 200)
        self.direction = Direction.RIGHT
        self.divider = 0
        self.previous_positions = SNAKE_INITIAL_POSITIONS_TEST[:]
        self.next_move_possible = True
        self.level = START_LEVEL
        self.level_length = LEVEL_LENGTH
        self.game_won = False
        self.score = 0
        self.next_level_state = False

    def _wall_collision(self):
        if self.direction == Direction.RIGHT:
            if self.rect.x + SNAKE_SIZE >= self.surface_width:
                return True

        if self.direction == Direction.LEFT:
            if self.rect.x - SNAKE_SIZE < 0:
                return True

        if self.direction == Direction.UP:
            if self.rect.y - SNAKE_SIZE < 0:
                return True

        if self.direction == Direction.DOWN:
            if self.rect.y + SNAKE_SIZE >= self.surface_height:
                return True

    def _player_input(self):
        if self.next_move_possible:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                if self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                    self.next_move_possible = False

            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                if self.direction != Direction.UP:
                    self.direction = Direction.DOWN
                    self.next_move_possible = False

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                    self.next_move_possible = False

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                    self.next_move_possible = False

    def _player_movement(self):
        self.divider += 1

        if self.divider % LEVEL_SPEEDS[self.level] == 0:
            self.next_move_possible = True
            if self.direction == Direction.RIGHT:
                if self._wall_collision():
                    self.rect.x = 0
                else:
                    self.rect.x += SNAKE_SIZE

            if self.direction == Direction.LEFT:
                if self._wall_collision():
                    self.rect.x = self.surface_width - SNAKE_SIZE
                else:
                    self.rect.x -= SNAKE_SIZE

            if self.direction == Direction.UP:
                if self._wall_collision():
                    self.rect.y = self.surface_height - SNAKE_SIZE
                else:
                    self.rect.y -= SNAKE_SIZE

            if self.direction == Direction.DOWN:
                if self._wall_collision():
                    self.rect.y = 0
                else:
                    self.rect.y += SNAKE_SIZE

            self.previous_positions.append(self.rect.bottomleft)
            self.previous_positions.pop(0)

    def _render_player(self):
        for position in self.previous_positions:
            position_rect = pygame.Rect(
                position[0], position[1], SNAKE_SIZE, SNAKE_SIZE
            )
            position_rect.bottomleft = (position[0], position[1])

            pygame.draw.rect(
                self.surface,
                (146, 162, 129),
                position_rect,
            )

    def extend_snake(self, postion):
        self.previous_positions.append(postion)

    def restart_full_game(self):
        self.rect.bottomleft = (400, 200)
        self.direction = Direction.RIGHT
        self.previous_positions = SNAKE_INITIAL_POSITIONS[:]

        self.level = START_LEVEL
        self.game_won = False
        self.score = 0
        self.next_level_state = False

    def restart_level(self):
        self.rect.bottomleft = (400, 200)
        self.direction = Direction.RIGHT
        self.previous_positions = SNAKE_INITIAL_POSITIONS[:]
        self.score = 0

    def _check_for_next_level(self):
        if len(self.previous_positions) >= LEVEL_LENGTH:
            self.score += LEVEL_LENGTH

            if self.level >= TOP_LEVEL:
                self.game_won = True
            else:
                self.next_level_state = True
                self.level += 1
                self.previous_positions = SNAKE_INITIAL_POSITIONS[:]
                self.rect.bottomleft = (400, 200)
                self.direction = Direction.RIGHT
                self.next_level_state = True

    def is_inside_snake(self, position):
        return position in self.previous_positions

    def is_game_active(self):
        # check for collision with self
        for position in self.previous_positions[:-3]:
            if self.rect.bottomleft == position:
                self.restart_level()
                return False

        # check if game was won
        if self.game_won:
            return False

        return True

    def update(self):
        self._player_input()
        self._player_movement()
        self._render_player()
        self._check_for_next_level()
