from random import randint

from . import game_screens
from .end_game_exception import EndGameException
from .game_model import GameModel
from .io_devices import AbstractIO


# BAS file "" created by ZX-Modules

#   3 BORDER NOT PI: POKE VAL "23624",VAL "71": POKE VAL "23693",VAL "71": CLS 
#   4 GO SUB VAL "6": GO TO VAL "10"
#   6 POKE VAL "23607",VAL "196": POKE VAL "23606",VAL "104": RETURN 
#   8 POKE VAL "23607",VAL "60": POKE VAL "23606",NOT PI: RETURN

#  21 DEF FN S(K)=INT (RND*K-0.0000001)+SGN PI
# def s(n): return random.randint(1, n)


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
                model.land_price = randint(10, 50)

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
