from typing import Any
import pygame
from pygame import Rect
from pygame.math import Vector2
from constatnts import SCREEN_H, SCREEN_W
from enums import AccDir, TurnDir


class Autko(pygame.sprite.Sprite):
    coefficient_of_friction = 0.22

    turn_speed = 0.0
    turn_value_degrees = 0.0


    def __init__(self, x=120, y=120):
        super().__init__()
        self.image = pygame.image.load("assets/aqua_ball.png").convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)


    def accelerate(self, dir: AccDir):
        print("ACC")
        # TODO accalerate has ange, must be update every frame !
        if dir == AccDir.FORWARD:
            self.acceleration = Vector2(0.6, 0).rotate(self.turn_value_degrees)
        if dir == AccDir.BACKWARD:
            self.acceleration = Vector2(-0.6, 0).rotate(self.turn_value_degrees)
            # self.acceleration.x = -0.6

    def accelerate_stop(self):
        self.acceleration.x = 0.0
        self.acceleration.y = 0.0
        print(f"!Stop {self.acceleration.x} {self.acceleration.y}")

    def turn_stop(self):
        self.turn_speed = 0

    def turn(self, dir: TurnDir):
        turn_strength_degrees = 4.00
        if dir == TurnDir.L:
            self.turn_speed +=turn_strength_degrees
        if dir == TurnDir.R:
            self.turn_speed -= turn_strength_degrees
        print(f"Turn.... {self.turn_value_degrees}")
            

    def update(self, *args: Any, **kwargs: Any) -> None:
        """
        Call every game loop
        """
        self._move_model_update()
        self._turning_update()
        self.__debug_prints()


        self.rect.x %= SCREEN_W 
        self.rect.y %= SCREEN_H 
        # return super().update(*args, **kwargs)

    def _move_model_update(self):
        self.velocity += self.acceleration
        if self.velocity.length() != 0:
            friction_force = -self.velocity.normalize() * self.coefficient_of_friction
            self.velocity += friction_force
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def _turning_update(self):
        self.turn_value_degrees += self.turn_speed
        self.turn_value_degrees %= 360.00

    def __debug_prints(self):
        print(f"Turn: {self.turn_value_degrees}")
        print(f"pos x y: {self.rect}")
        
