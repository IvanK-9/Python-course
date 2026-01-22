import sys
import pygame

def run_game():
    # Initialize window
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")
    
    # Define windows color (RGB)
    bg_color = (0, 102, 204) # Синий цвет [13]

    while True:
        # Отслеживание событий клавиатуры и мыши [14]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Применение цвета фона и обновление экрана [15, 16]
        screen.fill(bg_color)
        pygame.display.flip()

run_game()