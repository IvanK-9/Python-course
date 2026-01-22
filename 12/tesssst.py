import pygame
pygame.init()

pygame.display.set_mode((600, 400), pygame.DOUBLEBUF | pygame.HWSURFACE )
pygame.display.set_caption("MY f1rst PYGame")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    clock.tick(60)

