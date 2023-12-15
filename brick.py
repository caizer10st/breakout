import pygame
import sys

# 초기 설정
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("벽돌 게임")
clock = pygame.time.Clock()
# brick.py
background = pygame.image.load("/Users/caizer10/workspace/brick_game/ground.png")
speed_increase_interval = 10000  # 10초
ball_speed = 5
last_speed_increase_time = pygame.time.get_ticks()

# 공 설정
ball = pygame.Rect(350, 350, 20, 20)
ball_dx = 1
ball_dy = 1

# 하단 바 설정
paddle = pygame.Rect(300, 680, 100, 10)
paddle_speed = ball_speed * 2
lives = 3

# 벽돌 설정
brick_width = 60
brick_height = 30
bricks = [pygame.Rect(j*brick_width, i*brick_height, brick_width, brick_height) for i in range(5) for j in range(10)]
brick_count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-paddle_speed, 0)
    if keys[pygame.K_RIGHT] and paddle.right < 700:
        paddle.move_ip(paddle_speed, 0)

    ball.move_ip(ball_dx * ball_speed, ball_dy * ball_speed)

    if ball.top <= 0 or ball.bottom >= 700:
        ball_dy = -ball_dy
    if ball.left <= 0 or ball.right >= 700:
        ball_dx = -ball_dx

    if ball.colliderect(paddle):
        ball_dy = -ball_dy

    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy = -ball_dy
            brick_count += 1
            break

    if ball.bottom >= 700:
        lives -= 1
        paddle.width *= 0.9
        ball = pygame.Rect(350, 350, 20, 20)
        if lives == 0:
            print("게임 오버!")
            pygame.quit()
            sys.exit()

    if brick_count >= 10:
        paddle.width *= 1.1
        brick_count = 0

    if pygame.time.get_ticks() - last_speed_increase_time >= speed_increase_interval:
        ball_speed *= 1.1
        last_speed_increase_time = pygame.time.get_ticks()

    screen.blit(background, (0, 0))
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (0, 0, 0), paddle)  # 검은색 하단 바

    for brick in bricks:
        pygame.draw.rect(screen, (139, 69, 19), brick)  # 갈색 벽돌
        pygame.draw.rect(screen, (0, 0, 0), brick, 1)  # 벽돌 간 구분 표시

    pygame.display.flip()
    clock.tick(30)
