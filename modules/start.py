from .settings import *
from .map import *
from .hero import *
from .stats import *
from .enemy import *

def start_game():
    run = True
    while run:
        FPS.tick(90)
        screen.fill("#024C4A")
        if hero1.COUNT_HEARTS > 0 and hero1.WIN == False:
            
            map1.draw(screen)

            for object in map1.OBJECTS:
                name, image, x, y = object
                screen.blit(image, (x + map1.MAP_X, y))
            for enemy in enemy_list:
                enemy.show_image(screen)
                enemy.move()
            
            hero1.move()
            hero1.check_finish()
            hero1.show_image(screen)
            show_text()
        elif hero1.COUNT_HEARTS <= 0:  
            screen.blit(lose_text, (440, 350))
        else:
            screen.blit(win_text, (420, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()