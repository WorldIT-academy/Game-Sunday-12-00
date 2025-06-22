from .image import *
from .map import *
from .settings import *

class Object(Image):
    #сторовуем метод конструктор з параметрамі персанажа 
    def __init__(self, width: int, height: int, x: int, y: int, name: str, speed: int):
        #успотковоем метод з image
        Image.__init__(self, width, height, x, y, name)
        self.SPEED = speed
        self.GRAVITY_SPEED = 5
        self.STAND_COUNTER = 0
        # Створюємо лічильник руху ( для змінення зображення )
        self.IS_CROUCHING = False
        self.DIRECTION = "r"
        # Створюємо лічильник руху ( для змінення зображення )
        self.MOVE_COUNTER = 0
        self.JUMP_COUNTER = 0

    #створюємо метод перевірки колізії
    def check_colision(self):
        #створюємо прямокутник області персонажа
        hero_rect = pygame.Rect(self.X + 6, self.Y + 18, self.WIDTH - 12, self.HEIGHT - 18)
        if self.IS_CROUCHING:
            hero_rect.y += 10
            hero_rect.height -=10
        #створюємо властивості дозволу на рух персонажа
        self.CAN_FALL = True
        self.CAN_MOVE_RIGHT = True
        self.CAN_MOVE_LEFT = True
        #перебираємо список блоків
        for block in map1.RECT_LIST:
            #створюємо прямокутники для сторін блоку
            rect_top = pygame.Rect(block.x + 8, block.y, block.width - 16, 1)
            rect_left = pygame.Rect(block.x, block.y + 5, 1, block.height - 10)
            rect_right = pygame.Rect(block.x + block.width, block.y + 5, 1, block.height - 10)
            rect_bottom = pygame.Rect(block.x + 8, block.y + block.height, block.width - 16 ,1)
            
            #перевіряємо дотик та забороняємо рух
            if hero_rect.colliderect(rect_top):        
                self.CAN_FALL = False
                self.Y = block.y - self.HEIGHT + 1
            if hero_rect.colliderect(rect_left):        
                self.CAN_MOVE_RIGHT = False
            if hero_rect.colliderect(rect_right):        
                self.CAN_MOVE_LEFT = False
            if hero_rect.colliderect(rect_bottom): 
                self.JUMP_COUNTER = 0 
                