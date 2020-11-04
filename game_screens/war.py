from random import random

from io_devices import AbstractIO
from game_model import GameModel
from grain import sub_input, empty_lines, randint


def war(device: AbstractIO, model: GameModel):
    # 960 REM \#017\#001hAMONIQ\#017\#000
    # 970 IF (OST<=BIN ) OR (ZERNO<=5) THEN
    #   LET POS=BIN :
    #   GO TO VAL "1030"
    if model.ost <= 0 or model.zerno < 5:
        pos = 0
    else:
        # 980 PRINT AT VAL "19",SGN PI;"u NAS ";OST;" NEZANQTYH L\@DEJ":
        #   PRINT AT VAL "20",BIN ;"zERNA HWATIT NA ";INT (ZERNO/5);" WOINOW"
        device.at(12, 1).print(f"У нас {model.ost} незанятых людей")
        device.at(20, 0).print(f"Зерна хватит на {model.zerno // 5} воинов")
        while True:
            # 990 LET POS=-1: PRINT AT VAL "21",INT PI;"sKOLXKO PO[LEM W hAMONI\@?"
            device.at(21, 1).print("Сколько пошлём в Хамонию?")

            # 1000 GO SUB INPUT:
            #   LET POS=VAL F$:
            #   PRINT AT VAL "18",BIN ;S$:
            #   GO SUB PUS:
            #   IF POS<BIN THEN GO TO VAL "990"
            try:
                pos = int(sub_input(device, model))
            except ValueError:
                pos = -1

            device.at(18, 0).print(64 * " ")
            empty_lines(device)

            if pos < 0:
                continue

            # 1010 IF POS>OST THEN
            #   PRINT AT VAL "20",VAL "5";"u NAS MALO L\@DEJ!!!":
            #   GO SUB KEY:
            #   GO SUB PUS:
            #   GO TO VAL "990"
            if pos > model.ost:
                device.at(20, 5).print("У нас мало людей!!!")
                device.key()
                empty_lines(device)
                continue

            # 1020 IF POS>INT (ZERNO/5) THEN
            #   PRINT AT VAL "20",VAL "6";"u NAS MALO ZERNA!!!":
            #   GO SUB KEY:
            #   GO SUB PUS:
            #   GO TO VAL "990"
            if pos * 5 > model.zerno:
                device.at(20, 6).print("У нас мало зерна!!!")
                device.key()
                empty_lines(device)
                continue

            break

    # 1030 IF POS<=NOT PI THEN GO TO VAL "1070"
    if pos > 0:
        # 1040 LET NAS=NAS-POS: LET OST=OST-POS: LET ZERNO=ZERNO-POS*5
        model.nas -= pos
        model.ost -= pos
        model.zerno -= pos * 5

        # 1050 IF ZAHW>BIN THEN LET ZAHW=ZAHW+POS: GO TO VAL "1070"
        if model.zahv > 0:
            model.zahv += pos
        else:
            # 1060 LET ZAHW=POS: LET SROK=TIME+FN S(4)
            model.zahv = pos
            model.srok = model.time + randint(4)

    # 1070 IF ZAHW<=NOT PI THEN GO TO VAL "1140"
    # 1080 IF SROK<>TIME THEN GO TO VAL "1140"
    if model.zahv > 0 and model.srok == model.time:
        # 1090 IF ZAHW>NAS*VAL "2" THEN GO SUB POBEDA: GO TO VAL "1140"
        if model.zahv > model.nas * 2:
            victory(device, model)
        # 1100 IF ZAHW<INT (NAS/VAL "2") THEN GO SUB PORAV: GO TO VAL "1140"
        elif model.zahv < model.nas // 2:
            defeat(device, model)
        # 1110 IF RND>0.5 THEN GO SUB POBEDA: GO TO VAL "1140"
        elif random() > 0.5:
            victory(device, model)
        # 1120 GO SUB PORAV
        else:
            defeat(device, model)

    # 1140 RETURN


def defeat(device: AbstractIO, model: GameModel):
    # 1240 REM \#017\#001PORAVENIE\#017\#000
    # 1245 GO SUB CLS: RANDOMIZE USR VAL "54778"
    device.cls()

    # 1250 PRINT AT VAL "11",VAL "5";"\{i3}poravenie w hAMONII!!!"
    device.at(11, 5).ink(3).print("ПОРАЖЕНИЕ В Хамонии!!!")

    # 1260 LET UBITO=INT (ZAHW*(0.8+RND/5)):
    #   LET NAS=NAS+ZAHW-UBITO:
    #   LET POGIB=POGIB+UBITO
    ubito = int(model.zahv * (0.8 + random() / 5))
    model.nas += model.zahv - ubito
    model.pogib += ubito

    # 1270 PRINT AT VAL "13",SGN PI;"pOGIBLO - ";UBITO;" WOINOW"
    device.at(13, 1).print(f"Погибло - {ubito} воинов")

    # 1280 LET ZAHW=BIN :
    #   LET OST=NAS-Z-INT (ZAS/PROIZ)
    model.zahv = 0
    model.ost = model.nas - model.z - model.zas // model.proiz

    # 1285 GO SUB KEY: GO SUB CLS
    device.key()
    device.cls()

    # 1290 RETURN


def victory(device: AbstractIO, model: GameModel):
    # 1150 REM \#017\#001POBEDA\#017\#000
    # 1155 GO SUB CLS: RANDOMIZE USR VAL "54778"
    device.cls()

    # 1160 PRINT AT VAL "11",VAL "2";"\{i6}w hAMONII ODERVANA pobeda!!!"
    device.at(11, 2).ink(6).print("В хамонии одержана победа!!!")

    # 1170 LET T(INT PI)=INT (NAS*(RND/3+0.3)):
    #   LET T(SGN PI)=INT (ZAHW*(FN S(VAL "10")+VAL "4")):
    #   LET T(VAL "2")=INT (ZEML*(RND/VAL "2"+0.3)):
    #   LET NAS=NAS+T(INT PI):
    #   LET ZEML=ZEML+T(VAL "2"):
    #   LET ZERNO=ZERNO+T(SGN PI)

    captured_people = int(model.nas * (random() / 3 + 0.3))
    taken_grain = int(model.zahv * randint(10) + 4)
    annexed_territory = int(model.zeml * (random() / 2 + 0.3))

    model.nas += captured_people
    model.zeml += annexed_territory
    model.zerno += taken_grain

    # 1180 LET UBITO=INT (ZAHW*(RND/5+0.3)):
    #   LET POGIB=POGIB+UBITO:
    #   LET NAS=NAS+ZAHW-UBITO
    ubito = int(model.zahv * (random() / 5 + 0.3))
    model.pogib += ubito
    model.nas += model.zahv - ubito

    # 1190 PRINT AT VAL "13",BIN ;"u WRAGA ZAHWA^ENO:"
    device.at(13, 0).print("У врага захвачено:")

    # 1200 PRINT AT VAL "14",SGN PI;"zERNA - ";T(1);" BU[ELEJ":
    #   PRINT " zEMLI - ";T(2);" AKROW": PRINT " pLENNYH - ";T(3);" ^ELOWEK"
    device.at(14, 1).print(f"Зерна - {taken_grain} бушелей")
    device.print(f"Земли - {annexed_territory} акров")
    device.print(f"Пленных - {captured_people} человек")

    # 1210 PRINT AT VAL "18",VAL "6";"iZ ";ZAHW;" WOINOW ";UBITO;AT VAL "19",VAL "10";"PALO SMERTX\@ HRABRYH!"
    device.at(18, 6).print(f"Из {model.zahv} воинов {ubito} пало сметрью храбрых!")

    # 1220 LET ZAHW=BIN :
    #   LET OST=NAS-Z-INT (ZAS/PROIZ)
    model.zahv = 0
    model.ost = model.nas - model.z - int(model.zas / model.proiz)

    # 1225 GO SUB KEY:
    #   GO SUB CLS
    device.key()
    device.cls()

    # 1230 RETURN
