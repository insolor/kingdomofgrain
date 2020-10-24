from abstract_screen import AbstractScreen
from game_model import GameModel
from grain import empty_lines, sub_input


def guard(screen: AbstractScreen, model: GameModel):
    """Guard"""
    # 610 REM \#017\#001OHRANA\#017\#000
    while True:
        # 620 LET UBITO=NOT PI: LET Z=-1
        ubito = 0  # FIXME: Add to model?
        z = -1
        # 630 GO SUB PUS: PRINT AT VAL "20",VAL "5";"u NAS ";NAS;" ^ELOWEK"
        empty_lines(screen)
        screen.at(20, 5).print(f"У нас {model.nas} человек")

        # 640 PRINT AT VAL "21",INT PI;"sKOLXKO PO[LEM W WOJSKO?":
        #   GO SUB INPUT:
        #   LET Z=VAL F$:
        #   GO SUB PUS
        screen.at(21, 3).print("Сколько пошлём в войско?")
        z = int(sub_input(screen))
        empty_lines(screen)

        # 650 IF Z<NOT PI THEN GO TO VAL "620"
        if z < 0:
            continue

        # 660 IF Z>NAS THEN PRINT AT VAL "20",VAL "6";"u NAS MALO L\@DEJ!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "620"
        if z > model.nas:
            screen.at(20, 6).print("У нас мало людей!!!")
            key()
            empty_lines(screen)
            continue

        # 670 IF Z>INT (ZERNO/VAL "5") THEN
        #   PRINT AT VAL "20",SGN PI;"zERNA HWATIT NA ";INT (ZERNO/5);" WOINOW":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "620"
        if z > model.zerno // 5:
            screen.at(20, 1).print(f"Зерна хватит на {model.zerno // 5} воинов")
            key()
            empty_lines(screen)
            continue

        # 680 IF Z>NOT PI THEN
        #   LET OST=NAS-Z:
        #   LET ZERNO=ZERNO-Z*5:
        #   RETURN
        if z > 0:
            model.ost = model.nas - z
            model.zerno -= z * 5
        else:
            # 690 LET OST=NAS:
            #   RETURN
            model.ost = model.nas

        return
