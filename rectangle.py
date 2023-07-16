import sys
import pygame

# from random import randint

# clock = pygame.time.Clock()
# clock.tick(5) # call in main loop to slow events

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RECT_WIDTH = 100
RECT_HEIGHT = 200

RECT_X = SCREEN_WIDTH / 2 - RECT_WIDTH / 2
RECT_Y = SCREEN_HEIGHT / 2 - RECT_HEIGHT / 2

RECT_COLOR = pygame.Color('lightyellow')

STEP = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rect to move")

# screen.fill((255, 255, 255))
screen.fill(pygame.Color('yellow'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    if RECT_Y >= STEP:
                        RECT_Y -= STEP  # print("UP")
                case pygame.K_DOWN:
                    if RECT_Y <= SCREEN_HEIGHT - STEP - RECT_HEIGHT:
                        RECT_Y += STEP  # print("DOWN")
                case pygame.K_LEFT:
                    if RECT_X >= STEP:
                        RECT_X -= STEP  # print("LEFT")
                case pygame.K_RIGHT:
                    if RECT_X <= SCREEN_WIDTH - STEP - RECT_WIDTH:
                        RECT_X += STEP  # print("RIGHT")
            # OR
            # if event.key == pygame.K_UP:
            #     RECT_Y -= STEP  # print("UP")
            # elif event.key == pygame.K_DOWN:
            #     RECT_Y += STEP  # print("DOWN")
            # elif event.key == pygame.K_LEFT:
            #     RECT_X -= STEP  # print("LEFT")
            # elif event.key == pygame.K_RIGHT:
            #     RECT_X += STEP  # print("RIGHT")

        # print(event)
        screen.fill((32, 52, 71))
        # pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 200))  # (where, (color), (x, y, width, height))
        pygame.draw.rect(
            screen,
            RECT_COLOR,
            (RECT_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT)
        )  # (where, (color), (x, y, width, height))

        pygame.display.update()
