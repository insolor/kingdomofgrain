from random import random

from io_devices import AbstractIO
from game_model import GameModel
from grain import randint


def harvest(device: AbstractIO, model: GameModel):
    # 1300 REM \#017\#001UBORKA\#017\#000
    # 1305 GO SUB CLS
    device.cls()

    # 1320 IF OST>INT (ZAS/PROIZ) THEN
    #   RANDOMIZE USR VAL "47383":
    #   PRINT AT VAL "11",VAL "5";"bOLX[OE ^ISLO TUNEQDCEW":
    #   PRINT AT VAL "12",VAL "6";"RAZWRA]AET HLEBOROBOW":
    #   LET PROIZ=PROIZ-SGN PI:
    #   GO SUB KEY:
    #   GO SUB CLS
    if model.ost > model.zas // model.proiz:
        device.at(11, 5).print("Большое число тунеядцев")
        device.at(12, 6).print("развращает хлеборобов")
        model.proiz -= 1
        device.key()
        device.cls()

    # 1330 IF (OST<NAS/VAL "15") AND (PROIZ<PREDEL) THEN
    #   RANDOMIZE USR VAL "43909":
    #   PRINT AT VAL "11",SGN PI;"pOSTOQNNYJ TRUD WYRABATYWAET";AT VAL "12",VAL "10";"SNOROWKU":
    #   LET PROIZ=PROIZ+SGN PI:
    #   GO SUB KEY:
    #   GO SUB CLS
    if model.ost * 15 < model.nas and model.proiz < model.predel:
        device.at(11, 1).print("Постоянный труд вырабатывает сноровку")
        model.proiz += 1
        device.key()
        device.cls()

    # 1340 IF K<VAL "20" THEN
    #   PRINT AT VAL "11",VAL "4";"pLOHOE PITANIE SNIVAET":
    #   PRINT AT VAL "12",VAL "5";" PROIZWODITELXNOSTX!":
    #   LET PROIZ=PROIZ-INT (30/K):
    #   GO SUB KEY:
    #   GO SUB CLS
    if model.k < 20:
        device.at(11, 4).print("Плохое питание снижает")
        device.at(12, 5).print(" производительность!")
        model.proiz -= 30 // model.k
        device.key()
        device.cls()

    # 1350 IF PROIZ<=BIN THEN LET PROIZ=INT PI
    if model.proiz <= 0:
        model.proiz = 1

    # 1360 IF (K>VAL "30") AND (PROIZ<PREDEL) THEN
    #   PRINT AT VAL "11",SGN PI;"nA HORO[IH HAR^AH I RABOTAETSQ";
    #       AT VAL "12",VAL "13";"LU^[E":
    #   LET PROIZ=PROIZ+SGN PI:
    #   GO SUB KEY:
    #   GO SUB CLS
    if model.k > 30 and model.proiz < model.predel:
        device.at(11, 1).print("На хороших харчах и работается")
        device.at(12, 13).print("лучше")
        model.proiz += 1
        device.key()
        device.cls()

    # 1370 LET UROV=SGN PI+FN S(VAL "6")-IST:
    #   LET J=FN S(VAL "21")
    model.urozh = 1 + randint(6)
    j = randint(21)

    # 1380 IF J>=VAL "18" THEN LET UROV=VAL "10"
    if j >= 18:
        model.urozh = 10

    # 1390 IF J<=INT PI THEN LET UROV=SGN PI
    if j <= 3:
        model.urozh = 1

    # 1400 IF UROV<SGN PI THEN LET UROV=SGN PI
    if model.urozh < 1:
        model.urozh = 1

    # 1410 IF UROV>VAL "5" THEN
    #   RANDOMIZE USR VAL "58252":
    #   PRINT AT VAL "11",VAL "7";"oTLI^NYJ UROVAJ!!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if model.urozh > 5:
        device.at(11, 7).print("Отличный урожай!!!")
        device.key()
        device.cls()

    # 1420 LET I=BIN :
    #   IF UROV<VAL "2" THEN
    #       LET I=FN S(INT PI)
    i = 0
    if model.urozh < 2:
        i = randint(3)

    # 1430 IF I=SGN PI THEN
    #   RANDOMIZE USR VAL "62884":
    #   PRINT AT VAL "11",INT PI;"zASUHA POGUBILA UROVAJ!!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if i == 1:
        device.at(11, 3).print("Засуха погубила урожай!!!")
        device.key()
        device.cls()

    # 1440 IF I=VAL "2" THEN
    #   RANDOMIZE USR VAL "60568":
    #   PRINT AT VAL "11",BIN ;"pYLEWYE BURI POGUBILI UROVAJ!!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if i == 2:
        device.at(11, 0).print("Пылевые бури погубили урожай!!!")
        device.key()
        device.cls()

    # 1450 IF I=INT PI THEN RANDOMIZE USR VAL "59410":
    #   PRINT AT VAL "11",BIN ;"lIWNEWYE DOVDI POGUBILI UROVAJ!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if i == 3:
        device.at(11, 0).print("Ливневые дожди погубили урожай!!")
        device.key()
        device.cls()

    # 1460 LET SBOR=ZAS*UROV
    model.sbor = model.zas * model.urozh

    # 1470 IF RND>0.7 THEN
    #   LET SAR=4+FN S(8):
    #   LET SBOR=SBOR-INT (SBOR/SAR):
    #   RANDOMIZE USR VAL "61726":
    #   PRINT AT VAL "11",SGN PI;"sARAN^A POGUBILA 1/";SAR;" UROVAQ!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if random() > 0.7:
        sar = 4 + randint(8)
        model.sbor -= model.sbor // sar
        device.at(11, 1).print(f"Саранча погубила 1/{sar} урожая!")
        device.key()
        device.cls()

    # 1480 LET ZERNO=ZERNO+SBOR:
    #   LET J=FN S(5)
    model.zerno += model.sbor
    j = randint(5)

    # 1490 IF J=SGN PI THEN
    #   LET KRYS=INT (ZERNO/(FN S(10)+7)):
    #   RANDOMIZE USR VAL "57094":
    #   PRINT AT VAL "11",VAL "4";"nA GOROD NAPALI KRYSY!!!":
    #   LET ZERNO=ZERNO-KRYS:
    #   GO SUB KEY:
    #   GO SUB CLS
    if j == 1:
        model.krys = model.zerno // (randint(10) + 7)
        device.at(11, 4).print("На город напали крысы!!!")
        model.zerno -= model.krys
        device.key()
        device.cls()

    # 1500 RETURN
