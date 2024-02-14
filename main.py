import sys
from display import display
from hands import *
from button import *
from score import *

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mos = pygame.mouse.get_pos()
                    if (WMARGIN < mos[0] < WMARGIN  + TILEWIDTH * 10 and HEIGHT - HMARGIN - TILEHEIGHT * 5 < mos[1] < HEIGHT - HMARGIN - TILEHEIGHT * 2) or \
                            (WMARGIN  < mos[0] < WMARGIN  + TILEWIDTH * 7 and HEIGHT - HMARGIN - TILEHEIGHT * 2 < mos[1] < HEIGHT - HMARGIN - TILEHEIGHT):
                        x = (mos[0] - WMARGIN) // TILEWIDTH
                        y = (mos[1] - (HEIGHT - HMARGIN - TILEHEIGHT * 5)) // TILEHEIGHT
                        if hand.doraSelect:
                            if hand.hand.count(tiles.tiles[(x + y * 10)]) < 4:
                                hand.dora = tiles.tiles[(x + y * 10)]
                        else:
                            hand.addTile((x + y * 10))

                        hand.callType = ""
                        hand.doraSelect = False
                        hand.buttonShader = 0

                    elif (WMARGIN < mos[0] < WMARGIN + TILEWIDTH * ((len(hand.hand) + len(hand.handCalls)) + len(hand.handCallsKan) + len(hand.handCallsAnkan)) and HMARGIN < mos[1] < HMARGIN + TILEHEIGHT):
                        tile = (mos[0] - WMARGIN) // TILEWIDTH
                        print(tile)
                        if hand.callType == "chi":
                            hand.getChi(tile)
                        elif hand.callType == "pon":
                            hand.getPon(tile)
                        elif hand.callType == "kan":
                            hand.getKan(tile)
                        elif hand.callType == "ankan":
                            hand.getAnkan(tile)
                        else:
                            hand.removeTile(tile)

                        hand.callType = ""
                        hand.doraSelect = False
                        hand.buttonShader = 0

                    elif (WIDTH - WMARGIN - TILEWIDTH < mos[0] < WIDTH - WMARGIN  and HMARGIN < mos[1] < HMARGIN + TILEHEIGHT):
                        if hand.dora != "":
                            hand.dora = ""
                            hand.buttonShader = 0

                    elif (WMARGIN  + TILEWIDTH * 7 < mos[0] < WMARGIN + TILEWIDTH * 10 and HEIGHT - HMARGIN - TILEHEIGHT * 3  < mos[1] < HEIGHT - HMARGIN - TILEHEIGHT):
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
                            if hand.buttonShader == 7:
                                hand.buttonShader = 0
                            else:
                                hand.buttonShader = 7
                        hand.callType = ""

                    elif WMARGIN + TILEWIDTH < mos[0] < WMARGIN + TILEWIDTH * 8 and HEIGHT - HMARGIN - TILEHEIGHT < mos[1] < HEIGHT - HMARGIN:
                        print("2")
                        if ronButton.getClicked(mos) and score.winType == "ron":
                            score.winType = "tumo"
                        elif tumoButton.getClicked(mos) and score.winType == "tumo":
                            score.winType = "ron"

                        if len(hand.handCalls) + (len(hand.handCallsKan)) == 0:
                            if richiButton.getClicked(mos) and score.richiType == "":
                                score.richiType = "richi"
                            elif richiButton.getClicked(mos) and score.richiType == "richi":
                                score.richiType = "wrichi"
                            elif wRichiButton.getClicked(mos):
                                score.richiType = ""
                                score.iipatsuType = False
                        else:
                            score.richiType = ""

                        if score.richiType == "richi" or score.richiType == "wrichi":
                            if iipatsuButton.getClicked(mos) and score.iipatsuType == False:
                                score.iipatsuType = True
                            elif iipatsuButton.getClicked(mos) and score.iipatsuType:
                                score.iipatsuType = False

                        if haiteiButton.getClicked(mos) and score.haitei == False:
                            score.haitei = True
                        elif haiteiButton.getClicked(mos) and score.haitei == True:
                            score.haitei = False

                        if len(hand.handCallsKan) + len(hand.handCallsAnkan) > 0:
                            if rinshanButton.getClicked(mos) and score.rinshan == False:
                                score.rinshan = True
                            elif rinshanButton.getClicked(mos) and score.rinshan == True:
                                score.rinshan = False
                        else:
                            score.rinshan = False

                        if chankanButton.getClicked(mos):
                            print(hand.confirmedWins)
                            print(hand.winTiles)
                            score.chankan = not score.chankan

                        if len(hand.handCallsKan) + len(hand.handCallsAnkan) + len(hand.handCalls) == 0:
                            if tenHouButton.getClicked(mos):
                                score.tenhou = not score.tenhou

                    elif WMARGIN + TILEWIDTH * 8 < mos[0] < WMARGIN + TILEWIDTH * 9 and HEIGHT - HMARGIN - TILEHEIGHT < mos[1] < HEIGHT - HMARGIN:
                        if hand.bakazeIndex < 3:
                            hand.bakazeIndex += 1
                        else:
                            hand.bakazeIndex = 0

                    elif WMARGIN + TILEWIDTH * 9 < mos[0] < WMARGIN + TILEWIDTH * 10 and HEIGHT - HMARGIN - TILEHEIGHT < mos[1] < HEIGHT - HMARGIN:
                        if hand.jikazeIndex < 3:
                            hand.jikazeIndex += 1
                        else:
                            hand.jikazeIndex = 0

                    elif (WMARGIN  + TILEWIDTH * 10 < mos[0] < WMARGIN  + TILEWIDTH * 11 and HEIGHT - HMARGIN - TILEHEIGHT * 5 < mos[1] < HEIGHT - HMARGIN - TILEHEIGHT):
                        if chiButton.getClicked(mos):
                            hand.callType = "chi"
                            if hand.buttonShader == 4:
                                hand.callType = ""
                                hand.buttonShader = 0
                            else:
                                hand.buttonShader = 4

                        elif ponButton.getClicked(mos):
                            hand.callType = "pon"
                            if hand.buttonShader == 3:
                                hand.callType = ""
                                hand.buttonShader = 0
                            else:
                                hand.buttonShader = 3
                        elif kanButton.getClicked(mos):
                            hand.callType = "kan"
                            if hand.buttonShader == 2:
                                hand.callType = ""
                                hand.buttonShader = 0
                            else:
                                hand.buttonShader = 2
                        elif ankanButton.getClicked(mos):
                            hand.callType = "ankan"
                            if hand.buttonShader == 1:
                                hand.callType = ""
                                hand.buttonShader = 0
                            else:
                                hand.buttonShader = 1

                        hand.doraSelect = False

                    else:
                        hand.callType = ""
                        hand.doraSelect = False
                        hand.buttonShader = 0


        display()


main()