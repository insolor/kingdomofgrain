from random import random

from io_devices.abstract_io import AbstractIO
from game_model import GameModel
from grain import fn_s


def uborka(device: AbstractIO, model: GameModel):
    # global proiz, zerno, urozh
    # 1300 REM \#017\#001UBORKA\#017\#000
    # 1305 GO SUB CLS
    cls()
    # 1320 IF OST>INT (ZAS/PROIZ) THEN
    #   RANDOMIZE USR VAL "47383":
    #   PRINT AT VAL "11",VAL "5";"bOLX[OE ^ISLO TUNEQDCEW":
    #   PRINT AT VAL "12",VAL "6";"RAZWRA]AET HLEBOROBOW":
    #   LET PROIZ=PROIZ-SGN PI:
    #   GO SUB KEY:
    #   GO SUB CLS
    if ost > zas // proiz:
        print("Большое число тунеядцев\nразвращает хлеборобов")
        proiz -= 1
        key()
        cls()
    # 1330 IF (OST<NAS/VAL "15") AND (PROIZ<PREDEL) THEN
    #   RANDOMIZE USR VAL "43909":
    #   PRINT AT VAL "11",SGN PI;"pOSTOQNNYJ TRUD WYRABATYWAET";AT VAL "12",VAL "10";"SNOROWKU":
    #   LET PROIZ=PROIZ+SGN PI:
    #   GO SUB KEY:
    #   GO SUB CLS
    if ost * 15 < nas and proiz < predel:
        print("Постоянный труд вырабатывает сноровку")
        proiz += 1
        key()
        cls()
    # 1340 IF K<VAL "20" THEN
    #   PRINT AT VAL "11",VAL "4";"pLOHOE PITANIE SNIVAET":
    #   PRINT AT VAL "12",VAL "5";" PROIZWODITELXNOSTX!":
    #   LET PROIZ=PROIZ-INT (30/K):
    #   GO SUB KEY:
    #   GO SUB CLS
    if k < 20:
        print("Плохое питание снижает\n производительность!")
        proiz -= 30 // k
        key()
        cls()
    # 1350 IF PROIZ<=BIN THEN LET PROIZ=INT PI
    if proiz <= 0:
        proiz = 1
    # 1360 IF (K>VAL "30") AND (PROIZ<PREDEL) THEN
    #   PRINT AT VAL "11",SGN PI;"nA HORO[IH HAR^AH I RABOTAETSQ";AT VAL "12",VAL "13";"LU^[E":
    #   LET PROIZ=PROIZ+SGN PI:
    #   GO SUB KEY:
    #   GO SUB CLS
    if k > 30 and proiz < predel:
        print("На хороших харчах и работается\nлучше")
        proiz += 1
        key()
        cls()
    # 1370 LET UROV=SGN PI+FN S(VAL "6")-IST:
    #   LET J=FN S(VAL "21")
    urozh = 1 + fn_s(6)
    j = fn_s(21)
    # 1380 IF J>=VAL "18" THEN LET UROV=VAL "10"
    if j >= 18:
        urozh = 10
    # 1390 IF J<=INT PI THEN LET UROV=SGN PI
    if j <= 3:
        urozh = 1
    # 1400 IF UROV<SGN PI THEN LET UROV=SGN PI
    if urozh < 1:
        urozh = 1
    # 1410 IF UROV>VAL "5" THEN
    #   RANDOMIZE USR VAL "58252":
    #   PRINT AT VAL "11",VAL "7";"oTLI^NYJ UROVAJ!!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if urozh > 5:
        print("Отличный урожай!!!")
        key()
        cls()
    # 1420 LET I=BIN : IF UROV<VAL "2" THEN LET I=FN S(INT PI)
    i = 0
    if urozh < 2:
        i = fn_s(3)
    # 1430 IF I=SGN PI THEN
    #   RANDOMIZE USR VAL "62884":
    #   PRINT AT VAL "11",INT PI;"zASUHA POGUBILA UROVAJ!!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if i == 1:
        print("Засуха погубила урожай!!!")
        key()
        cls()
    # 1440 IF I=VAL "2" THEN
    #   RANDOMIZE USR VAL "60568":
    #   PRINT AT VAL "11",BIN ;"pYLEWYE BURI POGUBILI UROVAJ!!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if i == 2:
        print("Пылевые бури погубили урожай!!!")
        key()
        cls()
    # 1450 IF I=INT PI THEN RANDOMIZE USR VAL "59410":
    #   PRINT AT VAL "11",BIN ;"lIWNEWYE DOVDI POGUBILI UROVAJ!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if i == 3:
        print("Ливневые дожди погубили урожай!!")
        key()
        cls()
    # 1460 LET SBOR=ZAS*UROV
    sbor = zas * urozh
    # 1470 IF RND>0.7 THEN LET SAR=4+FN S(8):
    #   LET SBOR=SBOR-INT (SBOR/SAR):
    #   RANDOMIZE USR VAL "61726":
    #   PRINT AT VAL "11",SGN PI;"sARAN^A POGUBILA 1/";SAR;" UROVAQ!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if random() > 0.7:
        sar = 4 + fn_s(8)
        sbor -= sbor // sar
        print("Саранча погубила 1/%d урожая!" % sar)
        key()
        cls()
    # 1480 LET ZERNO=ZERNO+SBOR: LET J=FN S(5)
    zerno += sbor
    j = fn_s(5)
    # 1490 IF J=SGN PI THEN
    #   LET KRYS=INT (ZERNO/(FN S(10)+7)):
    #   RANDOMIZE USR VAL "57094":
    #   PRINT AT VAL "11",VAL "4";"nA GOROD NAPALI KRYSY!!!":
    #   LET ZERNO=ZERNO-KRYS:
    #   GO SUB KEY:
    #   GO SUB CLS
    if j == 1:
        krys = zerno // (fn_s(10) + 7)
        print("На город напали крысы!!!")
        zerno -= krys
        key()
        cls()
    # 1500 RETURN