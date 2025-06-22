import pygame

screen = pygame.display.set_mode((1300, 800))
pygame.display.set_caption("Game")

FPS = pygame.time.Clock()

count_object = [0,0,0]
enemy_list = []
enemy_move_count = [2, 6, 6, 3, 10, 10, 2, 4]
heart_list = []