import pygame, sys


pygame.init()
# starts the pygame modules (required for pygame to run)

clock = pygame.time.Clock()
# var clock

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("PONG!")

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()