import sys
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_BG_COLOR = (32, 52, 71)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter")

fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x = SCREEN_WIDTH / 2 - fighter_width / 2
fighter_y = SCREEN_HEIGHT - fighter_height


screen.fill(SCREEN_BG_COLOR)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(fighter_image, (fighter_x, fighter_y))
    pygame.display.update()
