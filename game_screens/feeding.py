from end_game_exception import EndGameException
from game_model import GameModel
from grain import sub_input, empty_lines
from io_devices import AbstractIO


def feeding(device: AbstractIO, model: GameModel):
    # 700 REM \#017\#001KORMEVKA\#017\#000
    # 710 LET K=-1: IF OST<=NOT PI THEN RETURN
    if model.ost <= 0:
        return

    while True:
        # 720 PRINT AT VAL "20",SGN PI;"mOVNO DATX ";INT (ZERNO/OST);" BU[ NA ^ELOWEKA":
        #   PRINT AT VAL "21",VAL "6";"sKOLXKO DA[X?"
        device.at(20, 1).print(f"Можно дать {model.grain // model.ost} буш на человека")
        device.at(21, 6).print("Сколько дать?")

        # 730 GO SUB INPUT:
        #   LET K=VAL F$:
        #   GO SUB PUS:
        #   IF K<BIN THEN :
        #       GO TO VAL "720"
        try:
            model.feeding_per_worker = int(sub_input(device, model))
        except ValueError:
            continue

        # 740 IF K*OST>ZERNO THEN
        #   PRINT AT VAL "20",INT PI;"u NAS NET STOLXKO ZERNA!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   GO TO VAL "720"
        if model.feeding_per_worker * model.ost > model.grain:
            device.print("У нас нет столько зерна!!!")
            device.wait_key()
            continue

        break

    # 750 LET ZERNO=ZERNO-K*OST
    model.grain -= model.feeding_per_worker * model.ost

    # 760 IF K<VAL "20" THEN
    #   LET UMERGOL=OST*INT (SGN PI-K/VAL "20"):
    #   LET UMERWSEGO=UMERWSEGO+UMERGOL:
    #   LET NAS=NAS-UMERGOL
    if model.feeding_per_worker < 20:
        model.dead_starvation = model.ost * (1 - model.feeding_per_worker // 20)
        model.dead_total += model.dead_starvation
        model.population -= model.dead_starvation

    # 770 IF NAS<=NOT PI OR K=NOT PI THEN
    #   GO SUB CLS:
    #   RANDOMIZE USR VAL "53620":
    #   PRINT AT VAL "11",INT PI;"\{i2}ty UMORIL WSEH GOLODOM!!!":
    #   GO SUB KEY:
    #   LET OI=BIN :
    #   LET U=SGN PI:
    #   GO SUB OITOG:
    #   RETURN
    if model.population <= 0 or model.feeding_per_worker == 0:
        device.cls()
        device.show_image("graveyard")
        device.at(11, 3).ink(2).print("Ты уморил всех голодом!!!")
        device.wait_key()
        raise EndGameException(False)

    # 780 IF K<=VAL "10" THEN
    #   PRINT AT VAL "20",VAL "10";"\{i3}du{egub!!!":
    #   GO SUB KEY:
    #   GO SUB PUS:
    #   GO TO VAL "800"
    if model.feeding_per_worker <= 10:
        device.at(10, 20).ink(3).print("ДУШЕГУБ!!!")
        device.wait_key()
        empty_lines(device)

    # 790 IF K<=VAL "21" THEN
    #   PRINT AT VAL "20",VAL "10";"\{i5}vadina!!!":
    #   GO SUB KEY:
    #   GO SUB PUS
    elif model.feeding_per_worker <= 21:
        device.at(20, 10).ink(5).print("ЖАДИНА!!!")
        device.wait_key()
        empty_lines(device)

    # 800 IF K>VAL "20" THEN
    #   LET UMERGOL=BIN
    elif model.feeding_per_worker > 20:
        model.dead_starvation = 0

    # 810 IF K>VAL "70" THEN
    #   PRINT AT VAL "20",BIN ;"\{i6}w..WY...wypx..pxem!!!za tebq!!!":
    #   GO SUB KEY:
    #   GO SUB PUS:
    #   GO TO VAL "830"
    elif model.feeding_per_worker > 70:
        device.at(20, 0).ink(6).print("В..вы...ВЫПЬ..ПЬЕМ!!!ЗА ТЕБЯ!!!")
        device.wait_key()
        empty_lines(device)

    # 820 IF K>VAL "50" THEN
    #   PRINT AT VAL "20",VAL "5";"\{i4}bLAGODETELX ty NA[!!!":
    #   GO SUB KEY:
    #   GO SUB PUS
    elif model.feeding_per_worker > 50:
        device.at(20, 5).ink(4).print("Благодетель ты НАШ!!!")
        device.wait_key()
        empty_lines(device)
    # 830 RETURN
