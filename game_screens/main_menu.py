from io_devices.abstract_io import AbstractIO
from game_screens.instructions import instr


def main_menu(screen: AbstractIO):
    while True:
        #  50 GO SUB CLS: RANDOMIZE USR VAL "51304"
        screen.cls()
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

        inkey = screen.key()
        if inkey == '1':
            break
        elif inkey == '2':
            instr()
        elif inkey == '3':
            pass  # Credits