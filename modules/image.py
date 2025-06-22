import pygame
from .path import *

class Image():
    def __init__(self, width: int, height: int, x: int, y: int, name: str):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.NAME = name
        self.create_image()
    def create_image(self, flip_x = False):
        path = find_path("images/" + self.NAME)
        image = pygame.image.load(path)
        self.IMAGE = pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))
        self.IMAGE = pygame.transform.flip(self.IMAGE, flip_x, False)
    def show_image(self, screen):
        screen.blit(self.IMAGE, (self.X, self.Y))