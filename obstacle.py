import pygame
import random


OBSTACLE_SIZE = 50


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, surface, snake):
        super().__init__()
        self.surface = surface
        self.snake = snake
        self.surface_width = surface.get_width()
        self.surface_height = surface.get_height()

        self.image = pygame.Surface((OBSTACLE_SIZE, OBSTACLE_SIZE))
        self.image.fill((70, 57, 86))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.generate_position()

    def generate_position(self):
        position = None

        while not position:
            generated_position = (
                random.randrange(0, self.surface_width - OBSTACLE_SIZE, OBSTACLE_SIZE),
                random.randrange(OBSTACLE_SIZE, self.surface_height, OBSTACLE_SIZE),
            )

            if self.snake.is_inside_snake(generated_position):
                continue
            else:
                position = generated_position
        return position
