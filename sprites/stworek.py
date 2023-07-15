from pygame import Surface
import pygame
from . import autko


#TODO to rewrite
class Stworek(autko.Autko):
    def __init__(self, screen: Surface, x=120, y=120, type: autko.TypeOfBall = autko.TypeOfBall.EVIL):
        super().__init__(screen, x, y, type)
        self.image = pygame.image.load("assets/cat.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.crash_sound = pygame.mixer.Sound("assets/meow2.mp3")
    ...