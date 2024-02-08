import sys
from display import display
from hands import *
from button import *

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mos = pygame.mouse.get_pos()
                    if (WMARGIN + TILEWIDTH * 2 < mos[0] < WMARGIN + TILEWIDTH * 2 + TILEWIDTH * 10 and HEIGHT - HMARGIN - TILEHEIGHT * 4 < mos[1] < HEIGHT - HMARGIN - TILEHEIGHT) or \
                            (WMARGIN + TILEWIDTH * 2 < mos[0] < WMARGIN + TILEWIDTH * 2 + TILEWIDTH * 7 and HEIGHT - HMARGIN - TILEHEIGHT  < mos[1] < HEIGHT - HMARGIN):
                        x = (mos[0] - WMARGIN - TILEWIDTH * 2) // TILEWIDTH
                        y = (mos[1] - (HEIGHT - HMARGIN - TILEHEIGHT * 4)) // TILEHEIGHT
                        hand.addTile((x + y * 10))

                    if (WMARGIN < mos[0] < WMARGIN + TILEWIDTH * len(hand.hand) and HMARGIN < mos[1] < HMARGIN + TILEHEIGHT):
                        tile = (mos[0] - WMARGIN) // TILEWIDTH
                        hand.removeTile(tile)

                    if (WMARGIN + TILEWIDTH * 2 + TILEWIDTH * 7 < mos[0] < WMARGIN + TILEWIDTH * 2 + TILEWIDTH * 10 and HEIGHT - HMARGIN - TILEHEIGHT  < mos[1] < HEIGHT - HMARGIN):
                        if sortButton.getClicked(mos):
                            hand.sort()
                        if clearButton.getClicked(mos):
                            hand.clear()


        display()


main()