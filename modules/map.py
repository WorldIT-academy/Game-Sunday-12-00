import pygame, pytmx
from .path import *
from .settings import *

class Map():
    def __init__(self, name: str):
        path = find_path(name)
        self.tile_map = pytmx.load_pygame(path)
        self.HEIGHT = self.tile_map.tileheight
        self.WIDTH = self.tile_map.tilewidth
        self.COUNT_BLOCK = self.tile_map.width
        self.RECT_LIST = []
        self.MAP_X = 0
        self.create_colision()
        self.create_object()

    def draw(self, screen):
        for layer in self.tile_map.visible_layers:
            if layer.name not in ["Collision Layer", "egg", "key", "meat", "enemy", "frog"]:
                for x, y, tile in layer:
                    if tile != 0:
                        image = self.tile_map.get_tile_image_by_gid(tile)
                        screen.blit(image,(x *self.WIDTH + self.MAP_X, y * self.HEIGHT))
    def create_colision(self):
        self.RECT_LIST = []
        layer = self.tile_map.get_layer_by_name("Collision Layer")
        for object in layer:
            rect = pygame.Rect(object.x + self.MAP_X, object.y, object.width, object.height)
            self.RECT_LIST.append(rect)
    def create_object(self):
        self.ENEMIES = []
        self.OBJECTS = []
        self.FINISH_RECT = None
        for layer in self.tile_map.visible_layers:
            if layer.name != "Collision Layer":
                for x, y, tile in layer:
                    if tile != 0:
                        if layer.name in ["egg", "key", "meat"]:
                            image = self.tile_map.get_tile_image_by_gid(tile)
                            self.OBJECTS.append([layer.name, image, x * self.WIDTH, y * self.HEIGHT])
                        elif layer.name == "enemy" or layer.name == "frog":
                            index = len(self.ENEMIES)
                            move_count = enemy_move_count[index] * self.WIDTH
                            self.ENEMIES.append([
                                layer.name, 
                                x * self.WIDTH, 
                                y * self.HEIGHT, 
                                x * self.WIDTH + move_count 
                            ])
                        elif layer.name == "finish":
                            self.FINISH_RECT = pygame.Rect(x * self.WIDTH, y * self.HEIGHT, self.WIDTH, self.HEIGHT)
            # if layer.name == "egg" or layer.name == "key" or layer.name == "meat":
                
    
map1 = Map("tilemaps/map.tmx")
