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
    if model.ost > model.zas // model.sower_productivity:
        device.at(11, 5).print("Большое число тунеядцев")
        device.at(12, 6).print("развращает хлеборобов")
        model.sower_productivity -= 1
        device.wait_key()
        device.cls()

    # 1330 IF (OST<NAS/VAL "15") AND (PROIZ<PREDEL) THEN
    #   RANDOMIZE USR VAL "43909":
    #   PRINT AT VAL "11",SGN PI;"pOSTOQNNYJ TRUD WYRABATYWAET";AT VAL "12",VAL "10";"SNOROWKU":
    #   LET PROIZ=PROIZ+SGN PI:
    #   GO SUB KEY:
    #   GO SUB CLS
    if model.ost * 15 < model.population and model.sower_productivity < model.max_sower_productivity:
        device.at(11, 1).print("Постоянный труд вырабатывает сноровку")
        model.sower_productivity += 1
        device.wait_key()
        device.cls()

    # 1340 IF K<VAL "20" THEN
    #   PRINT AT VAL "11",VAL "4";"pLOHOE PITANIE SNIVAET":
    #   PRINT AT VAL "12",VAL "5";" PROIZWODITELXNOSTX!":
    #   LET PROIZ=PROIZ-INT (30/K):
    #   GO SUB KEY:
    #   GO SUB CLS
    if model.feeding_per_worker < 20:
        device.at(11, 4).print("Плохое питание снижает")
        device.at(12, 5).print(" производительность!")
        model.sower_productivity -= 30 // model.feeding_per_worker
        device.wait_key()
        device.cls()

    # 1350 IF PROIZ<=BIN THEN LET PROIZ=INT PI
    if model.sower_productivity <= 0:
        model.sower_productivity = 1

    # 1360 IF (K>VAL "30") AND (PROIZ<PREDEL) THEN
    #   PRINT AT VAL "11",SGN PI;"nA HORO[IH HAR^AH I RABOTAETSQ";
    #       AT VAL "12",VAL "13";"LU^[E":
    #   LET PROIZ=PROIZ+SGN PI:
    #   GO SUB KEY:
    #   GO SUB CLS
    if model.feeding_per_worker > 30 and model.sower_productivity < model.max_sower_productivity:
        device.at(11, 1).print("На хороших харчах и работается")
        device.at(12, 13).print("лучше")
        model.sower_productivity += 1
        device.wait_key()
        device.cls()

    # 1370 LET UROV=SGN PI+FN S(VAL "6")-IST:
    #   LET J=FN S(VAL "21")
    model.grain_yield = 1 + randint(6)
    j = randint(21)

    # 1380 IF J>=VAL "18" THEN LET UROV=VAL "10"
    if j >= 18:
        model.grain_yield = 10

    # 1390 IF J<=INT PI THEN LET UROV=SGN PI
    if j <= 3:
        model.grain_yield = 1

    # 1400 IF UROV<SGN PI THEN LET UROV=SGN PI
    if model.grain_yield < 1:
        model.grain_yield = 1

    # 1410 IF UROV>VAL "5" THEN
    #   RANDOMIZE USR VAL "58252":
    #   PRINT AT VAL "11",VAL "7";"oTLI^NYJ UROVAJ!!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if model.grain_yield > 5:
        device.at(11, 7).print("Отличный урожай!!!")
        device.wait_key()
        device.cls()

    # 1420 LET I=BIN :
    #   IF UROV<VAL "2" THEN
    #       LET I=FN S(INT PI)
    i = 0
    if model.grain_yield < 2:
        i = randint(3)

    # 1430 IF I=SGN PI THEN
    #   RANDOMIZE USR VAL "62884":
    #   PRINT AT VAL "11",INT PI;"zASUHA POGUBILA UROVAJ!!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if i == 1:
        device.at(11, 3).print("Засуха погубила урожай!!!")
        device.wait_key()
        device.cls()

    # 1440 IF I=VAL "2" THEN
    #   RANDOMIZE USR VAL "60568":
    #   PRINT AT VAL "11",BIN ;"pYLEWYE BURI POGUBILI UROVAJ!!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if i == 2:
        device.at(11, 0).print("Пылевые бури погубили урожай!!!")
        device.wait_key()
        device.cls()

    # 1450 IF I=INT PI THEN RANDOMIZE USR VAL "59410":
    #   PRINT AT VAL "11",BIN ;"lIWNEWYE DOVDI POGUBILI UROVAJ!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if i == 3:
        device.at(11, 0).print("Ливневые дожди погубили урожай!!")
        device.wait_key()
        device.cls()

    # 1460 LET SBOR=ZAS*UROV
    model.harvest = model.zas * model.grain_yield

    # 1470 IF RND>0.7 THEN
    #   LET SAR=4+FN S(8):
    #   LET SBOR=SBOR-INT (SBOR/SAR):
    #   RANDOMIZE USR VAL "61726":
    #   PRINT AT VAL "11",SGN PI;"sARAN^A POGUBILA 1/";SAR;" UROVAQ!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if random() > 0.7:
        sar = 4 + randint(8)
        model.harvest -= model.harvest // sar
        device.at(11, 1).print(f"Саранча погубила 1/{sar} урожая!")
        device.wait_key()
        device.cls()

    # 1480 LET ZERNO=ZERNO+SBOR:
    #   LET J=FN S(5)
    model.grain += model.harvest
    j = randint(5)

    # 1490 IF J=SGN PI THEN
    #   LET KRYS=INT (ZERNO/(FN S(10)+7)):
    #   RANDOMIZE USR VAL "57094":
    #   PRINT AT VAL "11",VAL "4";"nA GOROD NAPALI KRYSY!!!":
    #   LET ZERNO=ZERNO-KRYS:
    #   GO SUB KEY:
    #   GO SUB CLS
    if j == 1:
        model.rats = model.grain // (randint(10) + 7)
        device.at(11, 4).print("На город напали крысы!!!")
        model.grain -= model.rats
        device.wait_key()
        device.cls()

    # 1500 RETURN
