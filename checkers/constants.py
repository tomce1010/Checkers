import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BROWN = (78, 53, 36)

CROWN = pygame.transform.scale(pygame.image.load('crown.png'), (45, 25))
WINNER = pygame.transform.scale(pygame.image.load('winner.png'), (500, 250))
#WINNER = pygame.image.load("winner.png").convert()
