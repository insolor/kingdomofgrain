from io_devices.abstract_io import AbstractIO
from game_model import GameModel
from grain import sub_input, empty_lines
from game_screens.game_results import game_results


def feeding(screen: AbstractIO, model: GameModel):
    """Feeding"""
    # 700 REM \#017\#001KORMEVKA\#017\#000
    # 710 LET K=-1: IF OST<=NOT PI THEN RETURN
    k = -1
    if model.ost <= 0:
        return

    while True:
        # 720 PRINT AT VAL "20",SGN PI;"mOVNO DATX ";INT (ZERNO/OST);" BU[ NA ^ELOWEKA":
        #   PRINT AT VAL "21",VAL "6";"sKOLXKO DA[X?"
        screen.at(20, 1).print(f"Можно дать {model.zerno // model.ost} буш на человека")
        screen.at(21, 6).print("Сколько дать?")

        # 730 GO SUB INPUT:
        #   LET K=VAL F$:
        #   GO SUB PUS:
        #   IF K<BIN THEN :
        #       GO TO VAL "720"
        k = int(sub_input(screen))
        if k < 0:
            continue

        # 740 IF K*OST>ZERNO THEN
        #   PRINT AT VAL "20",INT PI;"u NAS NET STOLXKO ZERNA!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "720"
        if k * model.ost > model.zerno:
            screen.print("У нас нет столько зерна!!!")
            screen.key()
            continue

        # 750 LET ZERNO=ZERNO-K*OST
        model.zerno -= k * model.ost

        # 760 IF K<VAL "20" THEN
        #   LET UMERGOL=OST*INT (SGN PI-K/VAL "20"):
        #   LET UMERWSEGO=UMERWSEGO+UMERGOL:
        #   LET NAS=NAS-UMERGOL
        if k < 20:
            umergol = model.ost * int(1 - k / 20)
            model.umervsego += umergol
            model.nas -= umergol

        # 770 IF NAS<=NOT PI OR K=NOT PI THEN
        #   GO SUB CLS:
        #   RANDOMIZE USR VAL "53620":
        #   PRINT AT VAL "11",INT PI;"\{i2}ty UMORIL WSEH GOLODOM!!!":
        #   GO SUB KEY:
        #   LET OI=BIN :
        #   LET U=SGN PI:
        #   GO SUB OITOG:
        #   RETURN
        if model.nas <= 0 or k == 0:
            screen.cls()
            screen.at(11, 3).ink(2).print("Ты уморил всех голодом!!!")
            screen.key()
            model.u = 1
            game_results(screen, model, 0)
            return

        # 780 IF K<=VAL "10" THEN
        #   PRINT AT VAL "20",VAL "10";"\{i3}du{egub!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "800"
        if k <= 10:
            screen.at(10, 20).ink(3).print("ДУШЕГУБ!!!")
            screen.key()
            empty_lines(screen)

        # 790 IF K<=VAL "21" THEN
        #   PRINT AT VAL "20",VAL "10";"\{i5}vadina!!!":
        #   GO SUB KEY:
        #   GO SUB PUS
        elif k <= 21:
            screen.at(20, 10).ink(5).print("ЖАДИНА!!!")
            screen.key()
            empty_lines(screen)

        # 800 IF K>VAL "20" THEN
        #   LET UMERGOL=BIN
        elif k > 20:
            model.umergol = 0

        # 810 IF K>VAL "70" THEN
        #   PRINT AT VAL "20",BIN ;"\{i6}w..WY...wypx..pxem!!!za tebq!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "830"
        elif k > 70:
            screen.at(20, 0).ink(6).print("В..вы...ВЫПЬ..ПЬЕМ!!!ЗА ТЕБЯ!!!")
            screen.key()
            empty_lines(screen)

        # 820 IF K>VAL "50" THEN
        #   PRINT AT VAL "20",VAL "5";"\{i4}bLAGODETELX ty NA[!!!":
        #   GO SUB KEY:
        #   GO SUB PUS
        elif k > 50:
            screen.at(20, 5).ink(4).print("Благодетель ты НАШ!!!")
            screen.key()
            empty_lines(screen)
        # 830 RETURN
        return
