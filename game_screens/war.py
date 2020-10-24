from random import random

from io_devices.abstract_io import AbstractIO
from game_model import GameModel
from grain import sub_input, empty_lines, fn_s

print = None


def hamony(device: AbstractIO, model: GameModel):
    # global nas, ost, zerno, zahv, srok
    # 960 REM \#017\#001hAMONIQ\#017\#000
    # 970 IF (OST<=BIN ) OR (ZERNO<=5) THEN
    #   LET POS=BIN :
    #   GO TO VAL "1030"
    if model.ost <= 0 or model.zerno < 5:
        pos = 0
    else:
        # 980 PRINT AT VAL "19",SGN PI;"u NAS ";OST;" NEZANQTYH L\@DEJ":
        #   PRINT AT VAL "20",BIN ;"zERNA HWATIT NA ";INT (ZERNO/5);" WOINOW"
        print("У нас %d незанятых людей" % ost)
        print("Зерна хватит на %d воинов" % (zerno / 5))
        while True:
            # 990 LET POS=-1: PRINT AT VAL "21",INT PI;"sKOLXKO PO[LEM W hAMONI\@?"
            pos = -1
            print("Сколько пошлём в Хамонию?")
            # 1000 GO SUB INPUT:
            #   LET POS=VAL F$:
            #   PRINT AT VAL "18",BIN ;S$:
            #   GO SUB PUS:
            #   IF POS<BIN THEN GO TO VAL "990"
            pos = int(sub_input())
            empty_lines()
            if pos < 0:
                continue
            # 1010 IF POS>OST THEN
            #   PRINT AT VAL "20",VAL "5";"u NAS MALO L\@DEJ!!!":
            #   GO SUB KEY:
            #   GO SUB PUS:
            #   GO TO VAL "990"
            if pos > ost:
                print("У нас мало людей!!!")
                key()
                empty_lines()
                continue
            # 1020 IF POS>INT (ZERNO/5) THEN
            #   PRINT AT VAL "20",VAL "6";"u NAS MALO ZERNA!!!":
            #   GO SUB KEY:
            #   GO SUB PUS:
            #   GO TO VAL "990"
            if pos * 5 > zerno:
                print("У нас мало зерна!!!")
                key()
                empty_lines()
                continue
            break
    # 1030 IF POS<=NOT PI THEN GO TO VAL "1070"
    if pos > 0:
        # 1040 LET NAS=NAS-POS: LET OST=OST-POS: LET ZERNO=ZERNO-POS*5
        nas -= pos
        ost -= pos
        zerno -= pos * 5
        # 1050 IF ZAHW>BIN THEN LET ZAHW=ZAHW+POS: GO TO VAL "1070"
        if zahv > 0:
            zahv += pos
        else:
            # 1060 LET ZAHW=POS: LET SROK=TIME+FN S(4)
            zahv = pos
            srok = time + fn_s(4)
    # 1070 IF ZAHW<=NOT PI THEN GO TO VAL "1140"
    if zahv <= 0:
        pass
    # 1080 IF SROK<>TIME THEN GO TO VAL "1140"
    elif srok != time:
        pass
    # 1090 IF ZAHW>NAS*VAL "2" THEN GO SUB POBEDA: GO TO VAL "1140"
    elif zahv > nas * 2:
        victory()
    # 1100 IF ZAHW<INT (NAS/VAL "2") THEN GO SUB PORAV: GO TO VAL "1140"
    elif zahv < nas // 2:
        defeat()
    # 1110 IF RND>0.5 THEN GO SUB POBEDA: GO TO VAL "1140"
    elif random() > 0.5:
        victory()
    # 1120 GO SUB PORAV
    else:
        defeat()
    # 1140 RETURN


def defeat(device: AbstractIO, model: GameModel):
    # global nas, pogib, zahv, ost
    # 1240 REM \#017\#001PORAVENIE\#017\#000
    # 1245 GO SUB CLS: RANDOMIZE USR VAL "54778"
    cls()
    # 1250 PRINT AT VAL "11",VAL "5";"\{i3}poravenie w hAMONII!!!"
    print("ПОРАЖЕНИЕ В Хамонии!!!")
    # 1260 LET UBITO=INT (ZAHW*(0.8+RND/5)):
    #   LET NAS=NAS+ZAHW-UBITO:
    #   LET POGIB=POGIB+UBITO
    ubito = int(zahv * (0.8 + random() / 5))
    nas += zahv - ubito
    pogib += ubito
    # 1270 PRINT AT VAL "13",SGN PI;"pOGIBLO - ";UBITO;" WOINOW"
    print("Погибло - %d воинов" % ubito)
    # 1280 LET ZAHW=BIN :
    #   LET OST=NAS-Z-INT (ZAS/PROIZ)
    zahv = 0
    ost = nas - z - int(zas / proiz)
    # 1285 GO SUB KEY: GO SUB CLS
    key()
    cls()
    # 1290 RETURN


def victory(device: AbstractIO, model: GameModel):
    # 1150 REM \#017\#001POBEDA\#017\#000
    # 1155 GO SUB CLS: RANDOMIZE USR VAL "54778"
    device.cls()
    # 1160 PRINT AT VAL "11",VAL "2";"\{i6}w hAMONII ODERVANA pobeda!!!"
    print("В хамонии одержана победа!!!")
    # 1170 LET T(INT PI)=INT (NAS*(RND/3+0.3)):
    #   LET T(SGN PI)=INT (ZAHW*(FN S(VAL "10")+VAL "4")):
    #   LET T(VAL "2")=INT (ZEML*(RND/VAL "2"+0.3)):
    #   LET NAS=NAS+T(INT PI):
    #   LET ZEML=ZEML+T(VAL "2"):
    #   LET ZERNO=ZERNO+T(SGN PI)
    captured_people = int(nas * (random() / 3 + 0.3))
    taken_grain = int(zahv * fn_s(10) + 4)
    annexed_territory = int(zeml * (random() / 2 + 0.3))
    nas += captured_people
    zeml += annexed_territory
    zerno += taken_grain

    # 1180 LET UBITO=INT (ZAHW*(RND/5+0.3)):
    #   LET POGIB=POGIB+UBITO:
    #   LET NAS=NAS+ZAHW-UBITO
    ubito = int(zahv*(random() / 5 + 0.3))
    pogib += ubito
    nas += zahv - ubito
    # 1190 PRINT AT VAL "13",BIN ;"u WRAGA ZAHWA^ENO:"
    print("У врага захвачено:")
    # 1200 PRINT AT VAL "14",SGN PI;"zERNA - ";T(1);" BU[ELEJ":
    #   PRINT " zEMLI - ";T(2);" AKROW": PRINT " pLENNYH - ";T(3);" ^ELOWEK"
    print("Зерна - %d бушелей" % taken_grain)
    print("Земли - %d акров" % annexed_territory)
    print("Пленных - %d человек" % captured_people)
    # 1210 PRINT AT VAL "18",VAL "6";"iZ ";ZAHW;" WOINOW ";UBITO;AT VAL "19",VAL "10";"PALO SMERTX\@ HRABRYH!"
    print("Из %d воинов %d пало сметрью храбрых!" % (zahv, ubito))
    # 1220 LET ZAHW=BIN :
    #   LET OST=NAS-Z-INT (ZAS/PROIZ)
    zahv = 0
    ost = nas - z - int(zas / proiz)
    # 1225 GO SUB KEY:
    #   GO SUB CLS
    key()
    cls()
    # 1230 RETURN