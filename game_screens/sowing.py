from io_devices.abstract_io import AbstractIO
from game_model import GameModel
from grain import sub_input, empty_lines


def posev(screen: AbstractIO, model: GameModel):
    # global zerno, ost, zas
    # 840 REM \#017\#001POSEW\#017\#000
    # 850 LET ZAS=-1: LET UROV=NOT PI: LET SBOR=NOT PI
    zas = -1
    urozh = 0
    sbor = 0
    # 860 IF (OST>NOT PI) AND (ZERNO>NOT PI) THEN
    #   GO TO VAL "880"
    # 870 RETURN
    if not (ost > 0 and zerno > 0):
        return
    # 880 PRINT AT VAL "18",SGN PI;"u NAS ";ZEML;" AKROW ZEMLI":
    #   PRINT AT VAL "19",BIN ;"l\@DI MOGUT ZASEQTX ";PROIZ*OST;" AKROW":
    #   PRINT AT VAL "20",VAL "2";"zERNA HWATIT NA ";ZERNO*2;" AKROW"
    print("У нас %d акров земли" % zeml)
    print("Люди могут засеять %d акров" % (proiz * ost))
    print("Зерна хватит на %d акров" % (zerno / 0.5))
    while True:
        # 890 PRINT AT VAL "21",VAL "7";"sKOLXKO ZASEEM?"
        print("Сколько засеем?")
        # 900 GO SUB INPUT: LET ZAS=VAL F$:
        #   PRINT AT VAL "18",BIN ;S$:
        #   GO SUB PUS:
        #   IF ZAS<BIN THEN
        #       GO TO VAL "890"
        zas = int(sub_input())
        empty_lines()
        if zas < 0:
            continue
        # 910 IF ZAS>ZEML THEN
        #   PRINT AT VAL "20",VAL "5";"u NAS MALO ZEMLI!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   LET ZAS=-1:
        #   GO TO VAL "890"
        if zas > zeml:
            print("У нас мало земли!!!")
            key()
            empty_lines()
            zas = -1
            continue
        # 920 IF ZAS/VAL "2">ZERNO THEN
        #   PRINT AT VAL "20",VAL "4";"u NAS NE HWATIT ZERNA!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   LET ZAS=-1:
        #   GO TO VAL "890"
        if zas * 0.5 > zerno:
            print("У нас не хватит зерна!!!")
            key()
            empty_lines()
            zas = -1
            continue
        # 930 IF INT (ZAS/PROIZ)>OST THEN
        #   PRINT AT VAL "20",VAL "5";"u NAS MALO L\@DEJ!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   LET ZAS=-1:
        #   GO TO VAL "890"
        if zas // proiz > ost:
            print("У нас мало людей!")
            key()
            empty_lines()
            zas = -1
            continue
        # 940 LET ZERNO=ZERNO-INT (ZAS/VAL "2"):
        #   LET OST=OST-INT (ZAS/PROIZ)
        zerno -= zas * 0.5
        ost -= zas // proiz
        # 950 RETURN
        return
