from random import random

from abstract_screen import AbstractScreen
from game_model import GameModel
from grain import fn_s


def intervention(screen: AbstractScreen, model: GameModel):
    # global rasst
    # 1860 REM \#017\#001WTORVENIE\#017\#000
    # 1870 LET RASST=RASST-FN S(VAL "5")-VAL "10"
    rasst -= fn_s(5) + 10
    # 1880 IF RASST<FN S(VAL "\{f0}5") THEN GO SUB ATAKA: GO TO VAL "1900"
    if rasst < fn_s(5):
        attack_by_enemies()
    # 1890 IF (RASST<VAL "15") AND (RND<0.1) THEN
    #   PRINT AT VAL "11",SGN PI;"wRAGI SOWER[ILI STREMITELXNYJ";AT VAL "12",VAL "9";"MAR[ - BROSOK!":
    #   GO SUB KEY:
    #   GO SUB CLS:
    #   GO SUB ATAKA
    elif rasst < 15 and random() < 0.1:
        print("Враги совершили стремительный марш - бросок!")
        key()
        cls()
        attack_by_enemies()
    # 1900 RETURN


def attack_by_enemies(screen: AbstractScreen, model: GameModel):
    # global nas, pogib, rasst, vragi
    # 1910 REM \#017\#001ATAKA\#017\#000
    # 1920 RANDOMIZE USR VAL "54778":
    #   PRINT AT VAL "11",VAL "7";"\{i3}gorod atakowan!!!":
    #   GO SUB KEY:
    #   LET I=INT (INT (10*RND)*0.1)+0.5: LET J=I+INT (INT (10*RND)*0.15)+0.5
    print("ГОРОД АТАКОВАН!!!")
    key()
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
    if vragi > z * j:
        print("Город пал, ведь его защищало мало солдат")
        key()
        cls()
        return 0
        # 1940 IF Z*J>WRAGI THEN
        #   PRINT AT VAL "13",INT PI;"NO ATAKA OTBITA! uRA-A-A!!!"
    else:
        print("Но атака отбита! Ура-а-а!!!")
        # 1950 IF FN S(3)=SGN PI THEN
        #   PRINT AT VAL "15",INT PI;"pROIZO[LA RE[A\@]AQ BITWA!!!"
        if fn_s(3) == 1:
            print("Произошла решающая битва!!!")
        # 1960 LET POGIBZ=INT (WRAGI/3)+INT (RND*Z/6):
        #   LET POGIB=POGIB+POGIBZ:
        #   LET NAS=NAS-POGIB:
        #   LET RASST=25+FN S(20):
        #   LET WRAGI=INT (NAS/4)+INT (RND*NAS/5)
        pogibz = int(vragi / 3) + int(random() * z / 6)
        pogib += pogibz
        nas -= pogib
        rasst = 25 + fn_s(20)
        vragi = int(nas / 4) + int(random() * nas / 5)
        # 1965 GO TO KEY:
        #   GO SUB CLS
        key()
        cls()
        # 1970 RETURN