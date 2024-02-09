from tiles import *

class Hand():
    def __init__(self):
        self.hand = []
        self.font = font
        self.akaDict = {"AM5":"M5", "AP5":"P5", "AS5":"S5"}
        self.validHand = False
        self.tenpai = False

    def addTile(self,tile):
        if len(self.hand) < 14:
            tile = tiles.tiles[tile]
            if tile in ["AM5", "AP5", "AS5"] and self.hand.count(tile) < 1:
                self.hand.append(tile)
                if len(self.hand) == 14:
                    self.checkWin(self.hand)
            elif tile not in ["AM5", "AP5", "AS5"] and self.hand.count(tile) < 4:
                self.hand.append(tile)
                if len(self.hand) == 14:
                    self.checkWin(self.hand)


    def removeTile(self,tile):
        if len(self.hand) > 0:
            del self.hand[tile]
            self.validHand = False

    def sort(self):
        tempHand = []
        if len(self.hand) == 14:
            suits = self.splitSuits(self.hand[:-1])
        else:
            suits = self.splitSuits(self.hand)

        for suit in suits:
            if len(suit) > 0:
                suit = self.sortNumbers(suit)
                for tile in suit:
                    tempHand.append(tile)

        if len(self.hand) == 14:
            tempHand.append(self.hand[-1])

        self.hand = tempHand

    def sortNumbers(self,suit):
        for _ in range(len(suit)):
            for i in range(len(suit) -1):
                if suit[i][-1] > suit[i + 1][-1]:
                    temp = suit[i]
                    suit[i] = suit[i + 1]
                    suit[i + 1] = temp
        return suit

    def splitSuits(self,list):
        manzu = []
        pinzu = []
        souzu = []
        honor = []
        for tile in list:
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

    def getHead(self,list):
        potentialHeads = []
        for tile in list:
            if list.count(tile) >= 2 and tile not in potentialHeads:
                potentialHeads.append(tile)

        return potentialHeads

    def getmentsu(self,list):
        suits = self.splitSuits(list)
        possibleShapes = []
        for suit in suits:
            possibleSuitShape = []
            confirmedSuitShapes = []
            if len(suit) == 0:
                continue
            if len(suit) % 3 != 0:
                break

            shuntsu = []
            koutsu = []

            if suit[0][0] != "H":
                shuntsu = self.getshuntsu(suit)

            koutsu = self.getkoutsu(suit)
            for shape in shuntsu:
                possibleSuitShape.append(shape)

            for shape in koutsu:
                possibleSuitShape.append(shape)

            for i in range(len(possibleSuitShape)):
                tempSuit = suit.copy()
                confirmedShapes = []
                confirmedShapes.append(possibleSuitShape[i])
                for tile in possibleSuitShape[i]:
                    tempSuit.remove(tile)
                if len(tempSuit) > 0:
                    for j in range(len(possibleSuitShape)):
                        if i != j and len(tempSuit) > 0:
                            if (tempSuit.count(possibleSuitShape[j][0]) == 1 and tempSuit.count(possibleSuitShape[j][1]) == 1 and tempSuit.count(possibleSuitShape[j][2]) == 1) or (tempSuit.count(possibleSuitShape[j][0]) == 3 and tempSuit.count(possibleSuitShape[j][1]) == 3 and tempSuit.count(possibleSuitShape[j][2]) == 3):
                                confirmedShapes.append(possibleSuitShape[j])
                                for tile in possibleSuitShape[j]:
                                    tempSuit.remove(tile)

                if len(tempSuit) == 0:
                    for shape in confirmedShapes:
                        if shape not in confirmedSuitShapes:
                            confirmedSuitShapes.append(shape)

                for shape in confirmedSuitShapes:
                    possibleShapes.append(shape)

            if len(possibleShapes) >= 4:
                return True

    def getshuntsu(self,suit):
        shapes = []
        tempSuit = suit.copy()
        for i in range(len(tempSuit) - 2):
            if tempSuit.count(tempSuit[i][0] + str(int(tempSuit[i][-1]) + 1)) > 0 and tempSuit.count(tempSuit[i][0] + str(int(tempSuit[i][-1]) + 2)) > 0:
                shapes.append((tempSuit[i],tempSuit[i][0] + str(int(tempSuit[i][-1]) + 1),tempSuit[i][0] + str(int(tempSuit[i][-1]) + 2)))
        return shapes

    def getkoutsu(self,suit):
        shapes = []
        for tile in suit:
            if suit.count(tile) >= 3 and tile not in shapes:
                shapes.append(tile)

        if len(shapes) > 0:
            for i in range(len(shapes)):
                shapes[i] = (shapes[i],shapes[i],shapes[i])

        return shapes

    def checkWin(self,list):
        tempList = []
        possibleWins = []
        for i in range(len(list)):
            if list[i] in ["AM5", "AP5", "AS5"]:
                list[i] = self.akaDict.get(list[i])
            tempList.append(list[i])

        if len(tempList) == 14:
            potentialHeads = self.getHead(tempList)
            if len(potentialHeads) > 0:
                for head in potentialHeads:
                    tempList = self.hand.copy()
                    tempList.remove(head)
                    tempList.remove(head)
                    if self.getmentsu(tempList):
                        possibleWins.append(tempList)

        if len(possibleWins) > 0:
            self.validHand = True
            print("2")
        else:
            self.validHand = False

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
        print(self.validHand)

hand = Hand()