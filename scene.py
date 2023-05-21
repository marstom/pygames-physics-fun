import pygame
from pygame import Surface
from sprites.autko import Autko
from pygame.sprite import Group
from enums import TurnDir, AccDir
from sprites.grass import Grass

from pygame.math import Vector2
from random import randint, uniform

class Scene:
    position = [0, 0]
    sprites: Group

    def __init__(self, screen: Surface, sprites: Group, screen_width: int, screen_height: int) -> None:
        self.sprites = sprites
        self.autko = Autko(screen, type=Autko.TypeOfBall.PLAYER)
        self.screen_width = screen_width
        self.screen_height = screen_height


        if 1:
            for _ in range(32):
                rand_angle = uniform(0, 360)
                rand_speed = uniform(1,5)
                rand_pos = [uniform(0, 800), uniform(0, 800)]
                evil = Autko(screen, x=rand_pos[0], y=rand_pos[1], type=Autko.TypeOfBall.EVIL)
                evil.velocity = Vector2(rand_speed, 0).rotate(rand_angle)
                sprites.add(evil)
        
        if 0:
            evil2= Autko(screen, x=290, y=120, type=Autko.TypeOfBall.EVIL)
            sprites.add(evil2)

        # grass = Grass()

        self.sprites.add(self.autko)
        # self.sprites.add(grass)

        # draw background
        self.bg = pygame.image.load("assets/bg.jpeg")
        self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))

    def render(self, screen: Surface):
        # Draw level background
        screen.blit(self.bg, (0, 0))

        # pygame.draw.rect(screen, [255, 0, 0], [self.rect.w, self.rect.h, self.rect.x, self.rect.y])
        # print(pygame.sprite.spritecollide(self.autko, self.sprites, False))
        self.sprites.update(sprites=self.sprites)
        self.sprites.draw(screen)

    def key_down(self, event):
        print("Move")
        if event.key == pygame.K_w:
            self.autko.accelerate(AccDir.FORWARD)
        if event.key == pygame.K_s:
            self.autko.accelerate(AccDir.BACKWARD)
        if event.key == pygame.K_a:
            self.autko.turn(TurnDir.R)
        if event.key == pygame.K_d:
            self.autko.turn(TurnDir.L)

    def key_up(self, event):
        print("Stop")
        # TODO only stop if acc keys pressed
        change_speed_keys = [pygame.K_w, pygame.K_s]
        if event.key in change_speed_keys:
            self.autko.accelerate_stop()
        turn_keys = [pygame.K_a, pygame.K_d]
        if event.key in turn_keys:
            self.autko.turn_stop()
