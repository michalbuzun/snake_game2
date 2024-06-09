import pygame
import random

OBSTACLE_SIZE = 50


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        print("surface size width: ", surface.get_width())
        self.surface = surface
        self.surface_width = surface.get_width()
        self.surface_height = surface.get_height()

        self.image = pygame.Surface((OBSTACLE_SIZE, OBSTACLE_SIZE))
        self.image.fill("blue")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (
            random.randrange(0, self.surface_width - OBSTACLE_SIZE, OBSTACLE_SIZE),
            random.randrange(OBSTACLE_SIZE, self.surface_height, OBSTACLE_SIZE),
        )

    # def player_input(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_UP] or keys[pygame.K_w]:
    #         self.direction = Direction.UP

    #     if keys[pygame.K_DOWN] or keys[pygame.K_s]:
    #         self.direction = Direction.DOWN

    #     if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    #         self.direction = Direction.RIGHT

    #     if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    #         self.direction = Direction.LEFT
