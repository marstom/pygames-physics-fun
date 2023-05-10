import pygame
from pygame import Surface
from sprites.autko import Autko
from pygame.sprite import Group
from enums import TurnDir, AccDir
from sprites.grass import Grass


class Scene:
    position = [0,0]
    sprites: Group

    def __init__(self, screen: Surface, sprites: Group, screen_width: int, screen_height: int) -> None:
        self.sprites = sprites
        self.autko = Autko(screen)
        self.screen_width = screen_width
        self.screen_height = screen_height

        # grass = Grass()

        self.sprites.add(self.autko)
        # self.sprites.add(grass)

        # draw background
        self.bg = pygame.image.load("assets/bg.jpeg")
        self.bg = pygame.transform.scale(self.bg, ( self.screen_width, self.screen_height))

    def render(self, screen: Surface):
        # Draw level background
        screen.blit(self.bg, (0,0))

        # pygame.draw.rect(screen, [255, 0, 0], [self.rect.w, self.rect.h, self.rect.x, self.rect.y])
        self.sprites.update()
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