from typing import Any
import pygame
from pygame import Rect
from pygame.math import Vector2
from enums import Dir




class Vector2D:
    x: float = 0.0
    y: float = 0.0

# Define the sprite class
class Autko(pygame.sprite.Sprite):
    coefficient_of_friction = 0.18



    def __init__(self, x=120, y=120):
        super().__init__()
        self.image = pygame.image.load("assets/car.png").convert_alpha()
        self.image.set_colorkey((255,255,255))
        # pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)


    def accelerate_x(self, dir: Dir):
        if dir == Dir.R:
            self.acceleration.x = 0.6
        if dir == Dir.L:
            self.acceleration.x = -0.6

    def stop_x(self):
        self.acceleration.x = 0.0
        self.acceleration.y = 0.0

    def turn(self):
        self.acceleration.rotate_ip(1)

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.velocity += self.acceleration
        # self.acceleration.rotate_ip(5)

        if self.velocity.length() > 0:
            friction_force = -self.velocity.normalize() * self.coefficient_of_friction
            self.velocity += friction_force

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y



        return super().update(*args, **kwargs)