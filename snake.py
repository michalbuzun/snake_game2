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
        self.image = pygame.Surface((SNAKE_SIZE, SNAKE_SIZE))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (400, 200)
        self.direction = Direction.RIGHT
        self.divider = 0
        self.previous_positions = [(250, 200), (300, 200), (350, 200), (400, 200)]

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.direction != Direction.DOWN:
                self.direction = Direction.UP

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.direction != Direction.UP:
                self.direction = Direction.DOWN

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.direction != Direction.LEFT:
                self.direction = Direction.RIGHT

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.direction != Direction.RIGHT:
                self.direction = Direction.LEFT

    def player_movement(self):
        self.divider += 1

        if self.divider % LEVEL_SPEED == 0:
            if self.direction == Direction.RIGHT:
                self.rect.x += SNAKE_SIZE
            if self.direction == Direction.LEFT:
                self.rect.x -= SNAKE_SIZE
            if self.direction == Direction.UP:
                self.rect.y -= SNAKE_SIZE
            if self.direction == Direction.DOWN:
                self.rect.y += SNAKE_SIZE

            self.previous_positions.append(self.rect.bottomleft)
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
        self.previous_positions.append(postion)

    def update(self):
        self.player_input()
        self.player_movement()
        self.render_player()
