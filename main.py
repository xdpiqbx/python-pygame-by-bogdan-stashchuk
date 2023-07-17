import sys
from random import randint

import pygame

pygame.init()

game_font = pygame.font.Font(None, 30)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_BG_COLOR = (32, 52, 71)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter")

FIGHTER_STEP = 0.8
fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()  # 70 X 65 = 14 X 13
fighter_x = SCREEN_WIDTH / 2 - fighter_width / 2
fighter_y = SCREEN_HEIGHT - fighter_height
is_fighter_moving_left = False
is_fighter_moving_right = False

ROCKET_STEP = 0.4
rocket_image = pygame.image.load('images/rocket.png')
rocket_width, rocket_height = rocket_image.get_size()  # 20 X 20 = 1 X 1
rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2
rocket_y = fighter_y - rocket_height
is_rocket_launched = False

ALIEN_STEP = 0.1
alien_speed = ALIEN_STEP
alien_image = pygame.image.load('images/alien.png')
alien_width, alien_height = alien_image.get_size()  # 45 X 59
alien_x = randint(0, SCREEN_WIDTH - alien_width)
alien_y = 0

game_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_LEFT:
                    is_fighter_moving_left = True
                case pygame.K_RIGHT:
                    is_fighter_moving_right = True
                case pygame.K_SPACE:
                    is_rocket_launched = True
                    rocket_y = fighter_y - rocket_height
                    rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_LEFT:
                    is_fighter_moving_left = False
                case pygame.K_RIGHT:
                    is_fighter_moving_right = False

    if is_fighter_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP  # print("LEFT")
    if is_fighter_moving_right and fighter_x <= SCREEN_WIDTH - FIGHTER_STEP - fighter_width:
        fighter_x += FIGHTER_STEP  # print("RIGHT")

    if is_rocket_launched:
        rocket_y -= ROCKET_STEP
    if is_rocket_launched and rocket_y + rocket_height <= 0:
        is_rocket_launched = False

    screen.fill(SCREEN_BG_COLOR)

    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(alien_image, (alien_x, alien_y))
    if is_rocket_launched:
        screen.blit(rocket_image, (rocket_x, rocket_y))

    alien_y += alien_speed

    game_score_text = game_font.render(f"Score: {game_score}", True, 'white')
    screen.blit(game_score_text, (15, 15))

    pygame.display.update()

    if is_rocket_launched \
            and alien_x - rocket_width * 0.5 < rocket_x < alien_x + (alien_width - rocket_width * 0.5) \
            and alien_y < rocket_y < alien_y + alien_height - rocket_height * 2:
        game_score += 1
        is_rocket_launched = False
        alien_speed += ALIEN_STEP / 10
        alien_y = 0
        alien_x = randint(0, SCREEN_WIDTH - alien_width)

    # Game Over
    if alien_y + alien_height > fighter_y + fighter_height / 2:
        break

game_over_text = game_font.render("Game Over", True, 'white')
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
screen.blit(game_over_text, game_over_rect)

pygame.display.update()
pygame.time.wait(1000)
pygame.quit()
