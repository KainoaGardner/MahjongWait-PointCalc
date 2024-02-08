from tiles import *

class Hand():
    def __init__(self):
        self.hand = []
        self.font = font

    def addTile(self,tile):
        if len(self.hand) < 14:
            tile = tiles.tiles[tile]
            if tile in ["AM5", "AP5", "AS5"] and self.hand.count(tile) < 1:
                self.hand.append(tile)
            elif tile not in ["AM5", "AP5", "AS5"] and self.hand.count(tile) < 4:
                self.hand.append(tile)

    def removeTile(self,tile):
        if len(self.hand) > 0:
            del self.hand[tile]

    def sort(self):
        tempHand = []
        suits = self.splitSuits()

        for suit in suits:
            if len(suit) > 0:
                suit = self.sortNumbers(suit)
                for tile in suit:
                    tempHand.append(tile)

        self.hand = tempHand


    def sortNumbers(self,suit):
        for _ in range(len(suit)):
            for i in range(len(suit) -1):
                if suit[i][-1] > suit[i + 1][-1]:
                    temp = suit[i]
                    suit[i] = suit[i + 1]
                    suit[i + 1] = temp
        return suit

    def splitSuits(self):
        manzu = []
        pinzu = []
        souzu = []
        honor = []
        for tile in self.hand:
            if tile not in ["AM5", "AP5", "AS5"]:
                match tile[0]:
                    case "M":
                        manzu.append(tile)
                    case "P":
                        pinzu.append(tile)
                    case "S":
                        souzu.append(tile)
                    case "H":
                        honor.append(tile)
            elif tile in ["AM5", "AP5", "AS5"]:
                match tile[1]:
                    case "M":
                        manzu.append(tile)
                    case "P":
                        pinzu.append(tile)
                    case "S":
                        souzu.append(tile)
        return [manzu,pinzu,souzu,honor]

    def clear(self):
        self.hand.clear()

    def displayTileNumber(self):
        for i in range(len(self.hand)):
            tileNumber = self.font.render(str(i + 1),True,"#ecf0f1")
            tileNumberRect = tileNumber.get_rect(center = (WMARGIN + TILEWIDTH // 2 + TILEWIDTH * i,TILEHEIGHT // 2))
            screen.blit(tileNumber,tileNumberRect)

    def displayHand(self):
        for i in range(len(self.hand)):
            pos = (WMARGIN + TILEWIDTH * i,HMARGIN)
            screen.blit(tiles.tileDict.get(self.hand[i]),pos)

    def display(self):
        self.displayHand()
        self.displayTileNumber()

hand = Hand()