import pygame
from pygame import Surface
from autko import Autko
from pygame.sprite import Sprite, Group
from enums import Dir


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
        if event.key == pygame.K_d:
            self.autko.accelerate_x(Dir.R)
        if event.key == pygame.K_a:
            self.autko.accelerate_x(Dir.L)

    def stop(self, event):
        print("Stop")
        if event.key == pygame.K_d:
            self.autko.stop_x()
        if event.key == pygame.K_a:
            self.autko.stop_x()
            ...

        print(event)