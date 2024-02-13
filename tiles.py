from settings import *
class Tiles():
    def __init__(self):
        self.tiles = []
        self.tileDict = {}
        self.createTiles()
        self.tileSelect = []

        self.tileBack = pygame.image.load("graphics/tiles/B0.png").convert()


    def createTiles(self):
        for suit in ["M","P","S"]:
            for number in range(1,10):
                tile = suit+str(number)
                image = pygame.image.load(f"graphics/tiles/{tile}.png").convert()
                self.tiles.append(tile)
                self.tileDict.update({tile:image})
            tile = "A" + suit + "5"
            image = pygame.image.load(f"graphics/tiles/{tile}.png").convert()
            self.tiles.append(tile)
            self.tileDict.update({tile: image})

        for number in range(1,8):
            tile = f"H{number}"
            image = pygame.image.load(f"graphics/tiles/{tile}.png").convert()
            self.tiles.append(tile)
            self.tileDict.update({tile:image})


    def displayTiles(self):
        for i in range(len(self.tiles)):
            pos = (WMARGIN + TILEWIDTH * (i % 10),HEIGHT - HMARGIN - TILEHEIGHT * 4 + TILEHEIGHT * (i // 10))
            screen.blit(self.tileDict.get(self.tiles[i]),pos)


    def display(self):
        self.displayTiles()


tiles = Tiles()


