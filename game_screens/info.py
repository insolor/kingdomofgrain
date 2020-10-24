from io_devices.abstract_io import AbstractIO
from game_model import GameModel
from grain import fn_s


def info(screen: AbstractIO, model: GameModel):
    """ИНФО"""
    # 300 REM \#017\#001INFO\#017\#000
    # 310 GO SUB CLS
    screen.cls()
    # 330 PRINT "\{i5}********************************"
    screen.ink(5).print("*" * 32)
    # 335 PRINT
    screen.print()
    # 340 INK VAL "6":
    #   PRINT AT VAL "2",VAL "8";TIME;" gOD PRAWLENIQ:":
    #   INK VAL "7"
    screen.ink(6).at(2, 8).print(f"{model.time} Год правления:").ink(7)
    # 350 IF BEV>BIN THEN PRINT ;"\{b0i7}w GOROD PRI[LO ";BEV;" BEVENCEW"
    if model.bezh > 0:
        screen.bright(0).ink(7).print(f'В город пришло {model.bezh} беженцев')
    # 360 PRINT "rODILOSX  ";ROD;" ^ELOWEK"
    screen.print(f'Родилось {model.rod} человек')
    # 370 PRINT "\{b0}uMERLO   ";UMER;" ^ELOWEK"
    screen.bright(0).print(f'Умерло   {model.umer} человек')
    # 380 IF UMERGOL>BIN THEN PRINT "OT gOLODA - ";UMERGOL;" ^ELOWEK"
    if model.umergol > 0:
        screen.print(f'От голода - {model.umergol} человек')
    # 390 IF POGIB>BIN THEN PRINT "\{b0}w BOQH POLEGLO ";POGIB;" ^ELOWEK"
    if model.pogib > 0:
        screen.bright(0).print(f'В боях полегло {model.pogib} человек')
    # 395 IF NAS<=BIN THEN LET NAS=SGN PI
    if model.nas <= 0:
        model.nas = 1
    # 400 PRINT "nASELENIE - ";NAS;" ^ELOWEK"
    screen.print(f"Население - {model.nas} человек")
    # 410 PRINT "\{b0}zEMLI - ";ZEML;" AKROW"
    screen.bright(0).print(f"Земли - {model.zeml} акров")
    # 420 PRINT "uROVAJ - ";UROV;" BU[/AKR"
    screen.print(f"Урожай - {model.urozh} буш/акр")
    # 430 IF KRYS>BIN THEN PRINT "kRYSY SOVRALI ";KRYS;" BU[."
    if model.krys > 0:
        screen.print(f"Крысы сожрали {model.krys} буш.")
    # 440 PRINT "\{b0}zAPASY ZERNA ";ZERNO;" BU[."
    screen.bright(0).print(f"Запасы зерна {model.zerno} буш.")
    # 450 PRINT "cENA ZEMLI ";CENA;" BU[/AKR"
    screen.print(f"Цена земли {model.cena} буш/акр")
    # 460 PRINT "\{b0}hLEBOROB ZASEWAET ";PROIZ;" AKROW"
    screen.bright(0).print(f"Хлебороб засевает {model.proiz} акров")
    # 470 LET I=25+FN S(10):
    #   IF RASST<I THEN PRINT "nAPADA\@T  ";WRAGI;" WOINOW":
    #       PRINT "ONI W ";RASST;" MILQH OT NAS!"
    i = 25 + fn_s(10)
    if model.rasst < i:
        screen.print(f"Нападают {model.vragi} воинов")
        screen.print(f"Они в {model.rasst} милях от нас!")
    # 475 PRINT
    # 480 PRINT "\{i5}********************************"
    screen.print()
    screen.print("*" * 32)
    # 490 RETURN
