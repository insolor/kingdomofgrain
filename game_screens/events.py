from random import random

from end_game_exception import EndGameException
from game_model import GameModel
from grain import randint
from io_devices import AbstractIO


def events(device: AbstractIO, model: GameModel):
    # 1550 REM \#017\#001NN\#017\#000
    # 1555 GO SUB CLS
    device.cls()

    # 1560 LET BEV=INT (RND*INT (NAS/4))
    model.refugees = int(random() * (model.population // 4))

    # 1570 IF (RASST<20) AND (RND>.5) THEN
    #   LET BEV=BEV+INT (RND*BEV):
    #   PRINT AT VAL "11",INT PI;"pRITOK BEVENCEW SPASA\@]IHSQ";AT VAL "12",VAL "7";"OT ZAHWAT^IKOW!!!":
    #   GO SUB KEY:
    #   GO SUB CLS
    if model.distance_to_enemies < 20 and random() > 0.5:
        model.refugees += int(random() * model.refugees)
        device.at(11, 3).print("Приток беженцев, спасающихся").at(12, 7).print("от захватчиков!!!")
        device.wait_key()
        device.cls()

    # 1580 LET NAS=NAS+BEV
    model.population += model.refugees

    # 1590 IF (K<10) OR (UMERWSEGO>NAS*10) THEN
    #   RANDOMIZE USR VAL "55936": PRINT AT VAL "11",SGN PI;"nAROD WOSSTAL PROTIW TIRANA!!!":
    #   GO SUB KEY:
    #   GO SUB CLS:
    #   GO TO VAL "1610"
    if model.feeding_per_worker < 10 or model.dead_total > model.population * 10:
        device.show_image("riot")
        device.at(11, 1).print("Народ восстал против тирана!!!")
        device.wait_key()
        device.cls()

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
        if (model.population - model.defenders) / 3 < model.defenders < model.dead_starvation:
            device.show_image("enemies")
            device.at(11, 1).print("Но войска подавили восстание!")
            rebels = (model.population - model.defenders) * int(random() / 5 + 0.1)
            model.dead_in_battles += rebels
            model.population -= rebels

            device.at(12, 5).print(f"В уличных боях полегло {rebels} жителей")
            device.wait_key()
            device.cls()
        else:
            # 1620 PRINT AT VAL "11",VAL "4";"wOJSKA PERE[LI NA STORONU";AT VAL "12",VAL "6";"WOSSTAW[EGO NARODA":
            #   PRINT AT VAL "14",VAL "5";"\{i4}monarhiq swergnuta!!!":
            #   GO SUB KEY:
            #   GO SUB CLS:
            #   LET U=SGN PI:
            #   LET OI=BIN :
            #   GO SUB OITOG:
            #   RETURN
            device.at(11, 4).print("Войска перешли на сторону").at(12, 6).print("восставшего народа")
            device.at(14, 5).ink(4).print("МОНАРХИЯ СВЕРГНУТА!!!")
            device.wait_key()
            device.cls()
            raise EndGameException(False)


    # 1600 GO TO VAL "1630"
    # 1630 LET UMER=UMER+INT (RND*2.5/100*NAS):
    #   LET ROD=INT (RND*(4+K/20)/100*NAS)
    model.dead_natural_cases += int(random() * 2.5 / 100 * model.population)
    model.born = int(random() * (4 + model.feeding_per_worker / 20) / 100 * model.population)

    # 1640 IF FN S(VAL "12")=SGN PI THEN
    #   LET CHUMA=INT (RND*50+VAL "5"):
    #   RANDOMIZE USR VAL "53620":
    #   PRINT AT VAL "11",INT PI;"~UMA UNESLA ";CHUMA;"% NASELENIQ!":
    #   LET UMER=UMER+INT (NAS*CHUMA/100):
    #   GO SUB KEY:
    #   GO SUB CLS
    if randint(12) == 1:
        plague = int(random() * 50 + 5)
        device.show_image("graveyard")
        device.at(11, 3).print(f"Чума унесла {plague}% населения!")
        model.dead_natural_cases += model.population * plague // 100
        device.wait_key()
        device.cls()

    # 1650 IF FN S(VAL "100")<VAL "5" THEN
    #   RANDOMIZE USR VAL "46225":
    #   PRINT AT VAL "11",VAL "4";"dEMOGRAFI^ESKIJ WZRYW!!!":
    #   LET DEM=INT ((RND/VAL "2"+0.5)*NAS):
    #   LET ROD=ROD+DEM:
    #   GO SUB KEY:
    #   GO SUB CLS
    if randint(100) < 5:
        device.show_image("baby_boom")
        device.at(11, 4).print("Демографический взрыв!!!")
        dem = int((random() / 2 + 0.5) * model.population)
        model.born += dem
        device.wait_key()
        device.cls()

    # 1660 IF (FN S(VAL "20"))=VAL "5" THEN
    #   RANDOMIZE USR VAL "52462":
    #   PRINT AT VAL "11",VAL "6";"\{i2}pova - a - a - ar!!!":
    #   LET SGOR=INT (NAS*(RND/3+0.3)):
    #   LET SGORZER=INT (ZERNO*(RND/4+0.1)):
    #   GO SUB KEY:
    #   GO SUB CLS:
    #   GO TO VAL "1666"
    if randint(20) == 5:
        device.show_image("fire")
        device.at(11, 6).ink(2).print("ПОЖА - А - А - АР!!!")
        dead_in_fire = int(model.population * (random() / 3 + 0.3))
        burnt_down_grain = int(model.grain * (random() / 4 + 0.1))
        device.wait_key()
        device.cls()

        # 1666 LET UMER=UMER+SGOR:
        #   LET ZERNO=ZERNO-SGORZER:
        #   RANDOMIZE USR VAL "53620":
        #   PRINT AT VAL "11",BIN ;"w OGNE POGIBLO ";SGOR;" ^ELOWEK":
        #   PRINT AT VAL "13",BIN ;"sGORELO NA SKLADAH ";SGORZER;AT VAL "14",VAL "11";"BU[.ZERNA":
        #   GO SUB KEY:
        #   GO SUB CLS
        model.dead_natural_cases += dead_in_fire
        model.grain -= burnt_down_grain
        device.show_image("graveyard")
        device.at(11, 0).print(f"В огне погибло {dead_in_fire} человек")
        device.at(13, 0).print(f"Сгорело на складах {burnt_down_grain}").at(14, 11).print("буш. зерна")
        device.wait_key()
        device.cls()

    # 1663 GO TO VAL "1670"
    # 1670 IF FN S(VAL "10")=VAL "2" THEN
    #   LET AGENT=AGENT+SGN PI:
    #   RANDOMIZE USR VAL "45067":
    #   PRINT AT VAL "11",SGN PI;"w GOROD PROBRALSQ DIWERSANT":
    #   GO SUB KEY:
    #   GO SUB CLS:
    if randint(10) == 2:
        model.agent += 1
        device.show_image("saboteur")
        device.at(11, 1).print("В город пробрался диверсант")
        device.wait_key()
        device.cls()

    # 1680 IF (AGENT<=BIN ) OR (Z>=NAS/VAL "10") THEN GO TO VAL "1720"
    if model.agent > 0 and model.defenders < model.population / 10:
        # 1690 RANDOMIZE USR VAL "52462":
        #   PRINT AT VAL "11",VAL "2";"dIWERSIQ!!!pODOVVENY HLEBNYE";AT VAL "12",VAL "13";"SKLADY.":
        #   LET SGORZER=INT (ZERNO*(RND/3+0.3)):
        #   LET ZERNO=ZERNO-SGORZER:
        #   PRINT AT VAL "14",VAL "2";"sGORELO ";SGORZER;" BU[.ZERNA":
        #   GO SUB KEY:
        #   GO SUB CLS
        device.show_image("fire")
        device.at(11, 2).print("Диверсия!!! Подожжены хлебные").at(12, 13).print("склады.")
        burnt_down_grain = int(model.grain * (random() / 3 + 0.3))
        model.grain -= burnt_down_grain
        device.at(14, 2).print(f"Сгорело {burnt_down_grain} буш. зерна")
        device.wait_key()
        device.cls()

        # 1700 IF Z>NAS/VAL "20" THEN
        #   PRINT AT VAL "11",VAL "6";"dIWERSANT SHWA^EN!!!":
        #   LET AGENT=AGENT-SGN PI:
        #   GO SUB KEY:
        #   GO SUB CLS:
        #   GO TO VAL "1720"
        if model.defenders > model.population / 20:
            device.at(11, 6).print("Диверсант схвачен!!!")
            model.agent -= 1
            device.wait_key()
            device.cls()
        else:
            # 1710 RANDOMIZE USR VAL "45067":
            #   PRINT AT VAL "11",VAL "6";"dIWERSANT SKRYLSQ!!!":
            #   GO SUB KEY:
            #   GO SUB CLS
            device.show_image("saboteur")
            device.at(11, 6).print("Диверсант скрылся!!!")
            device.wait_key()
            device.cls()

    # 1720 IF (AGENT<=BIN ) OR (Z<=NAS/VAL "2") THEN GO TO VAL "1740"
    if model.agent > 0 and model.defenders > model.population / 2:
        # 1730 IF RND<0.5 THEN
        #   PRINT AT VAL "11",VAL "4";"pOJMAN WRAVESKIJ AGENT!!!":
        #   LET AGENT=AGENT-SGN PI:
        #   GO SUB KEY:
        #   GO SUB CLS
        if random() < 0.5:
            device.at(11, 4).print("Пойман вражеский агент!!!")
            model.agent -= 1
            device.wait_key()
            device.cls()

    # 1740 IF (K>=VAL "60") AND (NAS-Z-INT (ZAS/PROIZ)>=NAS/VAL "5") THEN
    #   RANDOMIZE USR VAL "47383":
    #   PRINT AT VAL "11",BIN ;"tUNEQDSTWU\@]IE \\LEMENTY ZANQLISX  SAMOGONOWARENIEM IZ HLEBNYH";
    #       AT VAL "13",VAL "12";"IZLI[KOW";AT VAL "14",SGN PI;"pONIVAETSQ PROIZWODITELXNOSTX!":
    #   LET PROIZ=PROIZ-VAL "2":
    #   GO SUB KEY:
    #   GO SUB CLS
    if (model.feeding_per_worker >= 60 and
            model.population - model.defenders - model.zas // model.sower_productivity >= model.population / 5):
        device.show_image("parasites")
        device.at(11, 0).print("Тунеядствующие элементы занялись самогоноварением из хлебных")
        device.at(13, 12).print("излишков")
        device.at(14, 1).print("Понижается производительность!")
        model.sower_productivity -= 2
        device.wait_key()
        device.cls()

    # 1750 IF FN S(VAL "15")=VAL "8" THEN
    #   RANDOMIZE USR VAL "43909":
    #   PRINT AT VAL "11",VAL "2";"wNEDRENIE NOWYH ORUDIJ TRUDA    PODNQLO PROIZWODITELXNOSTX!":
    #   LET PROIZ=PROIZ+VAL "2":
    #   LET PREDEL=PREDEL+VAL "5":
    #   GO SUB KEY:
    #   GO SUB CLS
    if randint(15) == 8:
        device.show_image("tools")
        device.at(11, 2).print("Внедрение новых орудий труда    подняло производительность!")
        model.sower_productivity += 2
        model.max_sower_productivity += 5
        device.wait_key()
        device.cls()

    # 1760 IF FN S(VAL "50")<>VAL "50" THEN GO TO VAL "1800"
    if randint(50) == 50:
        # 1770 PRINT AT VAL "11",VAL "5";"\{i6}dworcowyj pereworot!!!"
        device.at(11, 5).ink(6).print("ДВОРЦОВЫЙ ПЕРВОРОТ!!!")

        # 1780 IF (FN S(VAL "2")=SGN PI) OR (Z<NAS/VAL "10") THEN
        #   PRINT AT VAL "13",VAL "2";"wY SWERGNUTY S PRESTOLA!!!":
        #   LET U=SGN PI:
        #   LET OI=SGN PI:
        #   GO SUB KEY:
        #   GO SUB CLS:
        #   GO SUB OITOG:
        #   RETURN
        if randint(2) == 1 or model.defenders < model.population / 10:
            device.at(13, 2).print("Вы свергнуты с престола!!!")
            device.wait_key()
            device.cls()
            raise EndGameException(True)
        else:
            # 1790 PRINT AT VAL "13",VAL "2";"NO WERNYE wAM WOJSKA RAZBILI";AT VAL "14",VAL "11";"MQTEVNIKOW":
            #   GO SUB KEY:
            #   GO SUB CLS
            device.at(13, 2).print("но верные Вам войска разбили").at(14, 11).print("мятежников")
            device.wait_key()
            device.cls()

    # 1800 IF (TIME<=10) OR (ZAS<>ZEML) THEN GO TO VAL "1820"
    if model.time > 10 and model.zas == model.land:
        # 1810 IF IST<VAL "4" THEN
        #   LET IST=IST+SGN PI:
        #   RANDOMIZE USR VAL "62884":
        #   PRINT AT VAL "11",VAL "4";"iSTO]ENIE ZEMELX SNIVAET";AT VAL "12",VAL "10";"UROVAJNOSTX":
        #   GO SUB KEY:
        #   GO SUB CLS:
        #   GO TO VAL "1830"
        if model.ist < 4:
            model.ist += 1
            device.show_image("bad_harvest")
            device.at(11, 4).print("Истощение земель снижает").at(12, 10).print("урожайность")
            device.wait_key()
            device.cls()
    else:
        # 1820 IF (ZAS<ZEML/VAL "2") AND (IST> -VAL "2") THEN
        #   LET IST=IST-SGN PI:
        #   RANDOMIZE USR VAL "58252":
        #   PRINT AT VAL "11",INT PI;"oTWEDENIE BOLX[IH PLO]ADEJ";AT VAL "12",VAL "4";"POD PARY POWY[AET UROVAJ":
        #   GO SUB KEY:
        #   GO SUB CLS
        if model.zas < model.land / 2 and model.ist > -2:
            model.ist -= 1
            device.show_image("excellent_harvest")
            device.at(11, 3).print("Отведение больших площадей").at(12, 4).print("под пары повышает урожай")
            device.wait_key()
            device.cls()

    # 1830 IF (FN S(VAL "15")=SGN PI) AND (AGENT>BIN ) THEN
    #   LET PROPALO=INT ((RND/VAL "5"+0.1)*ZERNO):
    #   RANDOMIZE USR VAL "47383":
    #   PRINT AT VAL "11",INT PI;"gRUPPOJ RASHITITELEJ POD";AT VAL "12",VAL "2";"PREDWODITELXSTWOM DIWERSANTA";
    #       AT VAL "13",INT PI;"POHI]ENO ";PROPALO;" BU[.ZERNA":
    #   LET ZERNO=ZERNO-PROPALO:
    #   GO SUB KEY:
    #   GO SUB CLS
    if randint(15) == 1 and model.agent > 0:
        stolen = int((random() / 5 + 0.1) * model.grain)
        device.show_image("parasites")
        device.at(11, 3).print("Группой расхитителей под")
        device.at(12, 2).print(f"предводительством диверсанта похищено {stolen} буш. зерна")
        model.grain -= stolen
        device.wait_key()
        device.cls()

    # 1840 LET NAS=NAS-UMER+ROD
    model.population += model.born - model.dead_natural_cases
    # 1850 RETURN
