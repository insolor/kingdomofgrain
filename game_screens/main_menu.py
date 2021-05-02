from io_devices import AbstractIO
from .instructions import instr


def main_menu(device: AbstractIO):
    while True:
        #  50 GO SUB CLS: RANDOMIZE USR VAL "51304"
        device.cls()
        device.show_image("castle")

        #  53 PRINT AT VAL "9",VAL "7";"\{i6}korolewstwo zerna"
        #  55 PRINT AT VAL "12",VAL "9";"\{i5}1 sTART IGRY"
        #  56 PRINT AT VAL "14",VAL "9";"\{i5}2 iNSTRUKCII"
        #  57 PRINT AT VAL "16",VAL "9";"\{i5}3 aWTORY"
        #  59 PRINT AT VAL "21",VAL "9";"\{i4}1992  mOSKWA"
        device.at(9, 7).ink(6).print("КОРОЛЕВСТВО ЗЕРНА")
        device.at(12, 9).ink(5).print("1 Старт игры")
        device.at(14, 9).ink(5).print("2 Инструкции")
        device.at(16, 9).ink(5).print("3 Авторы")
        device.at(21, 9).ink(4).print("1992 Москва")

        #  60 GO SUB KEY: IF INKEY$="1" THEN GO TO VAL "80"
        #  62 IF INKEY$="2" THEN GO SUB INSTR: GO SUB KEY: GO TO VAL "50"
        #  64 IF INKEY$="3" THEN RANDOMIZE USR VAL "48541": GO SUB KEY: GO TO VAL "50"
        #  66 GO TO VAL "60"

        inkey = device.wait_key()
        if inkey == '1':
            break
        elif inkey == '2':
            instr(device)
        elif inkey == '3':
            device.show_image("credits")
