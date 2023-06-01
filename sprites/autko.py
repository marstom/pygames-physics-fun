from typing import Any

import pygame
from pygame import Surface
from pygame.math import Vector2

from constatnts import SCREEN_H, SCREEN_W
from enums import AccDir, TurnDir

from enum import Enum, auto

DEBUG_PRINTS = 0


class Autko(pygame.sprite.Sprite):
    class TypeOfBall(Enum):
        PLAYER = auto()
        EVIL = auto()

    coefficient_of_friction = 0.22

    turn_speed = 0.0
    turn_value_degrees = 4.0
    top_speed = 10.00

    accel: AccDir = AccDir.STOP

    FRICT = False
    SPEED_LIMIT = False

    def __init__(self, screen: Surface, x=120, y=120, type: TypeOfBall = TypeOfBall.PLAYER):
        super().__init__()
        self.screen = screen
        if type == self.TypeOfBall.PLAYER:
            self.image = pygame.image.load("assets/aqua_ball.png").convert_alpha()
        elif type == self.TypeOfBall.EVIL:
            self.image = pygame.image.load("assets/evil_ball.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = Vector2(self.rect.x, self.rect.y)

        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

    def accelerate(self, dir: AccDir):
        print("ACC")
        # TODO accalerate has ange, must be update every frame !
        if dir == AccDir.FORWARD:
            self.acceleration = Vector2(0.1, 0)
        if dir == AccDir.BACKWARD:
            self.acceleration = Vector2(-0.1, 0)

    def accelerate_stop(self):
        self.accel = AccDir.STOP
        self.acceleration.x = 0.0
        self.acceleration.y = 0.0
        print(f"!Stop {self.acceleration.x} {self.acceleration.y}")

    def turn_stop(self):
        self.turn_speed = 0

    def turn(self, dir: TurnDir):
        turn_strength_degrees = 4.00
        if dir == TurnDir.L:
            self.turn_speed = turn_strength_degrees
        if dir == TurnDir.R:
            self.turn_speed -= turn_strength_degrees
        print(f"Turn.... {self.turn_value_degrees}")

    def update(self, *args: Any, **kwargs: Any) -> None:
        """
        Call every game loop
        """
        sprites: list[Autko] = kwargs["sprites"]
        # collision logic
        for sp in sprites:
            if sp is not self and self.rect.colliderect(sp.rect):
                sp: Autko
                if sp is not self:
                    collision_normal = Vector2(sp.rect.center) - Vector2(self.rect.center)
                    if collision_normal.length() == 0:
                        break
                    collision_normal.normalize_ip()

                    # Calculate relative velocity
                    relative_velocity = self.velocity - sp.velocity

                    # Calculate dot product of relative velocity and collision normal
                    dot_product = relative_velocity.dot(collision_normal)

                    # Calculate impulse
                    impulse = -1 * dot_product * collision_normal

                    # Update velocities
                    self.velocity += impulse
                    sp.velocity -= impulse

        self._move_model_update()
        self._turning_update()
        if DEBUG_PRINTS:
            self.__debug_prints()
        self._visualise_vectors()

        # Screen scroll
        self.rect.x %= SCREEN_W
        self.rect.y %= SCREEN_H

    def _move_model_update(self):
        # self.acceleration = self.acceleration.rotate(self.turn_value_degrees)
        self.position.x = self.rect.x
        self.position.y = self.rect.y

        self.velocity += self.acceleration.rotate(self.turn_value_degrees)

        if self.FRICT:
            if self.velocity.length() != 0:
                friction_force = -self.velocity.normalize() * self.coefficient_of_friction
                self.velocity += friction_force
        # self.position.x += self.velocity.x
        # self.rect.y += self.velocity.y
        self.position += self.velocity

        # robi rogal
        if self.SPEED_LIMIT:
            if abs(self.velocity.x) >= abs(self.top_speed):
                self.velocity.x = self.top_speed if self.velocity.x > 0 else -self.top_speed
            if abs(self.velocity.y) >= abs(self.top_speed):
                self.velocity.y = self.top_speed if self.velocity.y > 0 else -self.top_speed
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def _turning_update(self):
        self.turn_value_degrees += self.turn_speed
        self.turn_value_degrees %= 360.00

    def __debug_prints(self):
        print(f"Turn: {self.turn_value_degrees}")
        print(f"pos x y: {self.rect} {self.position}")
        print(f"Vel: {self.velocity}")

    def _visualise_vectors(self):
        # Draw direction vectors
        x = self.rect.x
        y = self.rect.y
        # pos = Vector2(x + self.rect.h / 2, y + self.rect.h / 2)
        pos = self.position + Vector2(self.rect.h / 2, self.rect.w / 2)
        if self.acceleration.length() > 0:
            pygame.draw.line(
                self.screen,
                (255, 0, 0),
                self.acceleration.rotate(self.turn_value_degrees).normalize() * 50 + pos,
                pos,
                4,
            )
        else:
            if DEBUG_PRINTS:
                print(f"Degree {self.turn_value_degrees}")
            pygame.draw.line(
                surface=self.screen,
                color=(128, 128, 121),
                start_pos=pos,
                end_pos=pos + Vector2(50, 0).rotate(self.turn_value_degrees),
                width=4,
            )
        if self.velocity.length() > 0:
            pygame.draw.line(self.screen, (0, 125, 255), self.velocity.normalize() * 50 + pos, pos, 4)
        if self.velocity.length() > 0:
            pygame.draw.line(self.screen, (0, 125, 0), self.velocity * 10 + pos, pos, 4)


def show(sp: Autko):
    print(f"Params {sp.velocity}, {sp.acceleration} {id(sp)}")
