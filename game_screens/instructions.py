from io_devices.abstract_io import AbstractIO


def instr(screen: AbstractIO):
    # 1510 REM \#017\#001instrukciq\#017\#000
    # 1515 GO SUB CLS
    screen.cls()
    # 1520 PRINT AT NOT PI,VAL "10";"instrukciq":
    #   PRINT "  wAM PREDLAGAETSQ POPROBOWATX":
    #   PRINT " SWOI SILY W UPRAWLENII STRANOJ":
    #   PRINT "  wA[A CELX - KAK MOVNO DOLX[E":
    #   PRINT AT VAL "4",VAL "5";"PRODERVATXSQ U WLASTI."
    print("ИНСТРУКЦИЯ")
    print("  Вам предлагается попробовать\n свои силы в управлении страной")
    print("  Ваша цель - как можно дольше\n продержаться у власти.")
    # 1522 PRINT AT VAL "5",VAL "8";"\{i6} u^TITE ~to:":
    #   PRINT "  oDNOMU ^ELOWEKU NUVNO W GOD":
    #   PRINT "   NE MENEE 22 BU[ELEJ ZERNA":
    #   PRINT "   ^TOBY ZASEQTX 1 AKR NUVNO":
    #   PRINT "   - 0.5 BU[ELEJ ZERNA":
    #   PRINT "   oDIN SOLDAT S'EDAET W GOD       - 5 BU[ELEJ ZERNA"
    print(" Учтите, что:")
    print("   Одному человеку нужно в год")
    print("   не менее 22 бушелей зерна")
    print("   Чтобы засеять 1 акр нужно")
    print("   - 0.5 бушелей зерна")
    print("  Один солдат съедает в год")
    print("   - 5 бушелей зерна")
    # 1530 PRINT :
    #   PRINT "        vELAEM uspeha!!!"
    print("        Желаем УСПЕХА!!!")
    # 1534 PRINT AT VAL "15",SGN PI;"\{i3} d-W REVIME \i\n\p PLAY SPECTRUM  WHOD W MEN\@           DOZAGRUZOK"
    print(" d - в режиме play spectrum - вход в меню дозагрузок")
    # 1536 PRINT AT VAL "18",VAL "9";"\{i3}k-KONEC IGRY"
    print(" k - конец игры")
    # 1540 RETURN
