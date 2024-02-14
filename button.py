from settings import *

class Button(pygame.sprite.Sprite):
    def __init__(self,text,pos):
        super().__init__()
        self.font = pygame.font.Font("font/BIZUDPGothic-Regular.ttf",TILEWIDTH // 3)
        self.image = pygame.image.load("graphics/tiles/B0.png").convert()
        self.rect = self.image.get_rect(topleft = pos)
        self.text = self.font.render(text, True, white)
        self.textRect = self.text.get_rect(center = self.rect.center)

    def getClicked(self,mouse):
        if self.rect.collidepoint(mouse):
            return True

    def draw(self):
        screen.blit(self.image,self.rect)
        screen.blit(self.text,self.textRect)


buttonGroup = pygame.sprite.Group()
callButtonGroup = pygame.sprite.Group()

sortButton = Button("理",(WMARGIN  + TILEWIDTH * 7,HEIGHT - HMARGIN - TILEHEIGHT * 2))
clearButton = Button("消",(WMARGIN  + TILEWIDTH * 8,HEIGHT - HMARGIN - TILEHEIGHT * 2))
doraButton = Button("ドラ",(WMARGIN  + TILEWIDTH * 9,HEIGHT - HMARGIN - TILEHEIGHT * 2))

buttons = [sortButton,clearButton,doraButton]

chiButton = Button("チー",(WMARGIN + TILEWIDTH * 10,HEIGHT - HMARGIN - TILEHEIGHT * 5))
ponButton = Button("ポン",(WMARGIN + TILEWIDTH * 10,HEIGHT - HMARGIN - TILEHEIGHT * 4))
kanButton = Button("カン",(WMARGIN + TILEWIDTH * 10,HEIGHT - HMARGIN - TILEHEIGHT * 3))
ankanButton = Button("暗槓",(WMARGIN + TILEWIDTH * 10,HEIGHT - HMARGIN - TILEHEIGHT * 2))

callButtons = [chiButton,ponButton,kanButton,ankanButton]

ronButton = Button("ロン",(WMARGIN + TILEWIDTH,HEIGHT - HMARGIN - TILEHEIGHT))
tumoButton = Button("ツモ",(WMARGIN + TILEWIDTH,HEIGHT - HMARGIN - TILEHEIGHT))

richiButton = Button("リーチ",(WMARGIN + TILEWIDTH * 2,HEIGHT - HMARGIN - TILEHEIGHT))
wRichiButton = Button("wリーチ",(WMARGIN + TILEWIDTH * 2,HEIGHT - HMARGIN - TILEHEIGHT))

iipatsuButton = Button("一発",(WMARGIN + TILEWIDTH * 3,HEIGHT - HMARGIN - TILEHEIGHT))

haiteiButton = Button("ハイテイ",(WMARGIN + TILEWIDTH * 4,HEIGHT - HMARGIN - TILEHEIGHT))

rinshanButton = Button("嶺上開花",(WMARGIN + TILEWIDTH * 5,HEIGHT - HMARGIN - TILEHEIGHT))

chankanButton = Button("槍槓",(WMARGIN + TILEWIDTH * 6,HEIGHT - HMARGIN - TILEHEIGHT))

tenHouButton = Button("天和",(WMARGIN + TILEWIDTH * 7,HEIGHT - HMARGIN - TILEHEIGHT))


# pointButton = [ronButton,tumoButton,richiButton,wRichiButton,iipatsuButton,haiteiButton,rinshanButton,chankanButton,tenHouButton]

for button in buttons:
    buttonGroup.add(button)

for button in callButtons:
    callButtonGroup.add(button)
