from io_devices import AbstractIO
from game_model import GameModel
from grain import fn_s


def info(device: AbstractIO, model: GameModel):
    """ИНФО"""
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
    if model.bezh > 0:
        device.bright(0).ink(7).print(f'В город пришло {model.bezh} беженцев')
    # 360 PRINT "rODILOSX  ";ROD;" ^ELOWEK"
    device.print(f'Родилось {model.rod} человек')
    # 370 PRINT "\{b0}uMERLO   ";UMER;" ^ELOWEK"
    device.bright(0).print(f'Умерло   {model.umer} человек')
    # 380 IF UMERGOL>BIN THEN PRINT "OT gOLODA - ";UMERGOL;" ^ELOWEK"
    if model.umergol > 0:
        device.print(f'От голода - {model.umergol} человек')
    # 390 IF POGIB>BIN THEN PRINT "\{b0}w BOQH POLEGLO ";POGIB;" ^ELOWEK"
    if model.pogib > 0:
        device.bright(0).print(f'В боях полегло {model.pogib} человек')
    # 395 IF NAS<=BIN THEN LET NAS=SGN PI
    if model.nas <= 0:
        model.nas = 1
    # 400 PRINT "nASELENIE - ";NAS;" ^ELOWEK"
    device.print(f"Население - {model.nas} человек")
    # 410 PRINT "\{b0}zEMLI - ";ZEML;" AKROW"
    device.bright(0).print(f"Земли - {model.zeml} акров")
    # 420 PRINT "uROVAJ - ";UROV;" BU[/AKR"
    device.print(f"Урожай - {model.urozh} буш/акр")
    # 430 IF KRYS>BIN THEN PRINT "kRYSY SOVRALI ";KRYS;" BU[."
    if model.krys > 0:
        device.print(f"Крысы сожрали {model.krys} буш.")
    # 440 PRINT "\{b0}zAPASY ZERNA ";ZERNO;" BU[."
    device.bright(0).print(f"Запасы зерна {model.zerno} буш.")
    # 450 PRINT "cENA ZEMLI ";CENA;" BU[/AKR"
    device.print(f"Цена земли {model.cena} буш/акр")
    # 460 PRINT "\{b0}hLEBOROB ZASEWAET ";PROIZ;" AKROW"
    device.bright(0).print(f"Хлебороб засевает {model.proiz} акров")
    # 470 LET I=25+FN S(10):
    #   IF RASST<I THEN PRINT "nAPADA\@T  ";WRAGI;" WOINOW":
    #       PRINT "ONI W ";RASST;" MILQH OT NAS!"
    i = 25 + fn_s(10)
    if model.rasst < i:
        device.print(f"Нападают {model.vragi} воинов")
        device.print(f"Они в {model.rasst} милях от нас!")
    # 475 PRINT
    # 480 PRINT "\{i5}********************************"
    device.print()
    device.print("*" * 32)
    # 490 RETURN