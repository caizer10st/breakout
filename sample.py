import pygame
import random

# 초기 설정
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 패들 설정
paddle_width, paddle_height = 100, 10
paddle_x, paddle_y = (width - paddle_width) // 2, height - 20
paddle_speed = 6

# 공 설정
ball_radius = 10
ball_x, ball_y = width // 2, height // 2
ball_speed_x, ball_speed_y = 4, -4

# 벽돌 설정
brick_width, brick_height = 80, 30
brick_rows, brick_columns = 5, 8
bricks = []

for i in range(brick_rows):
    for j in range(brick_columns):
        bricks.append(pygame.Rect(j * (brick_width + 10) + 35, i * (brick_height + 10) + 35, brick_width, brick_height))

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_speed

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 공의 벽 충돌
    if ball_x <= 0 or ball_x >= width - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y
    if ball_y >= height:
        break  # 게임 종료 조건

    # 패들 충돌
    if ball_x >= paddle_x and ball_x <= paddle_x + paddle_width and ball_y >= paddle_y - ball_radius:
        ball_speed_y = -ball_speed_y

    # 벽돌 충돌
    ball_rect = pygame.Rect(ball_x, ball_y, ball_radius, ball_radius)
    for brick in bricks[:]:
        if ball_rect.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y
            break

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
