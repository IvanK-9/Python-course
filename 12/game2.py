import pygame
pygame.init()

# Размеры окна
W, H = 600, 400
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Grafisk primitiver")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Заливаем фон белым цветом
sc.fill(WHITE)

# Рисуем фигуры
pygame.draw.rect(sc, BLUE, (10, 10, 50, 100), 2)  # Прямоугольник с контуром

pygame.draw.line(sc, GREEN, (200, 20), (350, 50), 2)  # Прямая линия
pygame.draw.aaline(sc, GREEN, (200, 40), (350, 70))  # Сглаженная линия

pygame.draw.polygon(sc, RED, [(200, 80), (250, 80), (300, 200)])  # Залитый треугольник
pygame.draw.polygon(sc, RED, [(200, 40), (350, 70), (400, 200)], 2)  # Контурный треугольник

pygame.draw.circle(sc, BLUE, (300, 250), 40)  # Залитый круг

# Исправленный вызов ellipse (убраны лишние параметры)
pygame.draw.ellipse(sc, RED, (450, 30, 50, 150), 5)  # Эллипс с контуром

# Дуга (нижняя половина эллипса)
pygame.draw.arc(sc, RED, (450, 30, 50, 150), 3.14, 6.28, 5)

# Обновляем экран
pygame.display.update()

# Основной цикл обработки событий
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Корректное завершение Pygame
            exit()
