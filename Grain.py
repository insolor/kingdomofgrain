import random

# BAS file "" created by ZX-Modules

#   3 BORDER NOT PI: POKE VAL "23624",VAL "71": POKE VAL "23693",VAL "71": CLS 
#   4 GO SUB VAL "6": GO TO VAL "10"
#   6 POKE VAL "23607",VAL "196": POKE VAL "23606",VAL "104": RETURN 
#   8 POKE VAL "23607",VAL "60": POKE VAL "23606",NOT PI: RETURN 

# Список номеров строк процедур
#  10 LET INSTR=VAL "1510": LET INFO=VAL "300": LET TORG=VAL "500": LET OHRANA=VAL "610": LET KORM=VAL "700": LET POSEW=VAL "840": LET HAMONY=VAL "960": LET UBORKA=VAL "1300": LET NN=VAL "1550": LET WAR=VAL "1860": LET OITOG=VAL "1980": LET POBEDA=VAL "1150": LET PORAV=VAL "1240": LET ATAKA=VAL "1910"
#  12 LET KEY=VAL "4010": LET CLS=VAL "4015": LET INPUT=VAL "4020"
#  14 LET PUS=VAL "4030": LET S$="                                                                "

s = "                                                                "

#  20 DIM T(VAL "3")
t = [0,0,0]

#  21 DEF FN S(K)=INT (RND*K-0.0000001)+SGN PI
def fn_S(K):
    return int(random.random()*K-0.0000001)+1

#  30 DIM Q(VAL "22")
q = [0 for x in range(22)]

def cls():
    #4015 POKE VAL "23659",VAL "2": CLS : POKE VAL "23659",NOT PI: RETURN 
    #4017 CLS : RETURN 
    pass

def info():
    # 300 REM \#017\#001INFO\#017\#000
    # 310 GO SUB CLS
    cls()
    # 330 PRINT "\{i5}********************************"
    print('********************************')
    # 335 PRINT 
    print()
    # 340 INK VAL "6": PRINT AT VAL "2",VAL "8";TIME;" gOD PRAWLENIQ:": INK VAL "7"
    print("%d Год правления:" % time)
    # 350 IF BEV>BIN THEN PRINT ;"\{b0i7}w GOROD PRI[LO ";BEV;" BEVENCEW"
    if bezh>0:
        print('В город пришло %d беженцев' % bezh)
    # 360 PRINT "rODILOSX  ";ROD;" ^ELOWEK"
    print('Родилось %d человек' % rod)
    # 370 PRINT "\{b0}uMERLO   ";UMER;" ^ELOWEK"
    print('Умерло   %d человек' % umer)
    # 380 IF UMERGOL>BIN THEN PRINT "OT gOLODA - ";UMERGOL;" ^ELOWEK"
    if umergol>0:
        print('От голода - %d человек' % umergol)
    # 390 IF POGIB>BIN THEN PRINT "\{b0}w BOQH POLEGLO ";POGIB;" ^ELOWEK"
    if pogib>0:
        print('В боях полегло %d человек' % pogib)
    # 395 IF NAS<=BIN THEN LET NAS=SGN PI
    global nas
    if nas<=0:
        nas = 1
    # 400 PRINT "nASELENIE - ";NAS;" ^ELOWEK"
    print("Население - %d человек" % nas)
    # 410 PRINT "\{b0}zEMLI - ";ZEML;" AKROW"
    print("Земли - %d акров" % zeml)
    # 420 PRINT "uROVAJ - ";UROV;" BU[/AKR"
    print("Урожай - %d буш/акр" % urov)
    # 430 IF KRYS>BIN THEN PRINT "kRYSY SOVRALI ";KRYS;" BU[."
    if krys>0:
        print("Крысы сожрали %d буш." % krys)
    # 440 PRINT "\{b0}zAPASY ZERNA ";ZERNO;" BU[."
    print("Запасы зерны %d буш." % zerno)
    # 450 PRINT "cENA ZEMLI ";CENA;" BU[/AKR"
    print("Цена земли %d буш/акр" % cena)
    # 460 PRINT "\{b0}hLEBOROB ZASEWAET ";PROIZ;" AKROW"
    print("Хлебороб засевает %d акров" % proiz)
    # 470 LET I=25+FN S(10): IF RASST<I THEN PRINT "nAPADA\@T  ";WRAGI;" WOINOW": PRINT "ONI W ";RASST;" MILQH OT NAS!"
    i = 25+fn_S(10)
    if rasst<i:
        print("Нападают %d воинов" % vragi)
        print("Они в %d милях от нас!" % rasst)
    # 475 PRINT
    # 480 PRINT "\{i5}********************************"
    print()
    print("********************************")
    # 490 RETURN

def torg():
    global zerno, zeml
    # 500 REM \#017\#001TORGOWLQ\#017\#000
    while True:
        # 510 LET ZEM=-1: PRINT AT VAL "20",VAL "5";"sKOLXKO KUPIM ZEMLI?"
        zem = -1
        print("Сколько купим земли?")
        # 520 GO SUB INPUT: LET ZEM=VAL F$: GO SUB PUS: IF ZEM<BIN THEN GO TO VAL "510"
        zem = int(sub_input())
        pus()
        # 530 IF CENA*ZEM>ZERNO THEN PRINT AT VAL "20",BIN ;"u NAS TOLXKO ";ZERNO;" BU[ELEJ ZERNA!!!": GO SUB KEY: GO SUB PUS: GO TO VAL "510"
        if cena*zem>zerno:
            print("У нас только %d бушелей зерна!!!" % zerno)
            key()
            pus()
            continue
        # 540 LET ZEML=ZEML+ZEM: LET ZERNO=ZERNO-CENA*ZEM
        zeml += zem
        zerno -= cena*zem
        # 550 PRINT AT VAL "20",SGN PI;"u NAS ";ZERNO;" BU[ELEJ ZERNA": GO SUB KEY: GO SUB PUS
        print("У нас %d бушелей зерна" % zerno)
        key()
        pus()
        break
    
    while True:
        # 560 LET ZEM=-1: PRINT AT VAL "20",VAL "4";"sKOLXKO ZEMLI PRODADIM?"
        zem = -1
        print("Сколько земли продадим?")
        # 570 GO SUB INPUT: LET ZEM=VAL F$: IF ZEM<BIN THEN GO TO VAL "560"
        zem = int(sub_input())
        # 580 IF ZEM>ZEML THEN PRINT AT VAL "20",BIN ;"u NAS TOLXKO ";ZEML;" AKROW ZEMLI!!!": GO SUB KEY: GO SUB PUS: GO TO VAL "560"
        if zem>zeml:
            print("У нас только %d акров земли!!!")
            key()
            pus()
            continue
        # 590 LET ZEML=ZEML-ZEM: LET ZERNO=ZERNO+ZEM*CENA
        zeml -= zem
        zerno += zem*cena
        # 600 RETURN 
        break

def ohrana():
    global ost, zerno
    # 610 REM \#017\#001OHRANA\#017\#000
    while True:
        # 620 LET UBITO=NOT PI: LET Z=-1
        ubito = 0
        z = -1
        # 630 GO SUB PUS: PRINT AT VAL "20",VAL "5";"u NAS ";NAS;" ^ELOWEK"
        pus()
        print("У нас %d человек" % nas)
        # 640 PRINT AT VAL "21",INT PI;"sKOLXKO PO[LEM W WOJSKO?": GO SUB INPUT: LET Z=VAL F$: GO SUB PUS
        print("Сколько пошлём в войско?")
        z = int(sub_input())
        pus()
        # 650 IF Z<NOT PI THEN GO TO VAL "620"
        if z<0:
            continue
        # 660 IF Z>NAS THEN PRINT AT VAL "20",VAL "6";"u NAS MALO L\@DEJ!!!": GO SUB KEY: GO SUB PUS: GO TO VAL "620"
        if z>nas:
            print("У нас мало людей!!!")
            key()
            pus()
            continue
        # 670 IF Z>INT (ZERNO/VAL "5") THEN PRINT AT VAL "20",SGN PI;"zERNA HWATIT NA ";INT (ZERNO/5);" WOINOW": GO SUB KEY: GO SUB PUS: GO TO VAL "620"
        if z>int(zerno/5):
            print("Зерна хватит на %d воинов" % (zerno/5))
            key()
            pus()
            continue
        # 680 IF Z>NOT PI THEN LET OST=NAS-Z: LET ZERNO=ZERNO-Z*5: RETURN 
        if z>0:
            ost=nas-z
            zerno-=z*5
        else:
            # 690 LET OST=NAS: RETURN 
            ost=nas
        return

def korm():
    global zerno, umergol, umervsego, nas, oi, u
    # 700 REM \#017\#001KORMEVKA\#017\#000
    # 710 LET K=-1: IF OST<=NOT PI THEN RETURN 
    k=-1
    if ost<=0:
        return
    while True:
        # 720 PRINT AT VAL "20",SGN PI;"mOVNO DATX ";INT (ZERNO/OST);" BU[ NA ^ELOWEKA": PRINT AT VAL "21",VAL "6";"sKOLXKO DA[X?"
        print("Можно дать %d буш на человека" % (zerno//ost))
        print("Сколько дать?")
        # 730 GO SUB INPUT: LET K=VAL F$: GO SUB PUS: IF K<BIN THEN : GO TO VAL "720"
        k = int(sub_input())
        if k<0:
            continue
        # 740 IF K*OST>ZERNO THEN PRINT AT VAL "20",INT PI;"u NAS NET STOLXKO ZERNA!!!": GO SUB KEY: GO SUB PUS: GO TO VAL "720"
        if k*ost>zerno:
            print("У нас нет столько зерна!!!")
            key()
            continue
        # 750 LET ZERNO=ZERNO-K*OST
        zerno-=k*ost
        # 760 IF K<VAL "20" THEN LET UMERGOL=OST*INT (SGN PI-K/VAL "20"): LET UMERWSEGO=UMERWSEGO+UMERGOL: LET NAS=NAS-UMERGOL
        if k<20:
            umergol=ost*int(1-k/20)
            umervsego+=umergol
            nas-=umergol
        # 770 IF NAS<=NOT PI OR K=NOT PI THEN GO SUB CLS: RANDOMIZE USR VAL "53620": PRINT AT VAL "11",INT PI;"\{i2}ty UMORIL WSEH GOLODOM!!!": GO SUB KEY: LET OI=BIN : LET U=SGN PI: GO SUB OITOG: RETURN 
        if nas<=0 or k==0:
            cls()
            print("Ты уморил всех голодом!!!")
            key()
            oi=0
            u=1
            oitog()
            return
        # 780 IF K<=VAL "10" THEN PRINT AT VAL "20",VAL "10";"\{i3}du{egub!!!": GO SUB KEY: GO SUB PUS: GO TO VAL "800"
        if k<=18:
            print("ДУШЕГУБ!!!")
            key()
            pus()
        # 790 IF K<=VAL "21" THEN PRINT AT VAL "20",VAL "10";"\{i5}vadina!!!": GO SUB KEY: GO SUB PUS
        elif k<=21:
            print("ЖАДИНА!!!")
            key()
            pus()
        # 800 IF K>VAL "20" THEN LET UMERGOL=BIN 
        if k>20:
            umergol=0
        # 810 IF K>VAL "70" THEN PRINT AT VAL "20",BIN ;"\{i6}w..WY...wypx..pxem!!!za tebq!!!": GO SUB KEY: GO SUB PUS: GO TO VAL "830"
        if k>70:
            print("В..вы...ВЫПЬ..ПЬЕМ!!!ЗА ТЕБЯ!!!")
            key()
            pus()
        # 820 IF K>VAL "50" THEN PRINT AT VAL "20",VAL "5";"\{i4}bLAGODETELX ty NA[!!!": GO SUB KEY: GO SUB PUS
        elif k>50:
            print("Благодетель ты НАШ!!!")
            key()
            pus()
        # 830 RETURN 
        return

def posev():
    global zerno, ost
    # 840 REM \#017\#001POSEW\#017\#000
    # 850 LET ZAS=-1: LET UROV=NOT PI: LET SBOR=NOT PI
    zas=-1
    urozh=0
    sbor=0
    # 860 IF (OST>NOT PI) AND (ZERNO>NOT PI) THEN GO TO VAL "880"
    # 870 RETURN 
    if not(ost>0 and zerno>0):
        return
    # 880 PRINT AT VAL "18",SGN PI;"u NAS ";ZEML;" AKROW ZEMLI": PRINT AT VAL "19",BIN ;"l\@DI MOGUT ZASEQTX ";PROIZ*OST;" AKROW": PRINT AT VAL "20",VAL "2";"zERNA HWATIT NA ";ZERNO*2;" AKROW"
    print("У нас %d акров земли" % zeml)
    print("Люди могут засеять %d акров" % (proiz*ost))
    print("Зерна хватит на %d акров" % (zerno/0.5))
    while True:
        # 890 PRINT AT VAL "21",VAL "7";"sKOLXKO ZASEEM?"
        print("Сколько засеем?")
        # 900 GO SUB INPUT: LET ZAS=VAL F$: PRINT AT VAL "18",BIN ;S$: GO SUB PUS: IF ZAS<BIN THEN GO TO VAL "890"
        zas = int(sub_input())
        pus()
        if zas<0:
            continue
        # 910 IF ZAS>ZEML THEN PRINT AT VAL "20",VAL "5";"u NAS MALO ZEMLI!!!": GO SUB KEY: GO SUB PUS: LET ZAS=-1: GO TO VAL "890"
        if zas>zeml:
            print("У нас мало земли!!!")
            key()
            pus()
            zas=-1
            continue
        # 920 IF ZAS/VAL "2">ZERNO THEN PRINT AT VAL "20",VAL "4";"u NAS NE HWATIT ZERNA!!!": GO SUB KEY: GO SUB PUS: LET ZAS=-1: GO TO VAL "890"
        if zas*0.5>zerno:
            print("У нас не хватит зерна!!!")
            key()
            pus()
            zas=-1
            continue
        # 930 IF INT (ZAS/PROIZ)>OST THEN PRINT AT VAL "20",VAL "5";"u NAS MALO L\@DEJ!!!": GO SUB KEY: GO SUB PUS: LET ZAS=-1: GO TO VAL "890"
        if zas//proiz>ost:
            print("У нас мало людей!")
            key()
            pus()
            zas=-1
            continue
        # 940 LET ZERNO=ZERNO-INT (ZAS/VAL "2"): LET OST=OST-INT (ZAS/PROIZ)
        zerno-=zas*0.5
        ost-=zas//proiz
        # 950 RETURN 
        return

def pobeda():
    global nas, zeml, zerno, pogib, zahv, ost
    #1150 REM \#017\#001POBEDA\#017\#000
    #1155 GO SUB CLS: RANDOMIZE USR VAL "54778"
    cls()
    #1160 PRINT AT VAL "11",VAL "2";"\{i6}w hAMONII ODERVANA pobeda!!!"
    print("В хамонии одержана победа!!!")
    #1170 LET T(INT PI)=INT (NAS*(RND/3+0.3)): LET T(SGN PI)=INT (ZAHW*(FN S(VAL "10")+VAL "4")): LET T(VAL "2")=INT (ZEML*(RND/VAL "2"+0.3)): LET NAS=NAS+T(INT PI): LET ZEML=ZEML+T(VAL "2"): LET ZERNO=ZERNO+T(SGN PI)
    t[2]=int(nas*(random()/3+0.3))
    t[0]=int(zahv*fn_S(10)+4)
    t[1]=int(zeml*(random()/2+0.3))
    nas+=t[2]
    zeml+=t[1]
    zerno+=t[0]
    #1180 LET UBITO=INT (ZAHW*(RND/5+0.3)): LET POGIB=POGIB+UBITO: LET NAS=NAS+ZAHW-UBITO
    ubito=int(zahv(random()/5+0.3))
    pogib+=ubito
    nas+=zahv-ubito
    #1190 PRINT AT VAL "13",BIN ;"u WRAGA ZAHWA^ENO:"
    print("У врага захвачено:")
    #1200 PRINT AT VAL "14",SGN PI;"zERNA - ";T(1);" BU[ELEJ": PRINT " zEMLI - ";T(2);" AKROW": PRINT " pLENNYH - ";T(3);" ^ELOWEK"
    print("Зерна - %d бушелей" % t[0])
    print("Земли - %d акров" % t[1])
    print("Пленных - %d человек" % t[2])
    #1210 PRINT AT VAL "18",VAL "6";"iZ ";ZAHW;" WOINOW ";UBITO;AT VAL "19",VAL "10";"PALO SMERTX\@ HRABRYH!"
    print("Из %d воинов %d пало сметрью храбрых!" % (zahv, ubito))
    #1220 LET ZAHW=BIN : LET OST=NAS-Z-INT (ZAS/PROIZ)
    zahv=0
    ost=nas-z-int(zas/proiz)
    #1225 GO SUB KEY: GO SUB CLS
    key()
    cls()
    #1230 RETURN 

def porazh():
    global nas, pogib, zahv, ost
    #1240 REM \#017\#001PORAVENIE\#017\#000
    #1245 GO SUB CLS: RANDOMIZE USR VAL "54778"
    cls()
    #1250 PRINT AT VAL "11",VAL "5";"\{i3}poravenie w hAMONII!!!"
    print("ПОРАЖЕНИЕ В Хамонии!!!")
    #1260 LET UBITO=INT (ZAHW*(0.8+RND/5)): LET NAS=NAS+ZAHW-UBITO: LET POGIB=POGIB+UBITO
    ubito=int(zahv*(0.8+random()/5))
    nas+=zahv-ubito
    pogib+=ubito
    #1270 PRINT AT VAL "13",SGN PI;"pOGIBLO - ";UBITO;" WOINOW"
    print("Погибло - %d воинов" % ubito)
    #1280 LET ZAHW=BIN : LET OST=NAS-Z-INT (ZAS/PROIZ)
    zahv=0
    ost=nas-z-int(zas/proiz)
    #1285 GO SUB KEY: GO SUB CLS
    key()
    cls()
    #1290 RETURN 

def instr():
    #1510 REM \#017\#001instrukciq\#017\#000
    #1515 GO SUB CLS
    cls()
    #1520 PRINT AT NOT PI,VAL "10";"instrukciq": PRINT "  wAM PREDLAGAETSQ POPROBOWATX": PRINT " SWOI SILY W UPRAWLENII STRANOJ": PRINT "  wA[A CELX - KAK MOVNO DOLX[E": PRINT AT VAL "4",VAL "5";"PRODERVATXSQ U WLASTI."
    print("ИНСТРУКЦИЯ")
    print("  Вам предлагается попробовать\n свои силы в управлении страной")
    print("  Ваша цель - как можно дольше\n продержаться у власти.")
    #1522 PRINT AT VAL "5",VAL "8";"\{i6} u^TITE ~to:": PRINT "  oDNOMU ^ELOWEKU NUVNO W GOD": PRINT "   NE MENEE 22 BU[ELEJ ZERNA": PRINT "   ^TOBY ZASEQTX 1 AKR NUVNO": PRINT "   - 0.5 BU[ELEJ ZERNA": PRINT "   oDIN SOLDAT S'EDAET W GOD       - 5 BU[ELEJ ZERNA"
    print(" Учтите, что:")
    print("   Одному человеку нужно в год")
    print("   не менее 22 бушелей зерна")
    print("   Чтобы засеять 1 акр нужно")
    print("   - 0.5 бушелей зерна")
    print("  Один солдат съедает в год")
    print("   - 5 бушелей зерна")
    #1530 PRINT : PRINT "        vELAEM uspeha!!!"
    print("        Желаем УСПЕХА!!!")
    #1534 PRINT AT VAL "15",SGN PI;"\{i3} d-W REVIME \i\n\p PLAY SPECTRUM  WHOD W MEN\@           DOZAGRUZOK"
    print(" d - в режиме play spectrum - вход в меню дозагрузок")
    #1536 PRINT AT VAL "18",VAL "9";"\{i3}k-KONEC IGRY"
    print(" k - конец игры")
    #1540 RETURN 

def hamony():
    global ost, zerno, zahv
    # 960 REM \#017\#001hAMONIQ\#017\#000
    # 970 IF (OST<=BIN ) OR (ZERNO<=5) THEN LET POS=BIN : GO TO VAL "1030"
    if ost<=0 or zerno<5:
        pos=0
    else:
        # 980 PRINT AT VAL "19",SGN PI;"u NAS ";OST;" NEZANQTYH L\@DEJ": PRINT AT VAL "20",BIN ;"zERNA HWATIT NA ";INT (ZERNO/5);" WOINOW"
        print("У нас %d незанятых людей" % ost)
        print("Зерна хватит на %d воинов" % (zerno/5))
        while True:
            # 990 LET POS=-1: PRINT AT VAL "21",INT PI;"sKOLXKO PO[LEM W hAMONI\@?"
            pos=-1
            print("Сколько пошлём в Хамонию?")
            #1000 GO SUB INPUT: LET POS=VAL F$: PRINT AT VAL "18",BIN ;S$: GO SUB PUS: IF POS<BIN THEN GO TO VAL "990"
            pos=int(sub_input())
            fn_S()
            pus()
            if pos<0:
                continue
            #1010 IF POS>OST THEN PRINT AT VAL "20",VAL "5";"u NAS MALO L\@DEJ!!!": GO SUB KEY: GO SUB PUS: GO TO VAL "990"
            if pos>ost:
                print("У нас мало людей!!!")
                key()
                pus()
                continue
            #1020 IF POS>INT (ZERNO/5) THEN PRINT AT VAL "20",VAL "6";"u NAS MALO ZERNA!!!": GO SUB KEY: GO SUB PUS: GO TO VAL "990"
            if pos*5>zerno:
                print("У нас мало зерна!!!")
                key()
                pus()
                continue
            break
    #1030 IF POS<=NOT PI THEN GO TO VAL "1070"
    if pos>0:            
        #1040 LET NAS=NAS-POS: LET OST=OST-POS: LET ZERNO=ZERNO-POS*5
        nas-=pos
        ost-=pos
        zerno-=pos*5
        #1050 IF ZAHW>BIN THEN LET ZAHW=ZAHW+POS: GO TO VAL "1070"
        if zahv>0:
            zahv+=pos
        else:
            #1060 LET ZAHW=POS: LET SROK=TIME+FN S(4)
            zahv=pos
            srok=time+fn_S(4)
    #1070 IF ZAHW<=NOT PI THEN GO TO VAL "1140"
    if zahv<=0:
        pass
    #1080 IF SROK<>TIME THEN GO TO VAL "1140"
    elif srok!=time:
        pass
    #1090 IF ZAHW>NAS*VAL "2" THEN GO SUB POBEDA: GO TO VAL "1140"
    elif zahv>nas*2:
        pobeda()
    #1100 IF ZAHW<INT (NAS/VAL "2") THEN GO SUB PORAV: GO TO VAL "1140"
    elif zahv<nas//2:
        porazh()
    #1110 IF RND>0.5 THEN GO SUB POBEDA: GO TO VAL "1140"
    elif random()>0.5:
        pobeda()
    #1120 GO SUB PORAV
    else:
        porazh()
    #1140 RETURN 

def uborka():
    #1300 REM \#017\#001UBORKA\#017\#000
    #1305 GO SUB CLS
    #1320 IF OST>INT (ZAS/PROIZ) THEN RANDOMIZE USR VAL "47383": PRINT AT VAL "11",VAL "5";"bOLX[OE ^ISLO TUNEQDCEW": PRINT AT VAL "12",VAL "6";"RAZWRA]AET HLEBOROBOW": LET PROIZ=PROIZ-SGN PI: GO SUB KEY: GO SUB CLS
    #1330 IF (OST<NAS/VAL "15") AND (PROIZ<PREDEL) THEN RANDOMIZE USR VAL "43909": PRINT AT VAL "11",SGN PI;"pOSTOQNNYJ TRUD WYRABATYWAET";AT VAL "12",VAL "10";"SNOROWKU": LET PROIZ=PROIZ+SGN PI: GO SUB KEY: GO SUB CLS
    #1340 IF K<VAL "20" THEN PRINT AT VAL "11",VAL "4";"pLOHOE PITANIE SNIVAET": PRINT AT VAL "12",VAL "5";" PROIZWODITELXNOSTX!": LET PROIZ=PROIZ-INT (30/K): GO SUB KEY: GO SUB CLS
    #1350 IF PROIZ<=BIN THEN LET PROIZ=INT PI
    #1360 IF (K>VAL "30") AND (PROIZ<PREDEL) THEN PRINT AT VAL "11",SGN PI;"nA HORO[IH HAR^AH I RABOTAETSQ";AT VAL "12",VAL "13";"LU^[E": LET PROIZ=PROIZ+SGN PI: GO SUB KEY: GO SUB CLS
    #1370 LET UROV=SGN PI+FN S(VAL "6")-IST: LET J=FN S(VAL "21")
    #1380 IF J>=VAL "18" THEN LET UROV=VAL "10"
    #1390 IF J<=INT PI THEN LET UROV=SGN PI
    #1400 IF UROV<SGN PI THEN LET UROV=SGN PI
    #1410 IF UROV>VAL "5" THEN RANDOMIZE USR VAL "58252": PRINT AT VAL "11",VAL "7";"oTLI^NYJ UROVAJ!!!": GO SUB KEY: GO SUB CLS
    #1420 LET I=BIN : IF UROV<VAL "2" THEN LET I=FN S(INT PI)
    #1430 IF I=SGN PI THEN RANDOMIZE USR VAL "62884": PRINT AT VAL "11",INT PI;"zASUHA POGUBILA UROVAJ!!!": GO SUB KEY: GO SUB CLS
    #1440 IF I=VAL "2" THEN RANDOMIZE USR VAL "60568": PRINT AT VAL "11",BIN ;"pYLEWYE BURI POGUBILI UROVAJ!!!": GO SUB KEY: GO SUB CLS
    #1450 IF I=INT PI THEN RANDOMIZE USR VAL "59410": PRINT AT VAL "11",BIN ;"lIWNEWYE DOVDI POGUBILI UROVAJ!!": GO SUB KEY: GO SUB CLS
    #1460 LET SBOR=ZAS*UROV
    #1470 IF RND>0.7 THEN LET SAR=4+FN S(8): LET SBOR=SBOR-INT (SBOR/SAR): RANDOMIZE USR VAL "61726": PRINT AT VAL "11",SGN PI;"sARAN^A POGUBILA 1/";SAR;" UROVAQ!": GO SUB KEY: GO SUB CLS
    #1480 LET ZERNO=ZERNO+SBOR: LET J=FN S(5)
    #1490 IF J=SGN PI THEN LET KRYS=INT (ZERNO/(FN S(10)+7)): RANDOMIZE USR VAL "57094": PRINT AT VAL "11",VAL "4";"nA GOROD NAPALI KRYSY!!!": LET ZERNO=ZERNO-KRYS: GO SUB KEY: GO SUB CLS
    #1500 RETURN 
    pass

def nn():
    #1550 REM \#017\#001NN\#017\#000
    #1555 GO SUB CLS
    #1560 LET BEV=INT (RND*INT (NAS/4))
    #1570 IF (RASST<20) AND (RND>.5) THEN LET BEV=BEV+INT (RND*BEV): PRINT AT VAL "11",INT PI;"pRITOK BEVENCEW SPASA\@]IHSQ";AT VAL "12",VAL "7";"OT ZAHWAT^IKOW!!!": GO SUB KEY: GO SUB CLS
    #1580 LET NAS=NAS+BEV
    #1590 IF (K<10) OR (UMERWSEGO>NAS*10) THEN RANDOMIZE USR VAL "55936": PRINT AT VAL "11",SGN PI;"nAROD WOSSTAL PROTIW TIRANA!!!": GO SUB KEY: GO SUB CLS: GO TO VAL "1610"
    #1600 GO TO VAL "1630"
    #1610 IF (Z>(NAS-Z)/3) AND (Z<UMERGOL) THEN RANDOMIZE USR "54778": PRINT AT VAL "11",SGN PI;"nO WOJSKA PODAWILI WOSSTANIE!": LET WOSST=(NAS-Z)*INT (RND/5+0.1): LET POGIB=POGIB+WOSST: LET NAS=NAS-WOSST: PRINT AT VAL "12",VAL "5";"w ULI^NYH BOQH POLEGLO";AT VAL "13",VAL "8";WOSST;" VITELEJ": GO SUB KEY: GO SUB CLS: GO TO VAL "1630"
    #1620 PRINT AT VAL "11",VAL "4";"wOJSKA PERE[LI NA STORONU";AT VAL "12",VAL "6";"WOSSTAW[EGO NARODA": PRINT AT VAL "14",VAL "5";"\{i4}monarhiq swergnuta!!!": GO SUB KEY: GO SUB CLS: LET U=SGN PI: LET OI=BIN : GO SUB OITOG: RETURN 
    #1630 LET UMER=UMER+INT (RND*2.5/100*NAS): LET ROD=INT (RND*(4+K/20)/100*NAS)
    #1640 IF FN S(VAL "12")=SGN PI THEN LET CHUMA=INT (RND*50+VAL "5"): RANDOMIZE USR VAL "53620": PRINT AT VAL "11",INT PI;"~UMA UNESLA ";CHUMA;"% NASELENIQ!": LET UMER=UMER+INT (NAS*CHUMA/100): GO SUB KEY: GO SUB CLS
    #1650 IF FN S(VAL "100")<VAL "5" THEN RANDOMIZE USR VAL "46225": PRINT AT VAL "11",VAL "4";"dEMOGRAFI^ESKIJ WZRYW!!!": LET DEM=INT ((RND/VAL "2"+0.5)*NAS): LET ROD=ROD+DEM: GO SUB KEY: GO SUB CLS
    #1660 IF (FN S(VAL "20"))=VAL "5" THEN RANDOMIZE USR VAL "52462": PRINT AT VAL "11",VAL "6";"\{i2}pova - a - a - ar!!!": LET SGOR=INT (NAS*(RND/3+0.3)): LET SGORZER=INT (ZERNO*(RND/4+0.1)): GO SUB KEY: GO SUB CLS: GO TO VAL "1666"
    #1663 GO TO VAL "1670"
    #1666 LET UMER=UMER+SGOR: LET ZERNO=ZERNO-SGORZER: RANDOMIZE USR VAL "53620": PRINT AT VAL "11",BIN ;"w OGNE POGIBLO ";SGOR;" ^ELOWEK": PRINT AT VAL "13",BIN ;"sGORELO NA SKLADAH ";SGORZER;AT VAL "14",VAL "11";"BU[.ZERNA": GO SUB KEY: GO SUB CLS
    #1670 IF FN S(VAL "10")=VAL "2" THEN LET AGENT=AGENT+SGN PI: RANDOMIZE USR VAL "45067": PRINT AT VAL "11",SGN PI;"w GOROD PROBRALSQ DIWERSANT": GO SUB KEY: GO SUB CLS:
    #1680 IF (AGENT<=BIN ) OR (Z>=NAS/VAL "10") THEN GO TO VAL "1720"
    #1690 RANDOMIZE USR VAL "52462": PRINT AT VAL "11",VAL "2";"dIWERSIQ!!!pODOVVENY HLEBNYE";AT VAL "12",VAL "13";"SKLADY.": LET SGORZER=INT (ZERNO*(RND/3+0.3)): LET ZERNO=ZERNO-SGORZER: PRINT AT VAL "14",VAL "2";"sGORELO ";SGORZER;" BU[.ZERNA": GO SUB KEY: GO SUB CLS
    #1700 IF Z>NAS/VAL "20" THEN PRINT AT VAL "11",VAL "6";"dIWERSANT SHWA^EN!!!": LET AGENT=AGENT-SGN PI: GO SUB KEY: GO SUB CLS: GO TO VAL "1720"
    #1710 RANDOMIZE USR VAL "45067": PRINT AT VAL "11",VAL "6";"dIWERSANT SKRYLSQ!!!": GO SUB KEY: GO SUB CLS
    #1720 IF (AGENT<=BIN ) OR (Z<=NAS/VAL "2") THEN GO TO VAL "1740"
    #1730 IF RND<0.5 THEN PRINT AT VAL "11",VAL "4";"pOJMAN WRAVESKIJ AGENT!!!": LET AGENT=AGENT-SGN PI: GO SUB KEY: GO SUB CLS
    #1740 IF (K>=VAL "60") AND (NAS-Z-INT (ZAS/PROIZ)>=NAS/VAL "5") THEN RANDOMIZE USR VAL "47383": PRINT AT VAL "11",BIN ;"tUNEQDSTWU\@]IE \\LEMENTY ZANQLISX  SAMOGONOWARENIEM IZ HLEBNYH";AT VAL "13",VAL "12";"IZLI[KOW";AT VAL "14",SGN PI;"pONIVAETSQ PROIZWODITELXNOSTX!": LET PROIZ=PROIZ-VAL "2": GO SUB KEY: GO SUB CLS
    #1750 IF FN S(VAL "15")=VAL "8" THEN RANDOMIZE USR VAL "43909": PRINT AT VAL "11",VAL "2";"wNEDRENIE NOWYH ORUDIJ TRUDA    PODNQLO PROIZWODITELXNOSTX!": LET PROIZ=PROIZ+VAL "2": LET PREDEL=PREDEL+VAL "5": GO SUB KEY: GO SUB CLS
    #1760 IF FN S(VAL "50")<>VAL "50" THEN GO TO VAL "1800"
    #1770 PRINT AT VAL "11",VAL "5";"\{i6}dworcowyj pereworot!!!"
    #1780 IF (FN S(VAL "2")=SGN PI) OR (Z<NAS/VAL "10") THEN PRINT AT VAL "13",VAL "2";"wY SWERGNUTY S PRESTOLA!!!": LET U=SGN PI: LET OI=SGN PI: GO SUB KEY: GO SUB CLS: GO SUB OITOG: RETURN 
    #1790 PRINT AT VAL "13",VAL "2";"NO WERNYE wAM WOJSKA RAZBILI";AT VAL "14",VAL "11";"MQTEVNIKOW": GO SUB KEY: GO SUB CLS
    #1800 IF (TIME<=10) OR (ZAS<>ZEML) THEN GO TO VAL "1820"
    #1810 IF IST<VAL "4" THEN LET IST=IST+SGN PI: RANDOMIZE USR VAL "62884": PRINT AT VAL "11",VAL "4";"iSTO]ENIE ZEMELX SNIVAET";AT VAL "12",VAL "10";"UROVAJNOSTX": GO SUB KEY: GO SUB CLS: GO TO VAL "1830"
    #1820 IF (ZAS<ZEML/VAL "2") AND (IST>-VAL "2") THEN LET IST=IST-SGN PI: RANDOMIZE USR VAL "58252": PRINT AT VAL "11",INT PI;"oTWEDENIE BOLX[IH PLO]ADEJ";AT VAL "12",VAL "4";"POD PARY POWY[AET UROVAJ": GO SUB KEY: GO SUB CLS
    #1830 IF (FN S(VAL "15")=SGN PI) AND (AGENT>BIN ) THEN LET PROPALO=INT ((RND/VAL "5"+0.1)*ZERNO): RANDOMIZE USR VAL "47383": PRINT AT VAL "11",INT PI;"gRUPPOJ RASHITITELEJ POD";AT VAL "12",VAL "2";"PREDWODITELXSTWOM DIWERSANTA";AT VAL "13",INT PI;"POHI]ENO ";PROPALO;" BU[.ZERNA": LET ZERNO=ZERNO-PROPALO: GO SUB KEY: GO SUB CLS
    #1840 LET NAS=NAS-UMER+ROD
    #1850 RETURN 
    pass

def war():
    #1860 REM \#017\#001WTORVENIE\#017\#000
    #1870 LET RASST=RASST-FN S(VAL "5")-VAL "10"
    #1880 IF RASST<FN S(VAL "\{f0}5") THEN GO SUB ATAKA: GO TO VAL "1900"
    #1890 IF (RASST<VAL "15") AND (RND<0.1) THEN PRINT AT VAL "11",SGN PI;"wRAGI SOWER[ILI STREMITELXNYJ";AT VAL "12",VAL "9";"MAR[ - BROSOK!": GO SUB KEY: GO SUB CLS:: GO SUB ATAKA
    #1900 RETURN 
    pass

def ataka():
    #1910 REM \#017\#001ATAKA\#017\#000
    #1920 RANDOMIZE USR VAL "54778": PRINT AT VAL "11",VAL "7";"\{i3}gorod atakowan!!!": GO SUB KEY: LET I=INT (INT (10*RND)*0.1)+0.5: LET J=I+INT (INT (10*RND)*0.15)+0.5
    #1930 IF WRAGI>Z*J THEN PRINT AT VAL "13",BIN ;"gOROD PAL,WEDX EGO ZA]I]ALO MALO": PRINT AT VAL "14",VAL "13";"SOLDAT": GO SUB KEY: GO SUB CLS: LET U=SGN PI: LET OI=BIN : GO SUB OITOG: RETURN 
    #1940 IF Z*J>WRAGI THEN PRINT AT VAL "13",INT PI;"NO ATAKA OTBITA! uRA-A-A!!!"
    #1950 IF FN S(3)=SGN PI THEN PRINT AT VAL "15",INT PI;"pROIZO[LA RE[A\@]AQ BITWA!!!"
    #1960 LET POGIBZ=INT (WRAGI/3)+INT (RND*Z/6): LET POGIB=POGIB+POGIBZ: LET NAS=NAS-POGIB: LET RASST=25+FN S(20): LET WRAGI=INT (NAS/4)+INT (RND*NAS/5)
    #1965 GO TO KEY: GO SUB CLS
    #1970 RETURN 
    pass

def oitog():
    #1980 REM \#017\#001OITOG\#017\#000
    #1985 GO SUB CLS
    #1987 RANDOMIZE USR VAL "64042"
    #1990 IF OI=SGN PI THEN PRINT AT VAL "8",INT PI;"\{i5}wA[E PRAWLENIE OKON^ENO!!!\{i7}";AT VAL "10",VAL "2";"wY UPRAWLQLI STRANOJ ";TIME;" LET": PRINT " zA \\TO WREMQ UMERLO OT GOLODA";AT VAL "12",VAL "8";UMERWSEGO;" ^ELOWEK"
    #2000 LET BOG=ZEML*CENA+ZERNO
    #2010 IF (BOG>NBOG) AND (OI=1) THEN PRINT AT VAL "14",BIN ;"wY UWELI^ILI BOGATSTWO W ";INT (BOG/NBOG);" RAZ!": GO TO VAL "2030"
    #2020 IF OI=SGN PI THEN PRINT AT VAL "14",VAL "5";"wY RAZORILI STRANU!!!"
    #2030 IF OI=SGN PI THEN PRINT AT VAL "17",VAL "7";"\{i4}do swidaniq!!!": GO TO VAL "2045"
    #2040 IF OI=BIN THEN PRINT AT VAL "9",BIN ;"\{i2}tAKIH NADO GNATX IZ PRAWITELEJ!!";AT VAL "11",SGN PI;"wY EDWA PRODERVALISX U WLASTI";AT VAL "12",VAL "10";TIME;" LET": PRINT AT VAL "14",BIN ;"\{i2}I UMORILI GOLODOM ";UMERWSEGO;" ^ELOWEK": PRINT AT VAL "16",VAL "5";"\{i2}kUDA \\TO GODITSQ?!"
    #2045 GO SUB KEY
    #2050 RETURN 
    pass

def save_load():
    #4040 GO SUB CLS: RANDOMIZE USR VAL "42751": PRINT AT VAL "11",VAL "5";"1 zAGRUZKA STAROJ IGRY";AT VAL "13",VAL "5";"2 zAPISX NOWOJ IGRY";AT VAL "15",VAL "5";"3 wYHOD"
    #4050 FOR N=SGN PI TO INT PI: IF INKEY$=STR$ N THEN GO TO (VAL "4E3"+N*VAL "100")
    #4055 NEXT N: GO TO VAL "4050"
    #4100 GO SUB VAL "4110": GO TO VAL "4120"
    #4110 PRINT AT VAL "19",VAL "6";"nABERITE IMQ FAJLA.": GO SUB VAL "8": POKE VAL "23659",VAL "2": POKE VAL "23613",NOT PI: INPUT LINE F$: POKE VAL "23659",NOT PI: GO SUB VAL "6": IF LEN F$>VAL "8" OR F$="" THEN GO TO VAL "4110"
    #4112 RETURN 
    #4120 RANDOMIZE USR VAL "15619": REM : LOAD F$ DATA Q()
    #4130 LET UMER=Q(SGN PI): LET ROD=Q(VAL "2"): LET UMERGOL=Q(INT PI): LET UMERWSEGO=Q(VAL "4"): LET POGIB=Q(VAL "5"): LET PROIZ=Q(VAL "6")
    #4140 LET PREDEL=Q(VAL "7"): LET WRAGI=Q(VAL "8"): LET RASST=Q(VAL "9"): LET CENA=Q(VAL "10"): LET SBOR=Q(VAL "11"): LET NAS=Q(VAL "12")
    #4150 LET ZEML=Q(VAL "13"): LET UROV=Q(VAL "14"): LET KRYS=Q(VAL "15"): LET ZERNO=Q(VAL "16"): LET TIME=Q(VAL "17"): LET U=Q(VAL "18")
    #4160 LET BEV=Q(VAL "19"): LET AGENT=Q(VAL "20"): LET NBOG=Q(VAL "21"): LET IST=Q(VAL "22")
    #4170 GO TO VAL "4040"
    #4200 GO SUB VAL "4110"
    #4210 LET Q(SGN PI)=UMER: LET Q(VAL "2")=ROD: LET Q(INT PI)=UMERGOL: LET Q(VAL "4")=UMERWSEGO: LET Q(VAL "5")=POGIB: LET Q(VAL "6")=PROIZ
    #4220 LET Q(VAL "7")=PREDEL: LET Q(VAL "8")=WRAGI: LET Q(VAL "9")=RASST: LET Q(VAL "10")=CENA: LET Q(VAL "11")=SBOR: LET Q(VAL "12")=NAS
    #4230 LET Q(VAL "13")=ZEML: LET Q(VAL "14")=UROV: LET Q(VAL "15")=KRYS: LET Q(VAL "16")=ZERNO: LET Q(VAL "17")=TIME: LET Q(VAL "18")=U
    #4240 LET Q(VAL "19")=BEV: LET Q(VAL "20")=AGENT: LET Q(VAL "21")=NBOG: LET Q(VAL "22")=IST
    #4250 RANDOMIZE USR VAL "15619": REM : SAVE F$ DATA Q()
    #4260 GO TO VAL "4040"
    #4300 RETURN 
    pass

def start_program():
    pass

def sub_input():
    #4020 POKE VAL "23659",VAL "2": POKE VAL "23613",NOT PI: INPUT LINE F$: POKE VAL "23659",NOT PI: IF F$="" THEN LET F$="0": GO TO VAL "4026"
    while True:
        f = input()
        if f=='':
            f = '0'
        #4021 IF F$="k" OR f$="K" THEN LET OI=SGN PI: GO SUB OITOG: GO TO VAL "50"
        if f=='k' or f=='K':
            OI = 1
            oitog()
            raise
        #4022 IF F$="d" OR f$="D" THEN GO SUB VAL "4040": GO SUB VAL "120"
        if f=='d' or f=='D':
            save_load()
            start_program()
            raise
        
        #4024 FOR N=SGN PI TO LEN F$: IF CODE F$(N)<VAL "48" OR CODE F$(N)>VAL "57" THEN GO TO VAL "4020"
        #4025 NEXT N
        #4026 RETURN 
        if all(x>='0' and x<='9' for x in f):
            return f

def pus():
    #4030 PRINT AT VAL "20",BIN ;S$: RETURN 
    pass

while True:
    while True:
        #  50 GO SUB CLS: RANDOMIZE USR VAL "51304"
        cls()
        #  53 PRINT AT VAL "9",VAL "7";"\{i6}korolewstwo zerna"
        #  55 PRINT AT VAL "12",VAL "9";"\{i5}1 sTART IGRY"
        #  56 PRINT AT VAL "14",VAL "9";"\{i5}2 iNSTRUKCII"
        #  57 PRINT AT VAL "16",VAL "9";"\{i5}3 aWTORY"
        #  59 PRINT AT VAL "21",VAL "9";"\{i4}1992  mOSKWA"
        print("КОРОЛЕВСТВО ЗЕРНА")
        print("1 Старт игры")
        print("2 Инструкции")
        print("3 Авторы")
        print("1992 Москва")
    
        #  60 GO SUB KEY: IF INKEY$="1" THEN GO TO VAL "80"
        #  62 IF INKEY$="2" THEN GO SUB INSTR: GO SUB KEY: GO TO VAL "50"
        #  64 IF INKEY$="3" THEN RANDOMIZE USR VAL "48541": GO SUB KEY: GO TO VAL "50"
        #  66 GO TO VAL "60"
        def key():
            #4010 IF INKEY$<>"" THEN GO TO VAL "4012"
            #4011 GO TO VAL "4010"
            #4012 RETURN 
            pass
    
        inkey = key()
        if inkey == '1':
            break
        elif inkey == '2':
            instr()
        elif inkey == '3':
            pass # Credits
        
        break

    #  80 REM \#017\#001\#019\#001na~alxnye ustanowki\#017\#000
    # Начальные установки

    #  90 LET UMER=NOT PI: LET ROD=NOT PI: # LET UMERGOL=NOT PI: LET UMERWSEGO=NOT PI: LET ZAHW=NOT PI: LET POGIB=NOT PI: LET PROIZ=VAL "10": LET PREDEL=VAL "15"
    umer = 0
    rod = 0
    umergol = 0
    umervsego = 0
    zahv = 0
    pogib = 0
    proiz = 10
    predel = 15

    # 100 LET WRAGI=FN S(VAL "10")+VAL "25": LET RASST=FN S(VAL "10")+VAL "25": LET CENA=FN S(VAL "10")+VAL "15": LET SBOR=VAL "2100"+FN S(VAL "600"): LET NAS=VAL "80"+FN S(VAL "20"): LET ZEML=VAL "900"+FN S(VAL "200")
    vragi = fn_S(10)+25
    rasst = fn_S(10)+25
    cena = fn_S(10)+15
    sbor = 2100+fn_S(600)
    nas = 80+fn_S(20)
    zeml = 900+fn_S(200)

    # 110 LET UROV=INT (SBOR/ZEML): LET KRYS=150+FN S(VAL "200"): LET ZERNO=SBOR-KRYS: LET TIME=SGN PI: LET U=NOT PI: LET BEV=5+FN S(VAL "5"): LET AGENT=NOT PI: LET NBOG=CENA*ZEML+ZERNO: LET IST=NOT PI
    urov = int(sbor/zeml)
    krys = 150+fn_S(200)
    zerno = sbor-krys
    time = 1
    u = 0
    bezh = 5+fn_S(5)
    agent = 0
    nbog = cena*zeml+zerno
    ist = 0

    # 120 REM \#017\#001**START PROGRAM**\#017\#000
    # Start program

    # 130 IF U<>NOT PI THEN GO TO VAL "50"
    while u==0:
        # 140 LET CENA=VAL "10"+FN S(VAL "40")
        cena = 10+fn_S(40)
        # 145 REM RANDOMIZE USR VAL "42675": GO SUB CLS
        cls()
        # 150 GO SUB INFO
        info()
        # 160 LET KRYS=NOT PI: LET POGIB=NOT PI: LET UMER=NOT PI: LET ROD=NOT PI
        krys = 0
        pogib = 0
        umer = 0
        rod = 0
        # 170 IF U=NOT PI THEN GO SUB TORG
        if u==0:
            torg()
        # 180 IF U=NOT PI THEN GO SUB OHRANA
        if u==0:
            ohrana()
        # 190 IF U=NOT PI THEN GO SUB KORM
        if u==0:
            korm()
        # 200 IF U=NOT PI THEN GO SUB POSEW
        if u==0:
            posev()
        # 210 IF U=NOT PI THEN GO SUB HAMONY
        if u==0:
            hamony()
        # 220 IF U=NOT PI THEN GO SUB UBORKA
        if u==0:
            uborka()
        # 230 IF U=NOT PI THEN GO SUB NN
        if u==0:
            nn()
        # 240 IF U=NOT PI THEN GO SUB WAR
        if u==0:
            war()
        # 290 LET TIME=TIME+SGN PI: GO TO VAL "120"
        time+=1
        break
    break
