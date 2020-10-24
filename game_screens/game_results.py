from io_devices import AbstractIO
from game_model import GameModel


def game_results(device: AbstractIO, model: GameModel, oi: bool):
    # 1980 REM \#017\#001OITOG\#017\#000
    # 1985 GO SUB CLS
    device.cls()

    # 1987 RANDOMIZE USR VAL "64042"

    # 1990 IF OI=SGN PI THEN
    #   PRINT AT VAL "8",INT PI;"\{i5}wA[E PRAWLENIE OKON^ENO!!!\{i7}";
    #       AT VAL "10",VAL "2";"wY UPRAWLQLI STRANOJ ";TIME;" LET":
    #   PRINT " zA \\TO WREMQ UMERLO OT GOLODA";
    #       AT VAL "12",VAL "8";UMERWSEGO;" ^ELOWEK"
    if oi:
        device.at(8, 3).ink(5).print("Ваше правление окончено!!!").ink(7)
        device.at(10, 2).print(f"Вы управляли страной {model.time} лет")
        device.print(" За это время умерло от голода ")
        device.at(12, 8).print(f"{model.umervsego} человек")

    # 2000 LET BOG=ZEML*CENA+ZERNO
    bog = model.zeml * model.cena + model.zerno

    # 2010 IF (BOG>NBOG) AND (OI=1) THEN
    #   PRINT AT VAL "14",BIN ;"wY UWELI^ILI BOGATSTWO W ";INT (BOG/NBOG);" RAZ!":
    #       GO TO VAL "2030"
    if oi:
        if bog > model.nbog:
            device.at(14, 0).print(f"Вы увеличили богатство в {bog // model.nbog} раз!")
        # 2020 IF OI=SGN PI THEN
        #   PRINT AT VAL "14",VAL "5";"wY RAZORILI STRANU!!!"
        else:
            device.at(14, 5).print("Вы разорили страну!!!")

    # 2030 IF OI=SGN PI THEN
    #   PRINT AT VAL "17",VAL "7";"\{i4}do swidaniq!!!":
    #   GO TO VAL "2045"
    if oi:
        device.at(17, 7).ink(4).print("До свидания!!!")

    # 2040 IF OI=BIN THEN
    #   PRINT AT VAL "9",BIN ;"\{i2}tAKIH NADO GNATX IZ PRAWITELEJ!!";
    #       AT VAL "11",SGN PI;"wY EDWA PRODERVALISX U WLASTI";
    #       AT VAL "12",VAL "10";TIME;" LET":
    #   PRINT AT VAL "14",BIN ;"\{i2}I UMORILI GOLODOM ";UMERWSEGO;" ^ELOWEK":
    #   PRINT AT VAL "16",VAL "5";"\{i2}kUDA \\TO GODITSQ?!"
    else:
        device.at(9, 0).ink(2).print("Таких надо гнать из правителей!!")
        device.at(12, 1).print("Вы едва продержались у власти")
        device.at(12, 10).print(f"{model.time} лет")
        if model.umervsego > 0:
            device.at(14, 0).ink(2).print(f"и уморили голодом {model.umervsego} человек")
        device.at(16, 5).ink(2).print("Куда это годится?!")

    # 2045 GO SUB KEY
    device.key()
    # 2050 RETURN
