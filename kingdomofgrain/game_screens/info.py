from random import randint

from kingdomofgrain.game_model import GameModel
from kingdomofgrain.io_devices import AbstractIO


def info(device: AbstractIO, model: GameModel):
    # 300 REM \#017\#001INFO\#017\#000
    # 310 GO SUB CLS
    device.cls()
    # 330 PRINT "\{i5}********************************"
    device.ink(5).print("*" * 32)
    # 335 PRINT
    device.print()
    # 340 INK VAL "6":
    #   PRINT AT VAL "2",VAL "8";TIME;" gOD PRAWLENIQ:":
    #   INK VAL "7"
    device.ink(6).at(2, 8).print(f"{model.time} Год правления:").ink(7)
    # 350 IF BEV>BIN THEN PRINT ;"\{b0i7}w GOROD PRI[LO ";BEV;" BEVENCEW"
    if model.refugees > 0:
        device.bright(0).ink(7).print(f"В город пришло {model.refugees} беженцев")
    # 360 PRINT "rODILOSX  ";ROD;" ^ELOWEK"
    device.print(f"Родилось {model.born} человек")
    # 370 PRINT "\{b0}uMERLO   ";UMER;" ^ELOWEK"
    device.bright(0).print(f"Умерло   {model.dead_natural_cases} человек")
    # 380 IF UMERGOL>BIN THEN PRINT "OT gOLODA - ";UMERGOL;" ^ELOWEK"
    if model.dead_starvation > 0:
        device.print(f"От голода - {model.dead_starvation} человек")
    # 390 IF POGIB>BIN THEN PRINT "\{b0}w BOQH POLEGLO ";POGIB;" ^ELOWEK"
    if model.dead_in_battles > 0:
        device.bright(0).print(f"В боях полегло {model.dead_in_battles} человек")
    # 395 IF NAS<=BIN THEN LET NAS=SGN PI
    if model.population <= 0:
        model.population = 1
    # 400 PRINT "nASELENIE - ";NAS;" ^ELOWEK"
    device.print(f"Население - {model.population} человек")
    # 410 PRINT "\{b0}zEMLI - ";ZEML;" AKROW"
    device.bright(0).print(f"Земли - {model.land} акров")
    # 420 PRINT "uROVAJ - ";UROV;" BU[/AKR"
    device.print(f"Урожай - {model.grain_yield} буш/акр")
    # 430 IF KRYS>BIN THEN PRINT "kRYSY SOVRALI ";KRYS;" BU[."
    if model.rats > 0:
        device.print(f"Крысы сожрали {model.rats} буш.")
    # 440 PRINT "\{b0}zAPASY ZERNA ";ZERNO;" BU[."
    device.bright(0).print(f"Запасы зерна {model.grain} буш.")
    # 450 PRINT "cENA ZEMLI ";CENA;" BU[/AKR"
    device.print(f"Цена земли {model.land_price} буш/акр")
    # 460 PRINT "\{b0}hLEBOROB ZASEWAET ";PROIZ;" AKROW"
    device.bright(0).print(f"Хлебороб засевает {model.sower_productivity} акров")
    # 470 LET I=25+FN S(10):
    #   IF RASST<I THEN PRINT "nAPADA\@T  ";WRAGI;" WOINOW":
    #       PRINT "ONI W ";RASST;" MILQH OT NAS!"
    i = randint(25, 35)
    if model.distance_to_enemies < i:
        device.print(f"Нападают {model.enemies} воинов")
        device.print(f"Они в {model.distance_to_enemies} милях от нас!")
    # 475 PRINT
    # 480 PRINT "\{i5}********************************"
    device.print()
    device.ink(5).print("*" * 32)
    # 490 RETURN
