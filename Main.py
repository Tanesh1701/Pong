import pygame
import random
import sys

pygame.init()

width = 750
height = 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Pong since I'm bored")
icon = pygame.image.load('racket.png')
pygame.display.set_icon(icon)

user = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
enemy = pygame.Rect(10, height / 2 - 70, 10, 140)
white = (255, 255, 255)
ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30)
ball_speed_x = 2 * random.choice((1, -1))
ball_speed_y = 2 * random.choice((1, -1))
y_change = 0
enemy_speed = 6
score_player = 0
score_enemy = 0


def restart():
    global ball_speed_y, ball_speed_x
    ball.center = (width / 2, height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


win = True
while win:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            win = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change -= 2
            if event.key == pygame.K_DOWN:
                y_change += 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_change += 2
            if event.key == pygame.K_DOWN:
                y_change -= 2

    user.y += y_change
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 0:
        restart()
        score_player += 1
    if ball.left >= width:
        restart()
        score_enemy += 1
    if ball.colliderect(user) or ball.colliderect(enemy):
        ball_speed_x *= -1

    if user.top <= 0:
        user.top = 0
    if user.bottom >= height:
        user.bottom = height

    if enemy.top < ball.y:
        enemy.top += enemy_speed
    if enemy.bottom > ball.y:
        enemy.bottom -= enemy_speed
    if enemy.top <= 0:
        enemy.top = 0
    if enemy.bottom >= height:
        enemy.bottom = height

    font = pygame.font.Font(None, 74)
    text = font.render(str(score_enemy), 1, white)
    screen.blit(text, (250, 10))
    text = font.render(str(score_player), 1, white)
    screen.blit(text, (420, 10))

    pygame.draw.rect(screen, white, user)
    pygame.draw.aaline(screen, (255, 255, 255), (width / 2, 0), (width / 2, height))
    pygame.draw.rect(screen, white, enemy)
    pygame.draw.ellipse(screen, white, ball)

    pygame.display.update()
