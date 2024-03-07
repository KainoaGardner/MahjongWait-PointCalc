from button import *
from tiles import *
from yaku import getYakuList

class Score():
    def __init__(self):
        self.shader = pygame.Surface((TILEWIDTH, TILEHEIGHT))
        self.shader.fill("#4b4b4b")
        self.shader.set_alpha(100)

        self.ronButton = ronButton
        self.tumoButton = tumoButton
        self.winType = "ron"
        self.richiButton = richiButton
        self.wRichiButton = wRichiButton
        self.richiType = ""
        self.iipatsuButton = iipatsuButton
        self.iipatsuType = False
        self.haitei = False
        self.haiteiButton = haiteiButton
        self.rinshan = False
        self.rinshanButton = rinshanButton
        self.chankanButton = chankanButton
        self.chankan = False
        self.tenhouButton = tenHouButton
        self.tenhou = False

        self.yaku = []
        self.yakuText = []
        self.fu = 0
        self.han = 0
        self.score = 0

    def displayButtons(self):
        if self.winType == "ron":
            self.ronButton.draw()
        else:
            self.tumoButton.draw()

        if self.richiType == "richi":
            self.richiButton.draw()
        elif self.richiType == "wrichi":
            self.wRichiButton.draw()
        else:
            self.richiButton.draw()
            screen.blit(self.shader,(WMARGIN + TILEWIDTH * 2,HEIGHT - HMARGIN - TILEHEIGHT))

        if self.iipatsuType:
            self.iipatsuButton.draw()
        else:
            self.iipatsuButton.draw()
            screen.blit(self.shader,(WMARGIN + TILEWIDTH * 3,HEIGHT - HMARGIN - TILEHEIGHT))

        if self.haitei:
            self.haiteiButton.draw()
        else:
            self.haiteiButton.draw()
            screen.blit(self.shader,(WMARGIN + TILEWIDTH * 4,HEIGHT - HMARGIN - TILEHEIGHT))

        if self.rinshan:
            self.rinshanButton.draw()
        else:
            self.rinshanButton.draw()
            screen.blit(self.shader, (WMARGIN + TILEWIDTH * 5,HEIGHT - HMARGIN - TILEHEIGHT))

        if self.chankan:
            self.chankanButton.draw()
        else:
            self.chankanButton.draw()
            screen.blit(self.shader, (WMARGIN + TILEWIDTH * 6,HEIGHT - HMARGIN - TILEHEIGHT))

        if self.tenhou:
            self.tenhouButton.draw()
        else:
            self.tenhouButton.draw()
            screen.blit(self.shader, (WMARGIN + TILEWIDTH * 7,HEIGHT - HMARGIN - TILEHEIGHT))

    def getWinYakuText(self,hand,winTiles):

        yakuList,han = getYakuList(hand,winTiles)
        if yakuList[0][0] in ["大三元","四暗刻","四暗刻単騎",'清老頭',"四槓子","国士無双十三面待ち","国士無双","純正九蓮宝燈","九蓮宝燈","小四喜","大四喜","字一色","緑一色"]:
            pass
        else:
            self.han = han
            for i,yaku in enumerate(yakuList):
                text = font.render(yaku[0],True,white)
                textRect = text.get_rect(center=(WMARGIN + TILEWIDTH * 12 + TILEWIDTH * (i // 6 * 3), HEIGHT - HMARGIN - TILEHEIGHT * 4 + TILEHEIGHT * (i % 6) - TILEHEIGHT // 2))

    def display(self):
        self.displayButtons()



score = Score()


