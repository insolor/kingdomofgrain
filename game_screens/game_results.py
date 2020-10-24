from io_devices import AbstractIO
from game_model import GameModel


def game_results(device: AbstractIO, model: GameModel, oi):
    # 1980 REM \#017\#001OITOG\#017\#000
    # 1985 GO SUB CLS
    cls()
    # 1987 RANDOMIZE USR VAL "64042"
    # 1990 IF OI=SGN PI THEN
    #   PRINT AT VAL "8",INT PI;"\{i5}wA[E PRAWLENIE OKON^ENO!!!\{i7}";
    #       AT VAL "10",VAL "2";"wY UPRAWLQLI STRANOJ ";TIME;" LET":
    #   PRINT " zA \\TO WREMQ UMERLO OT GOLODA";
    #       AT VAL "12",VAL "8";UMERWSEGO;" ^ELOWEK"
    if oi == 1:
        print("Ваше правление окончено!!!")
        print("Вы управляли страной %d лет" % time)
        print("За это время умерло от голода %d человек" % umervsego)
    # 2000 LET BOG=ZEML*CENA+ZERNO
    bog = zeml * cena + zerno
    # 2010 IF (BOG>NBOG) AND (OI=1) THEN
    #   PRINT AT VAL "14",BIN ;"wY UWELI^ILI BOGATSTWO W ";INT (BOG/NBOG);" RAZ!":
    #       GO TO VAL "2030"
    if oi == 1:
        if bog > nbog:
            print("Вы увеличили богатство в %d раз!" % int(bog / nbog))
        # 2020 IF OI=SGN PI THEN
        #   PRINT AT VAL "14",VAL "5";"wY RAZORILI STRANU!!!"
        else:
            print("Вы разорили страну!!!")
    # 2030 IF OI=SGN PI THEN
    #   PRINT AT VAL "17",VAL "7";"\{i4}do swidaniq!!!":
    #   GO TO VAL "2045"
    if oi == 1:
        print("До свидания!!!")
    # 2040 IF OI=BIN THEN
    #   PRINT AT VAL "9",BIN ;"\{i2}tAKIH NADO GNATX IZ PRAWITELEJ!!";
    #       AT VAL "11",SGN PI;"wY EDWA PRODERVALISX U WLASTI";
    #       AT VAL "12",VAL "10";TIME;" LET":
    #   PRINT AT VAL "14",BIN ;"\{i2}I UMORILI GOLODOM ";UMERWSEGO;" ^ELOWEK":
    #   PRINT AT VAL "16",VAL "5";"\{i2}kUDA \\TO GODITSQ?!"
    else:
        print("Таких надо гнать из правителей!!")
        print("Вы едва продержались у власти %d лет" % time)
        if umervsego > 0:
            print("и уморили голодом %d человек" % umervsego)
        print("Куда это годится?!")
    key()
    # 2045 GO SUB KEY
    # 2050 RETURN
    pass