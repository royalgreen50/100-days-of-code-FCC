import pygame
pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Chess Game")
display.fill((255, 255, 255))
running = True
clock = pygame.time.Clock()
FPS = 60
while running:
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()