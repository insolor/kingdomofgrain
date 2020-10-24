from io_devices.abstract_io import AbstractIO
from game_model import GameModel
from grain import sub_input, empty_lines


def purchase_land(screen: AbstractIO, model: GameModel):
    while True:
        # 510 LET ZEM=-1: PRINT AT VAL "20",VAL "5";"sKOLXKO KUPIM ZEMLI?"
        zem = -1
        screen.at(20, 5).print("Сколько купим земли?")

        # 520 GO SUB INPUT:
        #   LET ZEM=VAL F$:
        #   GO SUB PUS:
        #   IF ZEM<BIN THEN GO TO VAL "510"
        zem = int(sub_input())
        empty_lines(screen)
        if zem < 0:
            continue

        # 530 IF CENA*ZEM>ZERNO THEN PRINT AT VAL "20",BIN ;"u NAS TOLXKO ";ZERNO;" BU[ELEJ ZERNA!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "510"
        if model.cena * zem > model.zerno:
            screen.print(f"У нас только {model.zerno} бушелей зерна!!!")
            key()
            empty_lines(screen)
            continue

        # 540 LET ZEML=ZEML+ZEM:
        #   LET ZERNO=ZERNO-CENA*ZEM
        model.zeml += zem
        model.zerno -= model.cena * zem

        # 550 PRINT AT VAL "20",SGN PI;"u NAS ";ZERNO;" BU[ELEJ ZERNA":
        #   GO SUB KEY:
        #   GO SUB PUS
        screen.at(20, 1).print(f"У нас {model.zerno} бушелей зерна")
        key()
        empty_lines(screen)
        break


def sell_land(screen: AbstractIO, model: GameModel):
    while True:
        # 560 LET ZEM=-1:
        #   PRINT AT VAL "20",VAL "4";"sKOLXKO ZEMLI PRODADIM?"
        zem = -1
        screen.at(20, 4).print("Сколько земли продадим?")

        # 570 GO SUB INPUT: LET ZEM=VAL F$: IF ZEM<BIN THEN GO TO VAL "560"
        zem = int(sub_input())
        if zem < 0:
            continue

        # 580 IF ZEM>ZEML THEN PRINT AT VAL "20",BIN ;"u NAS TOLXKO ";ZEML;" AKROW ZEMLI!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "560"
        if zem > model.zeml:
            screen.at(20, 0).print(f"У нас только {model.zeml} акров земли!!!")
            key()
            empty_lines(screen)
            continue

        # 590 LET ZEML=ZEML-ZEM: LET ZERNO=ZERNO+ZEM*CENA
        model.zeml -= zem
        model.zerno += zem * model.cena
        # 600 RETURN
        break


def barter(screen: AbstractIO, model: GameModel):
    """Barter"""
    # 500 REM \#017\#001TORGOWLQ\#017\#000
    purchase_land(screen, model)
    sell_land(screen, model)