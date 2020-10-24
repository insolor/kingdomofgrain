from random import random

from io_devices import AbstractIO
from game_model import GameModel
from grain import randint


def nn(device: AbstractIO, model: GameModel):
    # 1550 REM \#017\#001NN\#017\#000
    # 1555 GO SUB CLS
    cls()
    # 1560 LET BEV=INT (RND*INT (NAS/4))
    bezh = int(random() * (model.nas // 4))
    # 1570 IF (RASST<20) AND (RND>.5) THEN
    #   LET BEV=BEV+INT (RND*BEV):
    #   PRINT AT VAL "11",INT PI;"pRITOK BEVENCEW SPASA\@]IHSQ";AT VAL "12",VAL "7";"OT ZAHWAT^IKOW!!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if rasst < 20 and random() > 0.5:
        bezh += int(random() * bezh)
        print("Приток беженцев, спасающихся\nот захватчиков!!!")
        key()
        cls()
    # 1580 LET NAS=NAS+BEV
    model.nas += bezh
    # 1590 IF (K<10) OR (UMERWSEGO>NAS*10) THEN
    #   RANDOMIZE USR VAL "55936": PRINT AT VAL "11",SGN PI;"nAROD WOSSTAL PROTIW TIRANA!!!":
    #   GO SUB KEY:
    #   GO SUB CLS:
    #   GO TO VAL "1610"
    if k < 10 or umervsego > nas * 10:
        print("Народ восстал против тирана!!!")
        key()
        cls()
        # 1610 IF (Z>(NAS-Z)/3) AND (Z<UMERGOL) THEN
        #   RANDOMIZE USR "54778":
        #   PRINT AT VAL "11",SGN PI;"nO WOJSKA PODAWILI WOSSTANIE!":
        #   LET WOSST=(NAS-Z)*INT (RND/5+0.1):
        #   LET POGIB=POGIB+WOSST:
        #   LET NAS=NAS-WOSST:
        #   PRINT AT VAL "12",VAL "5";"w ULI^NYH BOQH POLEGLO";AT VAL "13",VAL "8";WOSST;" VITELEJ":
        #   GO SUB KEY:
        #   GO SUB CLS:
        #   GO TO VAL "1630"
        if z > (nas - z) / 3 and z < umergol:
            print("Но войска подавили восстание!")
            vosst = (nas - z) * int(random() / 5 + 0.1)
            pogib += vosst
            nas -= vosst
            print("В уличных боях полегло %d жителей" % vosst)
            key()
            cls()
        else:
            # 1620 PRINT AT VAL "11",VAL "4";"wOJSKA PERE[LI NA STORONU";AT VAL "12",VAL "6";"WOSSTAW[EGO NARODA":
            #   PRINT AT VAL "14",VAL "5";"\{i4}monarhiq swergnuta!!!":
            #   GO SUB KEY:
            #   GO SUB CLS:
            #   LET U=SGN PI:
            #   LET OI=BIN :
            #   GO SUB OITOG:
            #   RETURN
            print("Войска перешли на сторону\nвосставшего народа")
            print("МОНАРХИЯ СВЕРГНУТА!!!")
            key()
            cls()
            return 0
    # 1600 GO TO VAL "1630"
    # 1630 LET UMER=UMER+INT (RND*2.5/100*NAS):
    #   LET ROD=INT (RND*(4+K/20)/100*NAS)
    umer += int(random() * 2.5 / 100 * nas)
    rod = int(random() * (4 + k / 20) / 100 * nas)
    # 1640 IF FN S(VAL "12")=SGN PI THEN
    #   LET CHUMA=INT (RND*50+VAL "5"):
    #   RANDOMIZE USR VAL "53620":
    #   PRINT AT VAL "11",INT PI;"~UMA UNESLA ";CHUMA;"% NASELENIQ!":
    #   LET UMER=UMER+INT (NAS*CHUMA/100):
    #   GO SUB KEY:
    #   GO SUB CLS
    if randint(12) == 1:
        chuma = int(random() * 50 + 5)
        print("Чума унесла %d%% населения!" % chuma)
        umer += int(nas * chuma / 100)
        key()
        cls()
    # 1650 IF FN S(VAL "100")<VAL "5" THEN
    #   RANDOMIZE USR VAL "46225":
    #   PRINT AT VAL "11",VAL "4";"dEMOGRAFI^ESKIJ WZRYW!!!":
    #   LET DEM=INT ((RND/VAL "2"+0.5)*NAS):
    #   LET ROD=ROD+DEM:
    #   GO SUB KEY:
    #   GO SUB CLS
    if randint(100) < 5:
        print("Демографический взрыв!!!")
        dem = int((random() / 2 + 0.5) * nas)
        rod += dem
        key()
        cls()
    # 1660 IF (FN S(VAL "20"))=VAL "5" THEN
    #   RANDOMIZE USR VAL "52462":
    #   PRINT AT VAL "11",VAL "6";"\{i2}pova - a - a - ar!!!":
    #   LET SGOR=INT (NAS*(RND/3+0.3)):
    #   LET SGORZER=INT (ZERNO*(RND/4+0.1)):
    #   GO SUB KEY:
    #   GO SUB CLS:
    #   GO TO VAL "1666"
    if randint(20) == 5:
        print("ПОЖА - А - А - АР!!!")
        sgor = int(nas * (random() / 3 + 0.3))
        sgorzer = int(zerno * (random() / 4 + 0.1))
        key()
        cls()
        # 1666 LET UMER=UMER+SGOR:
        #   LET ZERNO=ZERNO-SGORZER:
        #   RANDOMIZE USR VAL "53620":
        #   PRINT AT VAL "11",BIN ;"w OGNE POGIBLO ";SGOR;" ^ELOWEK":
        #   PRINT AT VAL "13",BIN ;"sGORELO NA SKLADAH ";SGORZER;AT VAL "14",VAL "11";"BU[.ZERNA":
        #   GO SUB KEY:
        #   GO SUB CLS
        umer += sgor
        zerno -= sgorzer
        print("В огне погибло %d человек" % sgor)
        print("Сгорело на складах %d буш. зерна" % sgorzer)
        key()
        cls()
    # 1663 GO TO VAL "1670"
    # 1670 IF FN S(VAL "10")=VAL "2" THEN
    #   LET AGENT=AGENT+SGN PI:
    #   RANDOMIZE USR VAL "45067":
    #   PRINT AT VAL "11",SGN PI;"w GOROD PROBRALSQ DIWERSANT":
    #   GO SUB KEY:
    #   GO SUB CLS:
    if randint(10) == 2:
        agent += 1
        print("В город пробрался диверсант")
        key()
        cls()
    # 1680 IF (AGENT<=BIN ) OR (Z>=NAS/VAL "10") THEN GO TO VAL "1720"
    if agent > 0 and z < nas / 10:
        # 1690 RANDOMIZE USR VAL "52462":
        #   PRINT AT VAL "11",VAL "2";"dIWERSIQ!!!pODOVVENY HLEBNYE";AT VAL "12",VAL "13";"SKLADY.":
        #   LET SGORZER=INT (ZERNO*(RND/3+0.3)):
        #   LET ZERNO=ZERNO-SGORZER:
        #   PRINT AT VAL "14",VAL "2";"sGORELO ";SGORZER;" BU[.ZERNA":
        #   GO SUB KEY:
        #   GO SUB CLS
        print("Диверсия!!! Подожжены хлебные склады.")
        sgorzer = int(zerno * (random() / 3 + 0.3))
        zerno -= sgorzer
        print("Сгорело %d буш. зерна" % sgorzer)
        key()
        cls()
        # 1700 IF Z>NAS/VAL "20" THEN
        #   PRINT AT VAL "11",VAL "6";"dIWERSANT SHWA^EN!!!":
        #   LET AGENT=AGENT-SGN PI:
        #   GO SUB KEY:
        #   GO SUB CLS:
        #   GO TO VAL "1720"
        if z > nas / 20:
            print("Диверсант схвачен!!!")
            agent -= 1
            key()
            cls()
        else:
            # 1710 RANDOMIZE USR VAL "45067":
            #   PRINT AT VAL "11",VAL "6";"dIWERSANT SKRYLSQ!!!":
            #   GO SUB KEY:
            #   GO SUB CLS
            print("Диверсант скрылся!!!")
            key()
            cls()
    # 1720 IF (AGENT<=BIN ) OR (Z<=NAS/VAL "2") THEN GO TO VAL "1740"
    if agent > 0 and z > nas / 2:
        # 1730 IF RND<0.5 THEN
        #   PRINT AT VAL "11",VAL "4";"pOJMAN WRAVESKIJ AGENT!!!":
        #   LET AGENT=AGENT-SGN PI:
        #   GO SUB KEY:
        #   GO SUB CLS
        if random() < 0.5:
            print("Пойман вражеский агент!!!")
            agent -= 1
            key()
            cls()
    # 1740 IF (K>=VAL "60") AND (NAS-Z-INT (ZAS/PROIZ)>=NAS/VAL "5") THEN
    #   RANDOMIZE USR VAL "47383":
    #   PRINT AT VAL "11",BIN ;"tUNEQDSTWU\@]IE \\LEMENTY ZANQLISX  SAMOGONOWARENIEM IZ HLEBNYH";
    #       AT VAL "13",VAL "12";"IZLI[KOW";AT VAL "14",SGN PI;"pONIVAETSQ PROIZWODITELXNOSTX!":
    #   LET PROIZ=PROIZ-VAL "2":
    #   GO SUB KEY:
    #   GO SUB CLS
    if k >= 60 and nas - z - zas // proiz >= nas / 5:
        print("Тунеядствующие элементы занялись самогоноварением из хлебных излишков")
        print("Понижается производительность!")
        proiz -= 2
        key()
        cls()
    # 1750 IF FN S(VAL "15")=VAL "8" THEN
    #   RANDOMIZE USR VAL "43909":
    #   PRINT AT VAL "11",VAL "2";"wNEDRENIE NOWYH ORUDIJ TRUDA    PODNQLO PROIZWODITELXNOSTX!":
    #   LET PROIZ=PROIZ+VAL "2":
    #   LET PREDEL=PREDEL+VAL "5":
    #   GO SUB KEY:
    #   GO SUB CLS
    if randint(15) == 8:
        print("Внедрение новых орудий труда подняло производительность!")
        proiz += 2
        predel += 5
        key()
        cls()
    # 1760 IF FN S(VAL "50")<>VAL "50" THEN GO TO VAL "1800"
    if randint(50) == 50:
        # 1770 PRINT AT VAL "11",VAL "5";"\{i6}dworcowyj pereworot!!!"
        print("ДВОРЦОВЫЙ ПЕРВОРОТ!!!")
        # 1780 IF (FN S(VAL "2")=SGN PI) OR (Z<NAS/VAL "10") THEN
        #   PRINT AT VAL "13",VAL "2";"wY SWERGNUTY S PRESTOLA!!!":
        #   LET U=SGN PI:
        #   LET OI=SGN PI:
        #   GO SUB KEY:
        #   GO SUB CLS:
        #   GO SUB OITOG:
        #   RETURN
        if randint(2) == 1 or z < nas / 10:
            print("Вы свергнуты с престола!!!")
            key()
            cls()
            return 1
        else:
            # 1790 PRINT AT VAL "13",VAL "2";"NO WERNYE wAM WOJSKA RAZBILI";AT VAL "14",VAL "11";"MQTEVNIKOW":
            #   GO SUB KEY:
            #   GO SUB CLS
            print("но верные Вам войска разбили мятежников")
            key()
            cls()
    # 1800 IF (TIME<=10) OR (ZAS<>ZEML) THEN GO TO VAL "1820"
    if model.time > 10 and zas == zeml:
        # 1810 IF IST<VAL "4" THEN
        #   LET IST=IST+SGN PI:
        #   RANDOMIZE USR VAL "62884":
        #   PRINT AT VAL "11",VAL "4";"iSTO]ENIE ZEMELX SNIVAET";AT VAL "12",VAL "10";"UROVAJNOSTX":
        #   GO SUB KEY:
        #   GO SUB CLS:
        #   GO TO VAL "1830"
        if ist < 4:
            ist += 1
            print("Истощение земель снижает урожайность")
            key()
            cls()
    else:
        # 1820 IF (ZAS<ZEML/VAL "2") AND (IST> -VAL "2") THEN
        #   LET IST=IST-SGN PI:
        #   RANDOMIZE USR VAL "58252":
        #   PRINT AT VAL "11",INT PI;"oTWEDENIE BOLX[IH PLO]ADEJ";AT VAL "12",VAL "4";"POD PARY POWY[AET UROVAJ":
        #   GO SUB KEY:
        #   GO SUB CLS
        if zas < zeml / 2 and ist > -2:
            ist -= 1
            print("Отведение больших площадей под пары повышает урожай")
            key()
            cls()
    # 1830 IF (FN S(VAL "15")=SGN PI) AND (AGENT>BIN ) THEN
    #   LET PROPALO=INT ((RND/VAL "5"+0.1)*ZERNO):
    #   RANDOMIZE USR VAL "47383":
    #   PRINT AT VAL "11",INT PI;"gRUPPOJ RASHITITELEJ POD";AT VAL "12",VAL "2";"PREDWODITELXSTWOM DIWERSANTA";
    #       AT VAL "13",INT PI;"POHI]ENO ";PROPALO;" BU[.ZERNA":
    #   LET ZERNO=ZERNO-PROPALO:
    #   GO SUB KEY:
    #   GO SUB CLS
    if randint(15) == 1 and agent > 0:
        propalo = int((random() / 5 + 0.1) * zerno)
        print("Группой расхитителей под предводительством диверсанта похищено %d буш. зерна" % propalo)
        zerno -= propalo
        key()
        cls()
    # 1840 LET NAS=NAS-UMER+ROD
    nas += rod - umer
    # 1850 RETURN