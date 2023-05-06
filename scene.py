import pygame
from pygame import Surface
from autko import Autko
from pygame.sprite import Sprite, Group
from enums import TurnDir, AccDir


class Scene:
    position = [0,0]
    sprites: Group

    def __init__(self, sprites) -> None:
        self.sprites = sprites
        self.autko = Autko()
        self.sprites.add(self.autko)

    def render(self, screen: Surface):
        # pygame.draw.rect(screen, [255, 0, 0], [self.rect.w, self.rect.h, self.rect.x, self.rect.y])
        self.sprites.update()
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
        # TODO only stop if acc keys pressed
        self.autko.stop()