import pygame
from enum import Enum, auto


SNAKE_SIZE = 50
LEVEL_SPEED = 50


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
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (400, 200)
        self.direction = Direction.RIGHT
        self.divider = 0
        self.previous_positions = [(250, 200), (300, 200), (350, 200), (400, 200)]
        self.next_move_possible = True

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

    def player_input(self):
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

    def player_movement(self):
        self.divider += 1

        if self.divider % LEVEL_SPEED == 0:
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
            self.is_alive()
            self.previous_positions.pop(0)

    def render_player(self):
        for position in self.previous_positions:
            position_rect = pygame.Rect(
                position[0], position[1], SNAKE_SIZE, SNAKE_SIZE
            )
            position_rect.bottomleft = (position[0], position[1])

            pygame.draw.rect(
                self.surface,
                "red",
                position_rect,
            )

    def extend_snake(self, postion):
        print("robak zjedzony")
        self.previous_positions.append(postion)

    def is_alive(self):
        print("all snake positions: ", self.previous_positions)
        print("self.rect.bottomleft: ", self.rect.bottomleft)

        for position in self.previous_positions[:-2]:
            if self.rect.bottomleft == position:
                return False

        return True

    def update(self):
        self.player_input()
        self.player_movement()
        self.render_player()
