from hands import hand
from score import *

def pinfu(list,winTiles):
    if (len(hand.handCalls) + len(hand.handCallsKan) + len(hand.handCallsAnkan)) == 0:
        if len(winTiles) >= 2:
            if winTiles[0] != winTiles[1][0] + str(int(winTiles[1][1]) - 3):
                return []
        for shape in list:
            if len(shape) == 3:
                if shape.count(shape[0]) > 1:
                    return []
            elif len(shape) == 2:
                if shape[0] in ["H5","H6","H7"] or shape[0] == hand.bakaze[hand.bakazeIndex] or shape[0] == hand.jikaze[hand.jikazeIndex]:
                    return []

        return ["平和",1]

def iipeikou(list):
    if (len(hand.handCalls) + len(hand.handCallsKan) + len(hand.handCallsAnkan)) == 0:
        doubleCount = 0
        checkedShapes = []
        for shape in list:
            if list.count(shape) == 2 and shape not in checkedShapes:
                doubleCount += 1
                checkedShapes.append(shape)

        if doubleCount == 1:
            return ["一盃口",1]
        elif doubleCount == 2:
            return ["二盃口", 3]

    return []

def tanyao(list):
    for shape in list:
        for tile in shape:
            if tile in ["M1","M9","P1","P9","S1","S9","H1","H2","H3","H4","H5","H6","H7"]:
                return []

    return ["断么九",1]

def yakuhai(list):
    yakuhaiCount = []
    for shape in list:
        if len(shape) >= 3:
            match shape[1]:
                case "H5":
                    yakuhaiCount.append(["白",1])
                case "H6":
                    yakuhaiCount.append(["發", 1])
                case "H7":
                    yakuhaiCount.append(["中",1])

            if shape[1] == "H1" and (hand.bakaze[hand.bakazeIndex] == "H1" or hand.jikaze[hand.jikazeIndex] == "H1"):
                yakuhaiCount.append(["東", 1])
            elif shape[1] == "H2" and (hand.bakaze[hand.bakazeIndex] == "H2" or hand.jikaze[hand.jikazeIndex] == "H2"):
                yakuhaiCount.append(["南", 1])
            elif shape[1] == "H3" and (hand.bakaze[hand.bakazeIndex] == "H3" or hand.jikaze[hand.jikazeIndex] == "H3"):
                yakuhaiCount.append(["西", 1])
            elif shape[1] == "H4" and (hand.bakaze[hand.bakazeIndex] == "H4" or hand.jikaze[hand.jikazeIndex] == "H4"):
                yakuhaiCount.append(["北", 1])

    return yakuhaiCount

def chitoi(list):
    pairCount = 0
    for shape in list:
        if list.count(shape) == 1:
            pairCount += 1

    if pairCount == 7:
        return ["七対子",2]
    else:return []

def sanshokudoujyun(list):
    for shape in list:
        if len(shape) == 3:
            if shape[0][0] == "M" and shape[0][1] == str(int(shape[1][1]) - 1) and shape[0][1] == str(int(shape[2][1]) - 2):
                if ("P" + shape[0][1],"P" + shape[1][1],"P" + shape[2][1]) in list and ("S" + shape[0][1],"S" + shape[1][1],"S" + shape[2][1]) in list:
                    if (len(hand.handCalls) + len(hand.handCallsKan)) > 0:
                        return ["三色同順",1]
                    else:
                        return ["三色同順",2]

    return []

def iitsu(list):
    for suit in ["M","P","S"]:
        if (suit + "1",suit + "2",suit + "3") in list and (suit + "4",suit + "5",suit + "6") in list and (suit + "7",suit + "8",suit + "9") in list:
            if (len(hand.handCalls) + len(hand.handCallsKan)) > 0:
                return ["一気通貫", 1]
            else:
                return ["一気通貫", 2]

    return []

def chanta(list):
    honors = 0
    for shape in list:
        if len(shape) == 4:
            if shape[1] not in ["M1","M9","P1","P9","S1","S9","H1","H2","H3","H4","H5","H6","H7"]:
                return []
            if shape[1] in ["H1","H2","H3","H4","H5","H6","H7"]:
                honors += 1
        else:
            if shape[0] not in ["M1","M9","P1","P9","S1","S9","H1","H2","H3","H4","H5","H6","H7"] and shape[-1] not in ["M1","M9","P1","P9","S1","S9","H1","H2","H3","H4","H5","H6","H7"]:
                return []
            if shape[0] in ["H1","H2","H3","H4","H5","H6","H7"]:
                honors += 1

    if (len(hand.handCalls) + len(hand.handCallsKan)) > 0:
        if honors > 0:
            return ["混全帯么九", 1]
        else:
            return ["純全帯么九", 2]
    else:
        if honors > 0:
            return ["混全帯么九", 2]
        else:
            return ["純全帯么九", 3]

def toitoi(list):
    if (len(hand.handCalls) + len(hand.handCallsKan)) > 0:
        for shape in list:
            if len(shape) == 3:
                if shape.count(shape[0]) != 3:
                    return []

        return ["対々和",2]
    return []

def shoudaisangen(list):
    triplet = 0
    pair = 0
    for drag in ['H5','H6','H7']:
        if (drag,drag,drag) in list or (drag,drag,drag,drag) in list or ("B0",drag,drag,"B0") in list:
            triplet += 1
        elif (drag,drag) in list:
            pair += 1

    if triplet == 2 and pair == 1:
        return ["小三元",2]
    elif triplet == 3:
        return ["大三元",1]
    else:
        return []

def sanAnkou(list):
    ankou = 0
    pairWait = False
    for shape in list:
        if len(shape) == 3:
            if shape.count(shape[0]) == 3 and shape not in hand.handCalls:
                if hand.hand[-1] not in shape or score.winType == "tumo":
                    ankou += 1
        elif len(shape) == 4 and shape not in hand.handCallsKan:
            if hand.hand[-1] not in shape or score.winType == "tumo":
                ankou += 1
        elif len(shape) == 2 and hand.hand[-1] in shape:
            pairWait = True

    if ankou == 3:
        return ["三暗刻",2]
    elif ankou == 4 and pairWait == False:
        return ["四暗刻",1]
    elif ankou == 4 and pairWait == True:
        return ["四暗刻単騎",2]
    else:
        return []

def honchinroutou(list):
    triplet = 0
    honor = 0
    for shape in list:
        if len(shape) == 3:
            if shape[0] in ["M1","M9","P1","P9","S1","S9"] and shape[0] == shape[1]:
                triplet += 1
            elif shape[0] in ["H1","H2","H3","H4","H5","H6","H7"] and shape[0] == shape[1]:
                triplet += 1
                honor += 1

        elif len(shape) == 4:
            if shape[1] in ["M1","M9","P1","P9","S1","S9"]:
                triplet += 1
            elif shape[1] in ["H1","H2","H3","H4","H5","H6","H7"]:
                triplet += 1
                honor += 1
        elif len(shape) == 2:
            if shape[0] not in ["M1","M9","P1","P9","S1","S9","H1","H2","H3","H4","H5","H6","H7"]:
                return []
            if shape[0] in ["H1","H2","H3","H4","H5","H6","H7"]:
                honor += 1

    if triplet == 4 and honor > 0:
        return ['混老頭',2]
    elif triplet == 4 and honor == 0:
        return ['清老頭',1]
    else:
        return []

def sanshokudoukou(list):
    for shape in list:
        if shape.count(shape[1]) >= 2 and shape[1][0] == "M":
            if (("S" + shape[1][1],"S" + shape[1][1],"S" + shape[1][1]) in list or ("S" + shape[1][1],"S" + shape[1][1],"S" + shape[1][1],"S" + shape[1][1]) in list or ("B0","S" + shape[1][1],"S" + shape[1][1],"B0") in list) and \
                    (("P" + shape[1][1], "P" + shape[1][1], "P" + shape[1][1]) in list or (
                    "P" + shape[1][1], "P" + shape[1][1], "P" + shape[1][1], "P" + shape[1][1]) in list or (
                     "B0", "P" + shape[1][1], "P" + shape[1][1], "B0") in list):
                return ["三色同刻",2]

    return []

def sansuuKantsu(list):
    kan = 0
    for shape in list:
        if len(shape) == 4:
            kan += 1

    if kan == 3:
        return ["三槓子",2]
    elif kan == 4:
        return ["四槓子",1]
    else:
        return []

def honchiniitsu(list):
    suitCount = 0
    suit = ""
    honor = 0
    for shape in list:
        if suit == "" and shape[1][0] != "H":
            suit = shape[1][0]
            suitCount += 1

        elif shape[1][0] == suit:
            suitCount += 1

        elif shape[1][0] == "H":
            honor += 1

    if suitCount + honor == 5 and honor != 0:
        if (len(hand.handCalls) + len(hand.handCallsKan)) > 0:
            return ["混一色",2]
        else:
            return ["混一色", 3]
    elif suitCount == 5 and honor == 0:
        if (len(hand.handCalls) + len(hand.handCallsKan)) > 0:
            return ["清一色",5]
        else:
            return ["清一色", 6]
    else:
        return []

def kokushi(list,winTiles):
    if len(list) == 14:
        if len(winTiles) == 13:
            return ["国士無双十三面待ち",2]
        else:
            return ["国士無双",1]
    return []

def chuuren(list,winTiles):
    if len(hand.handCalls) + len(hand.handCallsKan) == 0:
        tempList = []
        for shape in list:
            for tile in shape:
                tempList.append(tile)

        for suit in ["M","S","P"]:
            if tempList.count(suit + "1") >= 3 and tempList.count(suit + "2") >= 1 and tempList.count(suit + "3") >= 1 and tempList.count(suit + "4") >= 1 and tempList.count(suit + "5") >= 1 \
                    and tempList.count(suit + "6") >= 1 and tempList.count(suit + "7") >= 1 and tempList.count(suit + "8") >= 1 and tempList.count(suit + "9") >= 3:
                if len(winTiles) == 9:
                    return ["純正九蓮宝燈",2]
                else:
                    return ["九蓮宝燈",1]

    return []

def shoudaisuushii(list):
    triplet = 0
    pair = 0
    for shape in list:
        if len(shape) >= 3:
            if shape[1] in ["H1","H2","H3","H4"]:
                triplet += 1
        elif len(shape) == 2:
            if shape[1] in ["H1", "H2", "H3", "H4"]:
                pair += 1

    if triplet + pair == 4:
        if pair > 0:
            return ["小四喜",1]
        else:
            return ["大四喜",2]

    return []


def tsuiisou(list):
    for shape in list:
        for tile in shape:
            if tile not in ["H1","H2","H3","H4","H5","H6","H7"]:
                return []

    return ["字一色",1]

def ryuuiisou(list):
    for shape in list:
        for tile in shape:
            if tile not in ["S2","S3","S4","S6","S8","H6"]:
                return []

    return ["緑一色",1]

def getYakuList(hand,winTiles):
    yakuList = []
    yakuList.append(pinfu(hand,winTiles))
    yakuList.append(iipeikou(hand))
    yakuList.append(tanyao(hand))
    yakuList.append(iitsu(hand))
    yakuList.append(chanta(hand))
    yakuList.append(toitoi(hand))
    yakuList.append(shoudaisangen(hand))
    # yakuList.append(sanAnkou(hand))
    yakuList.append(honchinroutou(hand))
    yakuList.append(sanshokudoukou(hand))
    yakuList.append(sansuuKantsu(hand))
    yakuList.append(honchiniitsu(hand))
    yakuList.append(kokushi(hand,winTiles))
    yakuList.append(chuuren(hand,winTiles))
    yakuList.append(shoudaisuushii(hand))
    yakuList.append(tsuiisou(hand))
    yakuList.append(ryuuiisou(hand))

    for i in range(len(yakuList) - 1,-1,-1):
        if yakuList[i] == []:
            del yakuList[i]

    print(yakuList)

getYakuList([('M1', 'M2', 'M3'), ('P5', 'P6', 'P7'), ('S7', 'S8', 'S9'), ('M7', 'M8', 'M9'), ('S1', 'S1')],['M6', 'M9'])

# print(pinfu([('M1', 'M2', 'M3'), ('P5', 'P6', 'P7'), ('S7', 'S8', 'S9'), ('M7', 'M8', 'M9'), ('S1', 'S1')],['M6', 'M9']))
# print(iipeikou([('M1', 'M2', 'M3'), ('M1', 'M2', 'M3'), ('S7', 'S8', 'S9'), ('S7', 'S8', 'S9'), ('S1', 'S1')]))
# print(tanyao([('M4', 'M5', 'M6'), ('P2', 'P3', 'P4'), ('S5', 'S6', 'S7'), ('P6', 'P7', 'P8'), ('M8', 'M8')]))
# print(yakuhai([('M1', 'M1', 'M1'), ('P5', 'P6', 'P7'), ('S7', 'S8', 'S9'), ('H6', 'H6', 'H6'), ('S1', 'S1')]))
# print(chitoi([('M1', 'M1'), ('P3', 'P3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('H7', 'H7'), ('P9', 'P9')]))\
# print(sanshokudoujyun([('M1', 'M2', 'M3'), ('S1', 'S2', 'S3'), ('P1', 'P2', 'P3'), ('M7', 'M8', 'M9'), ('S1', 'S1')]))
# print(iitsu([('M1', 'M2', 'M3'), ('S1', 'S2', 'S3'), ('M4','M5','M6'), ('M7', 'M8', 'M9'), ('S1', 'S1')]))
# print(chanta([('P9', 'P9', 'P9'), ('M1', 'M2', 'M3'), ('P1', 'P2', 'P3'), ('P7', 'P8', 'P9'), ('S1', 'S1')]))
# print(toitoi([('H7', 'H7', 'H7'), ('M1', 'M1', 'M1'), ('P9', 'P9', 'P9'), ('H6', 'H6', 'H6', 'H6'), ('M9', 'M9')]))
# print(shoudaisangen([('H7', 'H7'), ('M7', 'M8', 'M9'), ('H6', 'H6', 'H6'), ('B0', 'H5', 'H5', 'B0'), ('P9', 'P9','P9')]))
# print(sanAnkou([('S6', 'S6', 'S6'), ('S4', 'S5', 'S6'), ('M5', 'M5', 'M5'), ('B0', 'P9', 'P9', 'B0'), ('P9', 'P9')]))
# print(honchinroutou([('M1', 'M1', 'M1'), ('P1', 'P1', 'P1'), ('P9', 'P9', 'P9'), ('S9', 'S9', 'S9'), ('H1', 'H1')]))
# print(sanshokudoukou([('P5', 'P5', 'P5'), ('P7', 'P8', 'P9'), ('S5', 'S5', 'S5'), ('B0', 'M5', 'M5', 'B0'), ('H7', 'H7')]))
# print(sansuuKantsu([('M1', 'M1', 'M1', 'M1'), ('H7', 'H7', 'H7', 'H7'), ('S9', 'S9', 'S9', 'S9'), ('B0', 'P9', 'P9', 'B0'), ('P7', 'P7')]))
# print(honchiniitsu([('M5', 'M5', 'M5'), ('M1', 'M2', 'M3'), ('M3', 'M4', 'M5'), ('M7', 'M8', 'M9'), ('M8', 'M8')]))
# print(kokushi(['M1', 'P1', 'P9', 'S1', 'S9', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'M9', 'M9'],['M1', 'M9', 'P1', 'P9', 'S1', 'S9', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7']))
# print(chuuren([('M9', 'M9', 'M9'), ('M1', 'M2', 'M3'), ('M4', 'M5', 'M6'), ('M7', 'M8', 'M9'), ('M1', 'M1')],['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9']))
# print(shoudaisuushii([('H1', 'H1', 'H1'), ('H2', 'H2', 'H2'), ('H3', 'H3', 'H3'), ('H4', 'H4', 'H4'), ('P7', 'P7')]))
# print(tsuiisou([('H1', 'H1', 'H1'), ('H2', 'H2', 'H2'), ('H7', 'H7', 'H7'), ('H4', 'H4', 'H4'), ('H5', 'H5')]))
# print(ryuuiisou([('H6', 'H6', 'H6'), ('S2', 'S2', 'S2'), ('S6', 'S6', 'S6'), ('S2', 'S3', 'S4'), ('S8', 'S8')]))