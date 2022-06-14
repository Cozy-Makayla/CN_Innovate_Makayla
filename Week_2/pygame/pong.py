import pygame, sys
from random import choice

pygame.init()   # starts the pygame modules (required for pygame to run)

WHITE = pygame.Color(255, 255, 255)
L_GREY = pygame.Color(200, 200, 200)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
BLACK = pygame.Color(0, 0, 0)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
player_score = 0
opponent_score = 0
prev_collision = 'null'
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 0
x = 0

ball = pygame.Rect(
    screen_width /2 -11,
    screen_height /2 -15,
    20, 20
)

player = pygame.Rect(
    screen_width -27,
    screen_height /2 -70,
    20, 140
)

opponent = pygame.Rect(
    10,
    screen_height /2 -70,
    20, 140
)

score_board = pygame.Rect(0, screen_height - 5, 30, 10)

def ball_animation():
    global ball_speed_x
    global ball_speed_y
    global prev_collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.right >= screen_width:
        ball_reset()
        score('opponent')
    if ball.left <= 0:
        ball_reset()
        score('player')

    if prev_collision != 'player':
        if ball.colliderect(player):
            ball_speed_x *= -1
            prev_collision = 'player'

    if prev_collision != 'opponent':
        if ball.colliderect(opponent):
            ball_speed_x *= -1
            prev_collision = 'opponent'

    ball.x += ball_speed_x
    ball.y += ball_speed_y

def paddle_animation():
    global player_speed
    global opponent_speed
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed = 5
            if event.key == pygame.K_UP:
                player_speed = -5
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed = 0
            if event.key == pygame.K_UP:
                player_speed = 0
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if opponent.top <= ball.y:
        opponent_speed = 5
    if opponent.bottom >= ball.y:
        opponent_speed = -5
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def draw_rects():
    pygame.draw.aaline(
    screen, L_GREY,
    (screen_width/ 2, 0),
    (screen_width/2, screen_height))
    # pygame.draw.rect(screen,)
    pygame.draw.rect(screen, GREEN, player, 0, 10)
    pygame.draw.rect(screen, RED, opponent, 0, 10)
    pygame.draw.ellipse(screen, BLUE + GREEN, ball)

def ball_reset():
    global ball_speed_y
    global ball_speed_x
    global prev_collision
    ball.center = (screen_width /2, screen_height /2)
    ball_speed_y *= choice((1, -1))
    ball_speed_x *= choice((1, -1))
    prev_collision = 'null'

def score(paddle):
    global player_score, opponent_score
    if paddle == 'player':
        player_score =+1
    if paddle == 'opponent':
        opponent_score =+1

pygame.display.set_caption("KING-PONG!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    x += 1
    if x >= 10:
            screen.fill(BLACK)
            x = 0
    ball_animation()
    paddle_animation()
    draw_rects()
    player.y += player_speed
    opponent.y += opponent_speed
    pygame.display.flip()
    clock.tick(60)


