import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OOPong")
direction = [0, 1]
angle = [0, 1, 2]

#ball
radius = 15
ball_x, ball_y =  WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7

#paddle
paddle_width = 20
paddle_height = 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0

run = True
while run:
    screen.fill("black")
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9

        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0

    # ball movement
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4

        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
        ball_vel_x *= -1

    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4

        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4

    # PADDLE MOVEMENT
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    # PADDLE COLLISIONS
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1

    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1

    #MOVEMENT
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    left_paddle_y += left_paddle_vel
    right_paddle_y += right_paddle_vel




    #OBJECT
    pygame.draw.circle(screen, "white", (ball_x, ball_y), radius)
    pygame.draw.rect(screen, "red", pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, "red", pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    pygame.display.update()