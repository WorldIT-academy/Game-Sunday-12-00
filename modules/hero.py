from .object import *
#стоворуем клас персанажа
class Hero(Object):
    #сторовуем метод конструктор з параметрамі персанажа 
    def __init__(self, width: int, height: int, x: int, y: int, name: str, speed: int):
        #успотковоем метод з image
        Object.__init__(self, width, height, x, y, name, speed)
        self.DEFAULT_SPEED = speed
        # Властивісь яка зберігає номер зображення бігу
        self.IMAGE_NUMBER = 0
        # Властивісьб яка зберігає направлення персонажа
        self.COUNT_CROUCHING = 0
        # 0 - не отримує шкоди, -10 - потрібно рухати ліворуч, 10 - потрібно рухати праворуч
        self.COUNT_DAMAGE = 0
        self.COUNT_HEARTS = 5
        self.WIN = False
    #создает медод руху
    def move(self):
        #викликаємо метод перевірки колізії
        self.check_colision()
        self.collect_object()
        #отримуємо список натиснутих клавіш 
        self.list_key = pygame.key.get_pressed()
        self.animation()
        #перевіряємо натискання та рухаємо персонажа
        if self.list_key[pygame.K_d] and self.CAN_MOVE_RIGHT:
            # Збільшуємо лічильник коли персонаж рухається, та змінуємо напрям руху 
            self.MOVE_COUNTER += 1
            self.DIRECTION = "r"
            if self.X <= 650 or map1.MAP_X < -map1.COUNT_BLOCK * map1.WIDTH + 1300:
                self.X += self.SPEED
            else:
                map1.MAP_X -= self.SPEED
                for enemy in enemy_list:
                    enemy.X -= self.SPEED
                    enemy.START_X -= self.SPEED
                    enemy.FINISH_X -= self.SPEED
                map1.FINISH_RECT.x -= self.SPEED
                map1.create_colision()
                
        elif self.list_key[pygame.K_a] and self.CAN_MOVE_LEFT: 
            self.X -= self.SPEED 
            self.MOVE_COUNTER += 1
            self.DIRECTION = "l"
            
        if self.list_key[pygame.K_LCTRL] and self.CAN_FALL == False:
            self.IS_CROUCHING = True
            self.COUNT_CROUCHING += 1
            if self.COUNT_CROUCHING >= 29:
                self.COUNT_CROUCHING = 0
            self.SPEED = self.DEFAULT_SPEED//2
        else:
            self.IS_CROUCHING = False
            self.COUNT_CROUCHING = 0
            self.SPEED = self.DEFAULT_SPEED

        if self.CAN_FALL:
            self.Y += self.GRAVITY_SPEED
        self.jump()

        if self.COUNT_DAMAGE > 0:
            self.COUNT_DAMAGE -= 1
            if self.CAN_MOVE_RIGHT:
                self.X += 10
        if self.COUNT_DAMAGE < 0:
            self.COUNT_DAMAGE += 1
            if self.CAN_MOVE_LEFT:
                self.X -= 10

    def jump(self):
        if self.list_key[pygame.K_SPACE] and self.CAN_FALL == False:
            self.JUMP_COUNTER = 30
        if self.JUMP_COUNTER > 0:
            self.JUMP_COUNTER -= 1
            self.Y -= 10
    # Створюємо метод анімації
    def animation(self):
        # Перевіряємо що персонаж стрибає, та змінюємо його зображення
        if self.JUMP_COUNTER > 0:
            self.NAME = "player/jump/0.png"
        # Перевіряємо що персонаж не знаходиться на платформі ( падає ) та не стрибає
        if self.CAN_FALL == True and self.JUMP_COUNTER == 0:
            self.NAME = 'player/gravity/0.png'

        if self.IS_CROUCHING:
            self.NAME = f"player/crouch/{self.COUNT_CROUCHING//15}.png"
        # Перевіряємо що персонаж рухається вже 5 або більше кадрів
        elif self.MOVE_COUNTER >= 5:
            self.STAND_COUNTER = 0
            self.NAME = f"player/run/{self.IMAGE_NUMBER}.png"
            # Змінуємо картинку на наступну, та заново запускаємо анімацію
            self.IMAGE_NUMBER += 1
            if self.IMAGE_NUMBER >= 6:
                self.IMAGE_NUMBER = 0
            self.MOVE_COUNTER = 0
        # Перевіряємо що не натиснуті кнопки руху в сторону та персонаж не падає
        elif not (self.list_key[pygame.K_d] and self.CAN_MOVE_RIGHT ):
            if not (self.list_key[pygame.K_a] and self.CAN_MOVE_LEFT) and self.CAN_FALL == False: 
                # В такому випадку зупиняємо лічильник руху та змінюємо зображення
                self.MOVE_COUNTER = 0
                self.NAME = "hero.png"
                self.STAND_COUNTER += 1
                if self.STAND_COUNTER >= 48:
                    self.STAND_COUNTER = 0
                self.NAME = f"player/idle/{self.STAND_COUNTER//12}.png"

        if self.COUNT_DAMAGE != 0:
            self.NAME = "player/damage.png"
        # Якщо напрям руху праворуч, завантажуємо зображення. Інакше розгортаємо його
        if self.DIRECTION == "r":
            self.create_image()
        else:
            self.create_image(True)
            
    def collect_object(self):
        hero_rect = pygame.Rect(self.X + 6, self.Y + 18, self.WIDTH - 12, self.HEIGHT - 18)
        for object in map1.OBJECTS:
            object_rect = pygame.Rect(object[2] + map1.MAP_X + map1.WIDTH / 4, object[3] + map1.HEIGHT / 4, map1.WIDTH / 2, map1.HEIGHT / 2)
            if hero_rect.colliderect(object_rect):
                map1.OBJECTS.remove(object)
                if object[0] == "egg":
                    count_object[0] += 1
                elif object[0] == "key":
                    count_object[1] += 1
                elif object[0] == "meat":
                    count_object[2] += 1
    def check_finish(self):
        hero_rect = pygame.Rect(self.X + 6, self.Y +18, self.WIDTH - 12, self.HEIGHT - 18)
        if hero_rect.colliderect(map1.FINISH_RECT):
            self.WIN = True


hero1 = Hero(70, 70, 0, 0, "hero.png", 3)