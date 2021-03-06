import random

import game_screens

from end_game_exception import EndGameException
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
            raise EndGameException(True)
        # 4022 IF F$="d" OR f$="D" THEN GO SUB VAL "4040": GO SUB VAL "120"
        if f == 'd' or f == 'D':
            save_load()
            # start_program()

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

        try:
            # 130 IF U<>NOT PI THEN GO TO VAL "50"
            while True:
                # 140 LET CENA=VAL "10"+FN S(VAL "40")
                model.land_price = 10 + randint(40)

                # 145 REM RANDOMIZE USR VAL "42675": GO SUB CLS
                device.cls()

                # 150 GO SUB INFO
                game_screens.info(device, model)

                # 160 LET KRYS=NOT PI:
                #   LET POGIB=NOT PI:
                #   LET UMER=NOT PI:
                #   LET ROD=NOT PI
                model.rats = 0
                model.dead_in_battles = 0
                model.dead_natural_cases = 0
                model.born = 0

                # 170 IF U=NOT PI THEN GO SUB TORG
                game_screens.barter(device, model)

                # 180 IF U=NOT PI THEN GO SUB OHRANA
                game_screens.guard(device, model)

                # 190 IF U=NOT PI THEN GO SUB KORM
                game_screens.feeding(device, model)

                # 200 IF U=NOT PI THEN GO SUB POSEW
                game_screens.sowing(device, model)

                # 210 IF U=NOT PI THEN GO SUB HAMONY
                game_screens.war(device, model)

                # 220 IF U=NOT PI THEN GO SUB UBORKA
                game_screens.harvest(device, model)

                # 230 IF U=NOT PI THEN GO SUB NN
                game_screens.events(device, model)

                # 240 IF U=NOT PI THEN GO SUB WAR
                game_screens.enemies.intervention(device, model)

                # 290 LET TIME=TIME+SGN PI:
                #   GO TO VAL "120"
                model.time += 1

        except EndGameException as ex:
            game_screens.game_results(device, model, ex.oi)
        break


if __name__ == "__main__":
    main(SimpleIO())
