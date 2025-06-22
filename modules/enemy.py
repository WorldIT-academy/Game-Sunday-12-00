from .object import *
from .hero import *

class Enemy(Object):
    def __init__(self, width: int, height: int, x: int, y: int, name: str, speed: int, finish_x: int, type: str ):
        Object.__init__(self, width, height, x, y, name, speed)
        self.FINISH_X = finish_x
        self.START_X = x
        self.ENEMY_DEAD = False
        self.DEAD_COUNTER = 0
        self.TYPE = type 
        self.STAND_COUNTER = 80
    def move(self):
        self.check_colision()
        if self.TYPE == 'frog':
            self.jump()
        
        if self.X > self.FINISH_X or self.CAN_MOVE_RIGHT == False:
            self.DIRECTION = "l"
            self.create_image(True)
        elif self.X < self.START_X or self.CAN_MOVE_LEFT == False:
            self.DIRECTION = "r"
            self.create_image()
        
        if self.ENEMY_DEAD == False:
            if self.STAND_COUNTER == 80:
                if self.DIRECTION == "r":
                    self.X += self.SPEED
                else:
                    self.X -= self.SPEED
                self.MOVE_COUNTER += 1
            
        if self.CAN_FALL == True and self.JUMP_COUNTER == 0:
            self.Y += self.GRAVITY_SPEED

        self.animation()
        self.hero_collision()
    def animation(self):
        if self.ENEMY_DEAD == True:
            self.DEAD_COUNTER += 1
            image_number = self.DEAD_COUNTER//9
            self.NAME = f"{self.TYPE}/death/{image_number}.png"
            if self.DEAD_COUNTER >= 53:
                enemy_list.remove(self)
        else:
            if self.TYPE == "frog":
                if self.STAND_COUNTER < 80:
                    image_number = self.STAND_COUNTER // 10
                    if image_number >= 4:
                        image_number -= 4
                    self.NAME = f'frog/idle/{image_number}.png'
                elif self.JUMP_COUNTER == 0:
                    self.NAME = "frog/gravity/0.png"
                else:
                    self.NAME = "frog/jump/0.png"
            else:
                image_number = self.MOVE_COUNTER//4
                self.NAME = f"enemy/run/{image_number}.png"
                if self.MOVE_COUNTER >= 15:
                    self.MOVE_COUNTER = 0
        if self.DIRECTION == "r":
            self.create_image()
        else:
            self.create_image(True)
    def hero_collision(self):
        hero_rect = pygame.Rect(hero1.X, hero1.Y, hero1.WIDTH, hero1.HEIGHT)
        enemy_rect = pygame.Rect(self.X+10, self.Y+ 15, self.WIDTH-20, self.HEIGHT-15)
        if hero_rect.colliderect(enemy_rect):
            if hero1.CAN_FALL == True and hero1.JUMP_COUNTER == 0:
                self.ENEMY_DEAD = True
            elif self.TYPE == "frog" and hero1.COUNT_DAMAGE == 0 and self.ENEMY_DEAD == False:
                hero1.COUNT_HEARTS -= 1
                if hero1.COUNT_HEARTS > 0: 
                    del heart_list[-1]
                    if hero1.X > self.X:
                        hero1.COUNT_DAMAGE = 10
                    else:
                        hero1.COUNT_DAMAGE = -10
    def jump(self):
        if self.ENEMY_DEAD == False:
            if self.CAN_FALL == False and self.STAND_COUNTER == 80:
                self.STAND_COUNTER = 0
            if self.STAND_COUNTER < 80:
                self.STAND_COUNTER += 1
                if self.STAND_COUNTER == 80:
                    self.JUMP_COUNTER = 15
            if self.JUMP_COUNTER > 0:
                self.JUMP_COUNTER -= 1 
                self.Y -= 5 
            
        

for enemy in map1.ENEMIES:
    new_enemy = Enemy(50, 50, enemy[1], enemy[2], "enemy.png", 2, enemy[3], enemy[0])
    enemy_list.append(new_enemy)
