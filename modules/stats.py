from .settings import *
from .image import *
from .hero import *

# Ініціалізуємо налаштування pygame, для роботи з текстом
pygame.init()

# Створюємо картинки ресурсів, для індекаторів кількості
egg_stat = Image(50,50,180,0,"map/egg.png")
key_stat = Image(50,50,279,0,"map/key.png")
meat_stat = Image(50,50,370,-2,"map/meat.png")
for i in range(hero1.COUNT_HEARTS):
    heart_stats = Image(24,24,20 + i * 24,15,"heart.png")
    heart_list.append(heart_stats)
# Налаштовужємо шрифт, та вказуємо розмір
font = pygame.font.Font(None, 30)
lose_font = pygame.font.Font(None, 100)
lose_text = lose_font.render("Ви програли", True, "white")
win_text = lose_font.render("Ви перемогли", True, "white")

# Створюємо функцію зображень тексту
def show_text():
    # Зображуємо картинки
    egg_stat.show_image(screen)
    key_stat.show_image(screen)
    meat_stat.show_image(screen)
    for heart in heart_list:
        heart.show_image(screen)
    # Створюємо цикл на 3 повторення
    for i in range(3):
        # Створюємо текст
        text = font.render(str(count_object[i]), True, "white")
        # Зображуємо текст на екрані
        screen.blit(text,(230 + i * 100, 15))