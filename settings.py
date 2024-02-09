import pygame

pygame.init()

TILEWIDTH = 66
TILEHEIGHT = 90
WMARGIN = TILEWIDTH
HMARGIN = TILEHEIGHT
FPS = 60

WIDTH = TILEWIDTH * 16 + WMARGIN * 2
HEIGHT = TILEHEIGHT * 8 + HMARGIN * 2

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font("font/BIZUDPGothic-Regular.ttf",TILEWIDTH//2)

white = "#ffffff"