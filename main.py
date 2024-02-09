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
                        if hand.doraSelect:
                            hand.dora = tiles.tiles[(x + y * 10)]
                        else:
                            hand.addTile((x + y * 10))

                        hand.callType = ""
                        hand.doraSelect = False
                        hand.buttonShader = 0

                    elif (WMARGIN < mos[0] < WMARGIN + TILEWIDTH * len(hand.hand) and HMARGIN < mos[1] < HMARGIN + TILEHEIGHT):
                        tile = (mos[0] - WMARGIN) // TILEWIDTH
                        hand.removeTile(tile)
                        hand.callType = ""
                        hand.doraSelect = False
                        hand.buttonShader = 0

                    elif (WMARGIN + TILEWIDTH * 15 < mos[0] < WMARGIN + TILEWIDTH * 16 and HMARGIN < mos[1] < HMARGIN + TILEHEIGHT):
                        if hand.dora != "":
                            hand.dora = ""
                            hand.buttonShader = 0

                    elif (WMARGIN + TILEWIDTH * 2 + TILEWIDTH * 7 < mos[0] < WMARGIN + TILEWIDTH * 2 + TILEWIDTH * 10 and HEIGHT - HMARGIN - TILEHEIGHT  < mos[1] < HEIGHT - HMARGIN):
                        if sortButton.getClicked(mos):
                            hand.sort()
                            hand.doraSelect = False
                            hand.buttonShader = 0
                        elif clearButton.getClicked(mos):
                            hand.clear()
                            hand.doraSelect = False
                            hand.buttonShader = 0
                        elif doraButton.getClicked(mos):
                            hand.doraSelect = not hand.doraSelect
                            hand.buttonShader = 7
                        hand.callType = ""


                    elif (WMARGIN + TILEWIDTH * 2 + TILEWIDTH * 10 < mos[0] < WMARGIN + TILEWIDTH * 2 + TILEWIDTH * 11 and HEIGHT - HMARGIN - TILEHEIGHT * 4 < mos[1] < HEIGHT - HMARGIN):
                        if chiButton.getClicked(mos):
                            hand.callType = "chi"
                            hand.buttonShader = 4
                        elif ponButton.getClicked(mos):
                            hand.callType = "pon"
                            hand.buttonShader = 3
                        elif kanButton.getClicked(mos):
                            hand.callType = "kan"
                            hand.buttonShader = 2
                        elif ankanButton.getClicked(mos):
                            hand.callType = "ankan"
                            hand.buttonShader = 1

                        hand.doraSelect = False

                    else:
                        hand.callType = ""
                        hand.doraSelect = False
                        hand.buttonShader = 0


        display()


main()