from kingdomofgrain.io_devices import AbstractIO


def instr(device: AbstractIO):
    # 1510 REM \#017\#001instrukciq\#017\#000
    # 1515 GO SUB CLS
    device.cls()
    # 1520 PRINT AT NOT PI,VAL "10";"instrukciq":
    #   PRINT "  wAM PREDLAGAETSQ POPROBOWATX":
    #   PRINT " SWOI SILY W UPRAWLENII STRANOJ":
    #   PRINT "  wA[A CELX - KAK MOVNO DOLX[E":
    #   PRINT AT VAL "4",VAL "5";"PRODERVATXSQ U WLASTI."
    device.at(0, 10).print("ИНСТРУКЦИЯ")
    device.print("  Вам предлагается попробовать")
    device.print(" свои силы в управлении страной")
    device.print("  Ваша цель - как можно дольше")
    device.at(4, 5).print("продержаться у власти.")

    # 1522 PRINT AT VAL "5",VAL "8";"\{i6} u^TITE ~to:":
    #   PRINT "  oDNOMU ^ELOWEKU NUVNO W GOD":
    #   PRINT "   NE MENEE 22 BU[ELEJ ZERNA":
    #   PRINT "   ^TOBY ZASEQTX 1 AKR NUVNO":
    #   PRINT "   - 0.5 BU[ELEJ ZERNA":
    #   PRINT "   oDIN SOLDAT S'EDAET W GOD       - 5 BU[ELEJ ZERNA"
    device.at(5, 8).ink(6).print(" Учтите что:")
    device.print("  Одному человеку нужно в год")
    device.print("   не менее 22 бушелей зерна")
    device.print("   Чтобы засеять 1 акр нужно")
    device.print("   - 0.5 бушелей зерна")
    device.print("   Один солдат съедает в год")
    device.print("   - 5 бушелей зерна")

    # 1530 PRINT :
    #   PRINT "        vELAEM uspeha!!!"
    device.print()
    device.print("        Желаем УСПЕХА!!!")
    # 1534 PRINT AT VAL "15",SGN PI;"\{i3} d-W REVIME \i\n\p PLAY SPECTRUM  WHOD W MEN\@           DOZAGRUZOK"
    device.at(15, 1).ink(3).print(" d-в режиме INPUT - вход в меню\n           дозагрузок")
    # 1536 PRINT AT VAL "18",VAL "9";"\{i3}k-KONEC IGRY"
    device.at(18, 9).ink(3).print("k-конец игры")
    # 1540 RETURN
