from random import random

from io_devices import AbstractIO
from game_model import GameModel
from grain import randint


def intervention(device: AbstractIO, model: GameModel):
    """Intervention of enemies"""
    # 1860 REM \#017\#001WTORVENIE\#017\#000
    # 1870 LET RASST=RASST-FN S(VAL "5")-VAL "10"
    model.distance_to_enemies -= randint(5) + 10

    # 1880 IF RASST<FN S(VAL "\{f0}5") THEN GO SUB ATAKA: GO TO VAL "1900"
    if model.distance_to_enemies < randint(5):
        attack_by_enemies(device, model)

    # 1890 IF (RASST<VAL "15") AND (RND<0.1) THEN
    #   PRINT AT VAL "11",SGN PI;"wRAGI SOWER[ILI STREMITELXNYJ";AT VAL "12",VAL "9";"MAR[ - BROSOK!":
    #   GO SUB KEY:
    #   GO SUB CLS:
    #   GO SUB ATAKA
    elif model.distance_to_enemies < 15 and random() < 0.1:
        device.at(11, 1).print("Враги совершили стремительный")
        device.at(12, 9).print("марш - бросок!")
        device.key()
        device.cls()
        attack_by_enemies(device, model)
    # 1900 RETURN


def attack_by_enemies(device: AbstractIO, model: GameModel):
    # 1910 REM \#017\#001ATAKA\#017\#000
    # 1920 RANDOMIZE USR VAL "54778":
    #   PRINT AT VAL "11",VAL "7";"\{i3}gorod atakowan!!!":
    #   GO SUB KEY:
    #   LET I=INT (INT (10*RND)*0.1)+0.5:
    #   LET J=I+INT (INT (10*RND)*0.15)+0.5
    device.at(11, 7).ink(3).print("ГОРОД АТАКОВАН!!!")
    device.key()

    i = int(int(10 * random()) * 0.1) + 0.5
    j = i + int(int(10 * random()) * 0.15) + 0.5

    # 1930 IF WRAGI>Z*J THEN
    #   PRINT AT VAL "13",BIN ;"gOROD PAL,WEDX EGO ZA]I]ALO MALO":
    #   PRINT AT VAL "14",VAL "13";"SOLDAT":
    #   GO SUB KEY:
    #   GO SUB CLS:
    #   LET U=SGN PI:
    #   LET OI=BIN :
    #   GO SUB OITOG:
    #   RETURN
    if model.enemies > model.defenders * j:
        device.at(13, 0).print("Город пал, ведь его защищало мало")
        device.at(14, 13).print("солдат")
        device.key()
        device.cls()

        model.u = True
        model.oi = False
        return
        # 1940 IF Z*J>WRAGI THEN
        #   PRINT AT VAL "13",INT PI;"NO ATAKA OTBITA! uRA-A-A!!!"
    else:
        device.at(13, 1).print("Но атака отбита! Ура-а-а!!!")

        # 1950 IF FN S(3)=SGN PI THEN
        #   PRINT AT VAL "15",INT PI;"pROIZO[LA RE[A\@]AQ BITWA!!!"
        if randint(3) == 1:
            device.at(15, 1).print("Произошла решающая битва!!!")

        # 1960 LET POGIBZ=INT (WRAGI/3)+INT (RND*Z/6):
        #   LET POGIB=POGIB+POGIBZ:
        #   LET NAS=NAS-POGIB:
        #   LET RASST=25+FN S(20):
        #   LET WRAGI=INT (NAS/4)+INT (RND*NAS/5)
        pogibz = model.enemies // 3 + int(random() * model.defenders / 6)
        model.dead_in_battles += pogibz
        model.population -= model.dead_in_battles
        model.distance_to_enemies = 25 + randint(20)
        model.enemies = int(model.population / 4) + int(random() * model.population / 5)

        # 1965 GO TO KEY:
        #   GO SUB CLS
        device.key()
        device.cls()

        # 1970 RETURN
