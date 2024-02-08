from settings import *

class Button(pygame.sprite.Sprite):
    def __init__(self,text,pos):
        super().__init__()
        self.font = pygame.font.SysFont("BIZ UDPゴシック",TILEWIDTH // 2)
        self.image = pygame.image.load("graphics/tiles/B0.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.text = self.font.render(text, True, "#ecf0f1")
        self.textRect = self.text.get_rect(center = self.rect.center)

    def getClicked(self,mouse):
        if self.rect.collidepoint(mouse):
            return True

    def draw(self):
        screen.blit(self.image,self.rect)
        screen.blit(self.text,self.textRect)


buttonGroup = pygame.sprite.Group()

sortButton = Button("Sort",(WMARGIN + TILEWIDTH * 2 + TILEWIDTH * 7,HEIGHT - HMARGIN - TILEHEIGHT))
clearButton = Button("Clear",(WMARGIN + TILEWIDTH * 2 + TILEWIDTH * 8,HEIGHT - HMARGIN - TILEHEIGHT))
otherButton = Button("Other",(WMARGIN + TILEWIDTH * 2 + TILEWIDTH * 9,HEIGHT - HMARGIN - TILEHEIGHT))

buttons = [sortButton,clearButton,otherButton]

for button in buttons:
    buttonGroup.add(button)
