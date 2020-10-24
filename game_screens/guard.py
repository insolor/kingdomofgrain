from io_devices import AbstractIO
from game_model import GameModel
from grain import empty_lines, sub_input


def guard(device: AbstractIO, model: GameModel):
    """Guard"""
    # 610 REM \#017\#001OHRANA\#017\#000
    while True:
        # 620 LET UBITO=NOT PI: LET Z=-1
        ubito = 0  # FIXME: Add to model?
        model.z = -1
        # 630 GO SUB PUS: PRINT AT VAL "20",VAL "5";"u NAS ";NAS;" ^ELOWEK"
        empty_lines(device)
        device.at(20, 5).print(f"У нас {model.nas} человек")

        # 640 PRINT AT VAL "21",INT PI;"sKOLXKO PO[LEM W WOJSKO?":
        #   GO SUB INPUT:
        #   LET Z=VAL F$:
        #   GO SUB PUS
        device.at(21, 3).print("Сколько пошлём в войско?")
        model.z = int(sub_input(device, model))
        empty_lines(device)

        # 650 IF Z<NOT PI THEN GO TO VAL "620"
        if model.z < 0:
            continue

        # 660 IF Z>NAS THEN PRINT AT VAL "20",VAL "6";"u NAS MALO L\@DEJ!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "620"
        if model.z > model.nas:
            device.at(20, 6).print("У нас мало людей!!!")
            device.key()
            empty_lines(device)
            continue

        # 670 IF Z>INT (ZERNO/VAL "5") THEN
        #   PRINT AT VAL "20",SGN PI;"zERNA HWATIT NA ";INT (ZERNO/5);" WOINOW":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "620"
        if model.z > model.zerno // 5:
            device.at(20, 1).print(f"Зерна хватит на {model.zerno // 5} воинов")
            device.key()
            empty_lines(device)
            continue

        # 680 IF Z>NOT PI THEN
        #   LET OST=NAS-Z:
        #   LET ZERNO=ZERNO-Z*5:
        #   RETURN
        if model.z > 0:
            model.ost = model.nas - model.z
            model.zerno -= model.z * 5
        else:
            # 690 LET OST=NAS:
            #   RETURN
            model.ost = model.nas

        return
