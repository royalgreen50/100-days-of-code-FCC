import itertools
import pygame
pygame.init()
#Initialize Pygame
display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Chess Game")
display.fill((0, 0, 0))
running = True
clock = pygame.time.Clock()
FPS = 60
#Create Game board

def draw_board():
    for i, j in itertools.product(range(8), range(8)):
        if (i + j) % 2 == 0:
            pygame.draw.rect(display, (192, 192, 192), (i * 100, j * 100, 100, 100))
        else:
            pygame.draw.rect(display, (169, 169, 169), (i * 100, j * 100, 100, 100))

draw_board()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
