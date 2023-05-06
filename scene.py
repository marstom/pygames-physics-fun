import pygame
from pygame import Surface
from autko import Autko
from pygame.sprite import Sprite, Group
from enums import Dir, TurnDir, AccDir


class Rect:
    w = 10
    h =10
    x = 12
    y = 32

    vel_x = 0
    frict = 0.01

    def refresh(self):
        self.x += self.vel_x
        self.vel_x -= self.frict


class Scene:
    position = [0,0]
    sprites: Group

    rect = Rect()

    def __init__(self, sprites) -> None:
        self.sprites = sprites
        self.autko = Autko()
        self.sprites.add(self.autko)

    def render(self, screen: Surface):
        pygame.draw.rect(screen, [255, 0, 0], [self.rect.w, self.rect.h, self.rect.x, self.rect.y])
        self.sprites.update()
        self.rect.refresh()

        self.sprites.draw(screen)

    def move(self, event):
        print("Move")
        if event.key == pygame.K_w:
            self.autko.accelerate(AccDir.FORWARD)
        if event.key == pygame.K_s:
            self.autko.accelerate(AccDir.BACKWARD)
        if event.key == pygame.K_a:
            self.autko.turn(TurnDir.R)
        if event.key == pygame.K_d:
            self.autko.turn(TurnDir.L)

    def stop(self, event):
        print("Stop")
        self.autko.stop()
        # if event.key == pygame.K_d:
        # if event.key == pygame.K_a:
            # self.autko.stop()
            # ...

        print(event)