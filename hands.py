from tiles import *
from score import *
class Hand():
    def __init__(self):
        self.hand = []
        self.handCalls = []
        self.handCallsKan = []
        self.handCallsAnkan = []

        self.font = font
        self.akaDict = {"AM5":"M5", "AP5":"P5", "AS5":"S5"}
        self.validHand = False
        self.winTiles = []
        self.point = 0

        self.machitext = self.font.render("待ち",True,white)
        self.machiRect = self.machitext.get_rect(midleft=(WMARGIN, HMARGIN + TILEHEIGHT + TILEHEIGHT // 2))

        self.callType = ""
        self.shader = pygame.Surface((TILEWIDTH,TILEHEIGHT))
        self.shader.fill("#4b4b4b")
        self.shader.set_alpha(100)
        self.callIndex = []
        self.kanCount = 0
        self.buttonShader = 0

        self.dora = ""
        self.doraSelect = False
        self.doraText = self.font.render("ドラ", True, white)
        self.doraTextRect = self.machitext.get_rect(center=(WIDTH - WMARGIN - TILEWIDTH + TILEWIDTH // 2,TILEHEIGHT // 2))

        self.agari = False
        self.agariText = self.font.render("和了", True, white)
        self.agariTextRect = self.machitext.get_rect(center=(WIDTH // 2,HMARGIN + TILEHEIGHT + TILEHEIGHT // 2))

        self.bakaze = ["H1","H2","H3","H4"]
        self.bakazeIndex = 0
        self.jikaze = ["H1","H2","H3","H4"]
        self.jikazeIndex = 0

        self.bakazeText = self.font.render("場風",True,white)
        self.bakazeRect = self.bakazeText.get_rect(center = (WMARGIN + TILEWIDTH * 8 + TILEWIDTH // 2,HEIGHT - HMARGIN+ TILEWIDTH // 2))

        self.jikazeText = self.font.render("自風",True,white)
        self.jikazeRect = self.jikazeText.get_rect(center = (WMARGIN + TILEWIDTH * 9 + TILEWIDTH // 2,HEIGHT - HMARGIN + TILEWIDTH // 2))

        self.confirmedWins = []


    def addTile(self,tile):
        if len(self.hand) + len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount < 14:
            tile = tiles.tiles[tile]
            if (tile not in ["AM5", "AP5", "AS5"] and (self.hand.count(tile) + self.handCalls.count(tile) + self.handCallsKan.count(tile) + self.handCallsAnkan.count(tile)) < 4) or (tile in ["AM5", "AP5", "AS5"] and (self.hand.count(tile) + self.handCalls.count(tile) + self.handCallsKan.count(tile) + self.handCallsAnkan.count(tile)) < 1):
                self.hand.append(tile)
                if len(self.hand) + len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount == 14:
                    if self.checkWin(self.hand):
                        self.agari = True
                    self.tenpai = False
                if len(self.hand) + len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount == 13:
                    self.checkTenpai()
                    self.agari = False
                print(("len", len(self.hand) + len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount))


    def removeTile(self,tile):
        if len(self.hand) + len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount > 0:
            if len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) > 0:
                if tile >= len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan):
                    del self.hand[tile - len(self.handCalls) - len(self.handCallsKan) - len(self.handCallsAnkan)]
                elif tile >= len(self.handCalls) + len(self.handCallsKan):
                    if (tile - len(self.handCalls) + len(self.handCallsKan)) % 4 == 0:
                        for _ in range(4):
                            del self.handCallsAnkan[0]
                        self.kanCount -= 1
                        score.rinshan = False


                elif tile >= len(self.handCalls):
                    clickedTile = self.handCallsKan[tile]
                    if clickedTile in ["AM5", "AP5", "AS5"]:
                        clickedTile = self.akaDict.get(clickedTile)

                    if self.handCallsKan.count(self.handCallsKan[tile]) == 4 and tile < len(self.handCallsKan) + len(self.handCalls) - 3:
                        print(tile)
                        if self.handCallsKan[tile + 1 - len(self.handCalls)] == clickedTile and self.handCallsKan[tile + 2 - len(self.handCalls)] == clickedTile and self.handCallsKan[tile + 3 - len(self.handCalls)] == clickedTile:
                            for _ in range(4):
                                del self.handCallsKan[tile - len(self.handCalls)]
                            self.kanCount -= 1
                            score.rinshan = False

                else:
                    clickedTile = self.handCalls[tile]
                    if clickedTile in ["AM5", "AP5", "AS5"]:
                        clickedTile = self.akaDict.get(clickedTile)

                    if tile < len(self.handCalls) - 2 and self.handCalls[tile + 1] == clickedTile[0] + str(int(clickedTile[1]) + 1) and self.handCalls[tile + 2] == clickedTile[0] + str(int(clickedTile[1]) + 2) and clickedTile[0] != "H":
                        for _ in range(3):
                            del self.handCalls[tile]
                    elif self.handCalls.count(self.handCalls[tile]) == 3 and tile < len(self.handCalls) - 2:
                        if self.handCalls[tile + 1] == clickedTile and self.handCalls[tile + 2] == clickedTile:
                            for _ in range(3):
                                del self.handCalls[tile]

                if len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount + len(
                        self.hand) == 13:
                    self.checkTenpai()
                elif len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount + len(
                        self.hand) == 14:
                    self.checkWin(self.hand)

            else:
                del self.hand[tile]

            self.validHand = False
            if len(self.hand) + len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount == 13:
                self.winTiles.clear()
                self.checkTenpai()
            else:
                self.tenpai = False
                self.winTiles.clear()

    def sort(self):
        tempHand = []
        if len(self.hand) + len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount == 14:
            suits = self.splitSuits(self.hand[:-1])
        else:
            suits = self.splitSuits(self.hand)

        for suit in suits:
            if len(suit) > 0:
                suit = self.sortNumbers(suit)
                for tile in suit:
                    tempHand.append(tile)

        if len(self.hand) + len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount == 14:
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
        self.handCalls.clear()

    def getHead(self,list):
        potentialHeads = []
        for tile in list:
            if list.count(tile) >= 2 and tile not in potentialHeads:
                potentialHeads.append(tile)

        return potentialHeads

    def getmentsu(self,list,head):
        head = head
        confirmedShapes = []
        list.remove(head)
        list.remove(head)
        possibleShapes = []

        koutsu = self.getkoutsu(list)
        for shape in koutsu:
            possibleShapes.append(shape)

        shuntsu = self.getshuntsu(list)
        for shape in shuntsu:
            possibleShapes.append(shape)

        if len(possibleShapes) >= 4 - (len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount) // 3:
            for i in range(len(possibleShapes)):
                tempList = list.copy()
                shapes = []
                shapes.append(possibleShapes[i])
                for tile in possibleShapes[i]:
                    tempList.remove(tile)
                for j in range(len(possibleShapes)):
                    if i != j:
                        if (possibleShapes[j].count(possibleShapes[j][0]) == 3 and tempList.count(possibleShapes[j][0]) >= 3) or (possibleShapes[j].count(possibleShapes[j][0]) == 1 and possibleShapes[j][0] in tempList and possibleShapes[j][1] in tempList and possibleShapes[j][2] in tempList):
                            shapes.append(possibleShapes[j])
                            for tile in possibleShapes[j]:
                                tempList.remove(tile)
                if len(tempList) == 0:
                    if len(confirmedShapes) > 0:
                        for confirmedShape in confirmedShapes:
                            for shape in shapes:
                                if shape not in confirmedShape:
                                    confirmedShapes.append(shapes)
                                    break
                    else:
                        confirmedShapes.append(shapes)

        return confirmedShapes

    def getshuntsu(self,list):
        shapes = []
        tempSuit = list.copy()
        for i in range(len(tempSuit)):
            if tempSuit[i][0] != "H":
                if tempSuit.count(tempSuit[i][0] + str(int(tempSuit[i][-1]) + 1)) > 0 and tempSuit.count(tempSuit[i][0] + str(int(tempSuit[i][-1]) + 2)) > 0:
                    shapes.append((tempSuit[i],tempSuit[i][0] + str(int(tempSuit[i][-1]) + 1),tempSuit[i][0] + str(int(tempSuit[i][-1]) + 2)))
        return shapes

    def getkoutsu(self,list):
        shapes = []
        for tile in list:
            if list.count(tile) >= 3 and tile not in shapes:
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
                tempList.append(self.akaDict.get(list[i]))
            else:
                tempList.append(list[i])

        potentialHeads = self.getHead(tempList)
        if len(potentialHeads) > 0:
                for head in potentialHeads:
                    temp = tempList.copy()
                    win = self.getmentsu(temp,head)
                    if len(win) > 0:
                        for hand in win:
                            if hand not in possibleWins:
                                count = 0
                                if len(possibleWins) > 0:
                                    for winHand in possibleWins:
                                        for shape in hand:
                                            if shape in winHand:
                                                count += 1
                                    if count < 4:
                                        if len(self.handCalls) > 0:
                                            for i in range((len(self.handCalls))//3):
                                                hand.append((self.handCalls[i * 3],self.handCalls[i * 3 + 1],self.handCalls[i * 3 + 2]))
                                        if len(self.handCallsKan) > 0:
                                            if self.kanCount > 0:
                                                for i in range((len(self.handCallsKan))//4):
                                                    hand.append((self.handCallsKan[i * 4], self.handCallsKan[i * 4 + 1],
                                                                 self.handCallsKan[i * 4 + 2], self.handCallsKan[i * 4 + 3]))
                                        if len(self.handCallsAnkan) > 0:
                                            if self.kanCount > 0:
                                                for i in range((len(self.handCallsAnkan))//4):
                                                    hand.append((self.handCallsAnkan[i * 4], self.handCallsAnkan[i * 4 + 1],
                                                                 self.handCallsAnkan[i * 4 + 2], self.handCallsAnkan[i * 4 + 3]))
                                        hand.append((head, head))

                                        possibleWins.append(hand)

                                else:
                                    if len(self.handCalls) > 0:
                                        for i in range((len(self.handCalls)) // 3):
                                            hand.append((self.handCalls[i * 3], self.handCalls[i * 3 + 1],
                                                         self.handCalls[i * 3 + 2]))
                                    if len(self.handCallsKan) > 0:
                                        if self.kanCount > 0:
                                            for i in range((len(self.handCallsKan)) // 4):
                                                hand.append((self.handCallsKan[i * 4], self.handCallsKan[i * 4 + 1],
                                                             self.handCallsKan[i * 4 + 2],
                                                             self.handCallsKan[i * 4 + 3]))
                                    if len(self.handCallsAnkan) > 0:
                                        if self.kanCount > 0:
                                            for i in range((len(self.handCallsAnkan)) // 4):
                                                hand.append((self.handCallsAnkan[i * 4], self.handCallsAnkan[i * 4 + 1],
                                                             self.handCallsAnkan[i * 4 + 2],
                                                             self.handCallsAnkan[i * 4 + 3]))

                                    hand.append((head, head))
                                    possibleWins.append(hand)

                    elif len(win) == 0:
                        temp.append(head)
                        temp.append(head)
                        if len(temp) == 2:
                            hand = []
                            if len(self.handCalls) > 0:
                                for i in range((len(self.handCalls)) // 3):
                                    hand.append((self.handCalls[i * 3], self.handCalls[i * 3 + 1],
                                                 self.handCalls[i * 3 + 2]))
                            if len(self.handCallsKan) > 0:
                                if self.kanCount > 0:
                                    for i in range((len(self.handCallsKan)) // 4):
                                        hand.append((self.handCallsKan[i * 4], self.handCallsKan[i * 4 + 1],
                                                     self.handCallsKan[i * 4 + 2],
                                                     self.handCallsKan[i * 4 + 3]))
                            if len(self.handCallsAnkan) > 0:
                                if self.kanCount > 0:
                                    for i in range((len(self.handCallsAnkan)) // 4):
                                        hand.append((self.handCallsAnkan[i * 4], self.handCallsAnkan[i * 4 + 1],
                                                     self.handCallsAnkan[i * 4 + 2],
                                                     self.handCallsAnkan[i * 4 + 3]))
                            hand.append((head, head))
                            possibleWins.append(hand)


        if len(possibleWins) > 0:
            print("True")
            self.confirmedWins.clear()
            self.confirmedWins.append(possibleWins[0])
            return True
        else:
            return False

    def checkTenpai(self):
        for tile in tiles.tiles:
            if tile not in ["AM5", "AP5", "AS5"] and (self.hand.count(tile) + self.handCalls.count(tile) + self.handCallsKan.count(tile) + self.handCallsAnkan.count(tile)) < 4:
                temp = self.hand.copy()
                temp.append(tile)
                if self.checkWin(temp):
                    self.winTiles.append(tile)

    def getChi(self,tile):
        if len(self.hand) > 0:
            if len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) > 0:
                tile = tile - (len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan))
            if tile < len(self.hand) - 2:
                if self.hand.count(self.hand[tile]) > 0 and self.hand.count(self.hand[tile][0] + str(int(self.hand[tile][1]) + 1)) > 0 and self.hand.count(self.hand[tile][0] + str(int(self.hand[tile][1]) + 2)) > 0:
                    self.handCalls.append(self.hand[tile])
                    self.handCalls.append(self.hand[tile][0] + str(int(self.hand[tile][1]) + 1))
                    self.handCalls.append(self.hand[tile][0] + str(int(self.hand[tile][1]) + 2))

                    self.hand.remove(self.hand[tile][0] + str(int(self.hand[tile][1]) + 2))
                    self.hand.remove(self.hand[tile][0] + str(int(self.hand[tile][1]) + 1))
                    self.hand.remove(self.hand[tile])

            score.richiType = ""
            score.iipatsuType = False

            if len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount + len(self.hand) == 13:
                self.checkTenpai()
            elif len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount + len(self.hand) == 14:
                self.checkWin(self.hand)



    def getPon(self,tile):
        if len(self.hand) > 0:
            if len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) > 0:
                tile = tile - (len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan))
            if tile < len(self.hand) - 2 and self.hand[tile + 1] == self.hand[tile] and self.hand[tile + 2] == self.hand[tile]:
                if self.hand.count(self.hand[tile]) >= 3:
                    for _ in range(3):
                        self.handCalls.append(self.hand[tile])
                        self.hand.remove(self.hand[tile])

            if len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount + len(self.hand) == 13:
                self.checkTenpai()
            elif len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount + len(self.hand) == 14:
                self.checkWin(self.hand)

            score.richiType = ""
            score.iipatsuType = False

    def getKan(self,tile):
        if len(self.hand) > 0:
            if len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) > 0:
                tile = tile - (len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan))
            if tile < len(self.hand) - 3:
                if self.hand.count(self.hand[tile]) == 4:
                    tile = self.hand[tile]
                    for _ in range(4):
                        self.handCallsKan.append(tile)
                        self.hand.remove(tile)

                    self.kanCount += 1

            if len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount + len(self.hand) == 13:
                self.checkTenpai()
            elif len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount + len(self.hand) == 14:
                self.checkWin(self.hand)

            score.richiType = ""
            score.iipatsuType = False

    def getAnkan(self,tile):
        if len(self.hand) > 0:
            if len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) > 0:
                tile = tile - (len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan))
            if tile < len(self.hand) - 3:
                if self.hand.count(self.hand[tile]) == 4:
                    tile = self.hand[tile]
                    self.handCallsAnkan.append("B0")
                    self.handCallsAnkan.append(tile)
                    self.handCallsAnkan.append(tile)
                    self.handCallsAnkan.append("B0")
                    for _ in range(4):
                        self.hand.remove(tile)

                    self.kanCount += 1

            if len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount + len(self.hand) == 13:
                self.checkTenpai()
            elif len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount + len(self.hand) == 14:
                self.checkWin(self.hand)

    def displayButtonShader(self):
        if self.buttonShader != 0:
            for i in range(1,5):
                if i == self.buttonShader:
                    continue
                else:
                    screen.blit(self.shader,(WMARGIN  + TILEWIDTH * 10,HEIGHT - HMARGIN - TILEHEIGHT * (i) - TILEHEIGHT))
            for i in range(5,8):
                if i == self.buttonShader:
                    continue
                else:
                    screen.blit(self.shader,(WMARGIN  + TILEWIDTH * 2 + TILEWIDTH * i,HEIGHT - HMARGIN - TILEHEIGHT * 2))

    def displayDora(self):
        screen.blit(self.doraText,self.doraTextRect)
        if self.dora != "":
            screen.blit(tiles.tileDict.get(self.dora),(WIDTH - WMARGIN - TILEWIDTH,HMARGIN))
        else:
            screen.blit(tiles.tileBack,(WIDTH - WMARGIN - TILEWIDTH,HMARGIN))


    def displayTenpai(self):
        if len(self.hand) + len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount == 13 and len(self.winTiles) > 0:
            self.displayWinTiles()
            screen.blit(self.machitext,self.machiRect)

    def displayWinTiles(self):
        for i in range(len(self.winTiles)):
            pos = (WMARGIN + TILEWIDTH * i,HMARGIN + TILEHEIGHT * 2)
            screen.blit(tiles.tileDict.get(self.winTiles[i]),pos)


    def displayWin(self):
        if len(self.hand) + len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan) - self.kanCount == 14 and self.agari:
            screen.blit(self.agariText,self.agariTextRect)
            for hand in self.confirmedWins:
                kanGap = 0
                for i,shape in enumerate(hand):
                    for j,tile in enumerate(shape):
                        screen.blit(tiles.tileDict.get(tile),(WMARGIN + TILEWIDTH * (j + i * 3) + (TILEWIDTH // 2) * i + kanGap * TILEWIDTH,HMARGIN + TILEHEIGHT * 2))
                    if len(shape) == 4:
                        kanGap += 1
    def displayScore(self):
        pass

    def displayWinds(self):
        screen.blit(self.bakazeText,self.bakazeRect.topleft)
        screen.blit(tiles.tileDict.get(self.bakaze[self.bakazeIndex]),(WMARGIN + TILEWIDTH * 8,HEIGHT - HMARGIN - TILEHEIGHT))
        screen.blit(self.jikazeText, self.jikazeRect.topleft)
        screen.blit(tiles.tileDict.get(self.jikaze[self.jikazeIndex]),
                    (WMARGIN + TILEWIDTH * 9,HEIGHT - HMARGIN - TILEHEIGHT))

    def displayTileNumber(self):
        for i in range(len(self.hand) + len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan)):
            tileNumber = self.font.render(str(i + 1),True,white)
            tileNumberRect = tileNumber.get_rect(center = (WMARGIN + TILEWIDTH // 2 + TILEWIDTH * i,TILEHEIGHT // 2))
            screen.blit(tileNumber,tileNumberRect)

    def displayHand(self):
        for i in range(len(self.hand)):
            pos = (WMARGIN + TILEWIDTH * i + (len(self.handCalls) + len(self.handCallsKan) + len(self.handCallsAnkan)) * TILEWIDTH,HMARGIN)
            screen.blit(tiles.tileDict.get(self.hand[i]),pos)

    def displayHandCalls(self):
        for i in range(len(self.handCalls)):
            pos = (WMARGIN + TILEWIDTH * i,HMARGIN)
            screen.blit(tiles.tileDict.get(self.handCalls[i]),pos)
        for i in range(len(self.handCallsKan)):
            pos = (WMARGIN + TILEWIDTH * i + len(self.handCalls) * TILEWIDTH, HMARGIN)
            screen.blit(tiles.tileDict.get(self.handCallsKan[i]), pos)
        for i in range(len(self.handCallsAnkan)):
            pos = (WMARGIN + TILEWIDTH * i + (len(self.handCallsKan) + len(self.handCalls)) * TILEWIDTH, HMARGIN)
            screen.blit(tiles.tileDict.get(self.handCallsAnkan[i]), pos)

        for i in range(len(self.handCalls) + len(self.handCallsKan)):
            screen.blit(self.shader, (WMARGIN + TILEWIDTH * i, HMARGIN))

    def printKanCount(self):
        if self.kanCount > 0:
            kanCountText = self.font.render(str(self.kanCount),True,"White")
            kanCountRect  = kanCountText.get_rect(center = (WIDTH - TILEWIDTH,HEIGHT - TILEHEIGHT * 2))
            screen.blit(kanCountText,kanCountRect)



    def display(self):
        self.displayHand()
        self.displayHandCalls()
        self.displayTileNumber()
        self.displayTenpai()
        self.displayDora()
        self.displayWin()
        self.printKanCount()
        self.displayWinds()


hand = Hand()