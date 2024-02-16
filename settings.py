import pygame

pygame.init()

TILEWIDTH = 66
TILEHEIGHT = 90
WMARGIN = TILEWIDTH
HMARGIN = TILEHEIGHT
FPS = 60

WIDTH = TILEWIDTH * 20 + WMARGIN * 2
HEIGHT = TILEHEIGHT * 9 + HMARGIN * 2

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font("font/BIZUDPGothic-Regular.ttf",TILEWIDTH//3)
bigFont = pygame.font.Font("font/BIZUDPGothic-Regular.ttf",TILEWIDTH//2)

white = "#ffffff"

text = bigFont.render("大三元", True, white)
textRect = text.get_rect(center=(WMARGIN + TILEWIDTH * 12, HEIGHT - HMARGIN - TILEHEIGHT * 4 - TILEHEIGHT // 2))