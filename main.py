import threading
import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load('img/crysis.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

# Изначальное положение цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Создаем флаг для остановки потока
stop_flag = False


# Создаем функцию для перемещения цели
def move_target():
    global target_x, target_y, stop_flag
    while not stop_flag:
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        pygame.time.delay(2000)  # Подождать 2 секунды


# Запускаем поток для перемещения цели
target_thread = threading.Thread(target=move_target)
target_thread.start()

running = True
while running:
    screen.fill(color)

    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_flag = True
            running = False

        # Проверяем, попал ли курсор мыши в область цели
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Добавили обновление цвета при попадании в цель
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

# Останавливаем поток перед выходом из программы
target_thread.join()

pygame.quit()
