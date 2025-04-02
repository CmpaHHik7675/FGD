import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Перша гра в Pygame")

# Колір фону рандомно
BACKGROUND_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Колір прямокутника
RECT_COLOR = (255, 0, 0)
rect_x, rect_y = WIDTH // 2, HEIGHT // 2  # Початкові координати прямокутника

# Основний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обробка руху миші
        if event.type == pygame.MOUSEMOTION:
            rect_x, rect_y = event.pos  # Зміщення прямокутника в позицію миші

        # Обробка натискання клавіші
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_x -= 10  # Переміщення ліворуч
            elif event.key == pygame.K_RIGHT:
                rect_x += 10  # Переміщення праворуч
            elif event.key == pygame.K_UP:
                rect_y -= 10  # Переміщення вгору
            elif event.key == pygame.K_DOWN:
                rect_y += 10  # Переміщення вниз
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Заповнення фону кольором
    screen.fill(BACKGROUND_COLOR)

    # Малювання прямокутника
    pygame.draw.rect(screen, RECT_COLOR, (rect_x, rect_y, 50, 50))

    # Оновлення екрану
    pygame.display.flip()

pygame.quit()
