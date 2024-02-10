from settings import *

class Button(pygame.sprite.Sprite):
    def __init__(self,text,pos):
        super().__init__()
        self.font = pygame.font.Font("font/BIZUDPGothic-Regular.ttf",TILEWIDTH // 2)
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

sortButton = Button("理",(WMARGIN  + TILEWIDTH * 7,HEIGHT - HMARGIN - TILEHEIGHT))
clearButton = Button("消",(WMARGIN  + TILEWIDTH * 8,HEIGHT - HMARGIN - TILEHEIGHT))
doraButton = Button("ドラ",(WMARGIN  + TILEWIDTH * 9,HEIGHT - HMARGIN - TILEHEIGHT))

buttons = [sortButton,clearButton,doraButton]

chiButton = Button("チー",(WMARGIN  + TILEWIDTH * 10,HEIGHT - HMARGIN - TILEHEIGHT * 4))
ponButton = Button("ポン",(WMARGIN  + TILEWIDTH * 10,HEIGHT - HMARGIN - TILEHEIGHT * 3))
kanButton = Button("カン",(WMARGIN + TILEWIDTH * 10,HEIGHT - HMARGIN - TILEHEIGHT * 2))
ankanButton = Button("暗槓",(WMARGIN  + TILEWIDTH * 10,HEIGHT - HMARGIN - TILEHEIGHT * 1))

callButtons = [chiButton,ponButton,kanButton,ankanButton]

for button in buttons:
    buttonGroup.add(button)

for button in callButtons:
    callButtonGroup.add(button)
