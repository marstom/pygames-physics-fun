from typing import Any
import pygame
from pygame import Rect


class Vector2D:
    x: float = 0.0
    y: float = 0.0

# Define the sprite class
class Autko(pygame.sprite.Sprite):
    friction = 0.11


    def __init__(self, x=120, y=120):
        super().__init__()
        self.image = pygame.image.load("assets/car.png").convert_alpha()
        self.image.set_colorkey((255,255,255))
        # pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = Vector2D()


    def speed_x(self):
        self.speed.x = 5.0

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

        self.speed.x -= self.friction if self.speed.x >= 0 else 0
        self.speed.y -= self.friction if self.speed.y >= 0 else 0


        return super().update(*args, **kwargs)