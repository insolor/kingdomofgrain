from ..game_model import GameModel
from ..io_devices import AbstractIO
from ..utils import sub_input, empty_lines


def purchase_land(device: AbstractIO, model: GameModel):
    while True:
        # 510 LET ZEM=-1: PRINT AT VAL "20",VAL "5";"sKOLXKO KUPIM ZEMLI?"
        device.at(20, 5).print("Сколько купим земли?")

        # 520 GO SUB INPUT:
        #   LET ZEM=VAL F$:
        #   GO SUB PUS:
        #   IF ZEM<BIN THEN GO TO VAL "510"
        try:
            zem = int(sub_input(device, model))
        except ValueError:
            zem = -1

        empty_lines(device)
        if zem < 0:
            continue

        # 530 IF CENA*ZEM>ZERNO THEN PRINT AT VAL "20",BIN ;"u NAS TOLXKO ";ZERNO;" BU[ELEJ ZERNA!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "510"
        if model.land_price * zem > model.grain:
            device.print(f"У нас только {model.grain} бушелей зерна!!!")
            device.wait_key()
            empty_lines(device)
            continue

        # 540 LET ZEML=ZEML+ZEM:
        #   LET ZERNO=ZERNO-CENA*ZEM
        model.land += zem
        model.grain -= model.land_price * zem

        # 550 PRINT AT VAL "20",SGN PI;"u NAS ";ZERNO;" BU[ELEJ ZERNA":
        #   GO SUB KEY:
        #   GO SUB PUS
        device.at(20, 1).print(f"У нас {model.grain} бушелей зерна")
        device.wait_key()
        empty_lines(device)
        break


def sell_land(device: AbstractIO, model: GameModel):
    while True:
        # 560 LET ZEM=-1:
        #   PRINT AT VAL "20",VAL "4";"sKOLXKO ZEMLI PRODADIM?"
        device.at(20, 4).print("Сколько земли продадим?")

        # 570 GO SUB INPUT: LET ZEM=VAL F$: IF ZEM<BIN THEN GO TO VAL "560"
        try:
            zem = int(sub_input(device, model))
        except ValueError:
            continue

        # 580 IF ZEM>ZEML THEN PRINT AT VAL "20",BIN ;"u NAS TOLXKO ";ZEML;" AKROW ZEMLI!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "560"
        if zem > model.land:
            device.at(20, 0).print(f"У нас только {model.land} акров земли!!!")
            device.wait_key()
            empty_lines(device)
            continue

        # 590 LET ZEML=ZEML-ZEM: LET ZERNO=ZERNO+ZEM*CENA
        model.land -= zem
        model.grain += zem * model.land_price
        # 600 RETURN
        break


def barter(device: AbstractIO, model: GameModel):
    # 500 REM \#017\#001TORGOWLQ\#017\#000
    purchase_land(device, model)
    sell_land(device, model)
