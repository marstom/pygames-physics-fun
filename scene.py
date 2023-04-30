import pygame
from pygame import Surface


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

    rect = Rect()

    def render(self, screen: Surface):
        pygame.draw.rect(screen, [255, 0, 0], [self.rect.w, self.rect.h, self.rect.x, self.rect.y])
        self.rect.refresh()

    def move(self, event):
        if event.key == pygame.K_d:
            self.rect.vel_x +=1
        if event.key == pygame.K_a:
            self.rect.vel_x -=1

        print(event)