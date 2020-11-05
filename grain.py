import random

import game_screens

from io_devices import AbstractIO, SimpleIO
from game_model import GameModel

# BAS file "" created by ZX-Modules

#   3 BORDER NOT PI: POKE VAL "23624",VAL "71": POKE VAL "23693",VAL "71": CLS 
#   4 GO SUB VAL "6": GO TO VAL "10"
#   6 POKE VAL "23607",VAL "196": POKE VAL "23606",VAL "104": RETURN 
#   8 POKE VAL "23607",VAL "60": POKE VAL "23606",NOT PI: RETURN


#  21 DEF FN S(K)=INT (RND*K-0.0000001)+SGN PI
def randint(k):
    return random.randint(1, k)


def save_load():
    pass


def sub_input(device: AbstractIO, model: GameModel):
    # 4020 POKE VAL "23659",VAL "2":
    #   POKE VAL "23613",NOT PI:
    #   INPUT LINE F$:
    #   POKE VAL "23659",NOT PI:
    #   IF F$="" THEN
    #       LET F$="0":
    #       GO TO VAL "4026"
    while True:
        f = device.input()
        if f == '':
            f = '0'
        # 4021 IF F$="k" OR f$="K" THEN
        #   LET OI=SGN PI:
        #   GO SUB OITOG:
        #   GO TO VAL "50"  # to main menu
        if f == 'k' or f == 'K':
            model.oi = True
            raise
        # 4022 IF F$="d" OR f$="D" THEN GO SUB VAL "4040": GO SUB VAL "120"
        if f == 'd' or f == 'D':
            save_load()
            # start_program()
            raise

        # 4024 FOR N=SGN PI TO LEN F$:
        #   IF CODE F$(N)<VAL "48" OR CODE F$(N)>VAL "57" THEN GO TO VAL "4020"
        # 4025 NEXT N
        # 4026 RETURN
        if f.isdecimal():
            return f


def empty_lines(device: AbstractIO):
    # 4030 PRINT AT VAL "20",BIN ;S$: RETURN
    device.at(20, 0).print(" " * 64)


def main(device: AbstractIO):
    while True:
        game_screens.main_menu(device)  # 50

        #  80 REM \#017\#001\#019\#001na~alxnye ustanowki\#017\#000
        # Начальные установки
        model = GameModel()

        # 120 REM \#017\#001**START PROGRAM**\#017\#000
        # Start program

        # 130 IF U<>NOT PI THEN GO TO VAL "50"
        while not model.u:
            # 140 LET CENA=VAL "10"+FN S(VAL "40")
            model.cena = 10 + randint(40)

            # 145 REM RANDOMIZE USR VAL "42675": GO SUB CLS
            device.cls()

            # 150 GO SUB INFO
            game_screens.info(device, model)

            # 160 LET KRYS=NOT PI:
            #   LET POGIB=NOT PI:
            #   LET UMER=NOT PI:
            #   LET ROD=NOT PI
            model.krys = 0
            model.pogib = 0
            model.umer = 0
            model.rod = 0

            # 170 IF U=NOT PI THEN GO SUB TORG
            if not model.u:
                game_screens.barter(device, model)

            # 180 IF U=NOT PI THEN GO SUB OHRANA
            if not model.u:
                game_screens.guard(device, model)

            # 190 IF U=NOT PI THEN GO SUB KORM
            if not model.u:
                game_screens.feeding(device, model)

            # 200 IF U=NOT PI THEN GO SUB POSEW
            if not model.u:
                game_screens.sowing(device, model)

            # 210 IF U=NOT PI THEN GO SUB HAMONY
            if not model.u:
                game_screens.war(device, model)

            # 220 IF U=NOT PI THEN GO SUB UBORKA
            if not model.u:
                game_screens.harvest(device, model)

            # 230 IF U=NOT PI THEN GO SUB NN
            if not model.u:
                game_screens.events(device, model)

            # 240 IF U=NOT PI THEN GO SUB WAR
            if not model.u:
                game_screens.enemies.intervention(device, model)

            # 290 LET TIME=TIME+SGN PI:
            #   GO TO VAL "120"
            model.time += 1

        game_screens.game_results(device, model)
        break


if __name__ == "__main__":
    main(SimpleIO())
