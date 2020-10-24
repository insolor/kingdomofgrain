from random import random

from abstract_screen import AbstractScreen
from barter import barter
from enemies import intervention
from feeding import feeding
from game_model import GameModel

# BAS file "" created by ZX-Modules

#   3 BORDER NOT PI: POKE VAL "23624",VAL "71": POKE VAL "23693",VAL "71": CLS 
#   4 GO SUB VAL "6": GO TO VAL "10"
#   6 POKE VAL "23607",VAL "196": POKE VAL "23606",VAL "104": RETURN 
#   8 POKE VAL "23607",VAL "60": POKE VAL "23606",NOT PI: RETURN 

# Список номеров строк процедур
#  10 LET INSTR=VAL "1510":
#       LET INFO=VAL "300":
#       LET TORG=VAL "500":
#       LET OHRANA=VAL "610":
#       LET KORM=VAL "700":
#       LET POSEW=VAL "840":
#       LET HAMONY=VAL "960":
#       LET UBORKA=VAL "1300":
#       LET NN=VAL "1550":
#       LET WAR=VAL "1860":
#       LET OITOG=VAL "1980":
#       LET POBEDA=VAL "1150":
#       LET PORAV=VAL "1240":
#       LET ATAKA=VAL "1910"
#  12 LET KEY=VAL "4010":
#       LET CLS=VAL "4015":
#       LET INPUT=VAL "4020"
#  14 LET PUS=VAL "4030":
#       LET S$="                                                                "
from game_results import game_results
from guard import guard
from harvest import uborka
from info import info
from main_menu import main_menu
from nn import nn
from simple_screen import SimpleScreen
from sowing import posev
from war import hamony

s = " " * 64

#  20 DIM T(VAL "3")
t = [0, 0, 0]


#  21 DEF FN S(K)=INT (RND*K-0.0000001)+SGN PI
def fn_s(k):
    return int(random() * k - 0.0000001) + 1


def save_load():
    pass


def sub_input(screen: AbstractScreen):
    # 4020 POKE VAL "23659",VAL "2":
    #   POKE VAL "23613",NOT PI:
    #   INPUT LINE F$:
    #   POKE VAL "23659",NOT PI:
    #   IF F$="" THEN
    #       LET F$="0":
    #       GO TO VAL "4026"
    while True:
        f = screen.input()
        if f == '':
            f = '0'
        # 4021 IF F$="k" OR f$="K" THEN LET OI=SGN PI: GO SUB OITOG: GO TO VAL "50"
        if f == 'k' or f == 'K':
            oi = 1
            game_results(oi)
            raise
        # 4022 IF F$="d" OR f$="D" THEN GO SUB VAL "4040": GO SUB VAL "120"
        if f == 'd' or f == 'D':
            save_load()
            # start_program()
            raise

        # 4024 FOR N=SGN PI TO LEN F$: IF CODE F$(N)<VAL "48" OR CODE F$(N)>VAL "57" THEN GO TO VAL "4020"
        # 4025 NEXT N
        # 4026 RETURN
        if all('0' <= x <= '9' for x in f):
            return f


def empty_lines(screen: AbstractScreen):
    # 4030 PRINT AT VAL "20",BIN ;S$: RETURN
    screen.print(s)
    pass


def main(screen: AbstractScreen):
    while True:
        main_menu(screen)

        #  80 REM \#017\#001\#019\#001na~alxnye ustanowki\#017\#000
        # Начальные установки
        model = GameModel()

        # 120 REM \#017\#001**START PROGRAM**\#017\#000
        # Start program

        # 130 IF U<>NOT PI THEN GO TO VAL "50"
        while model.u is None:
            # 140 LET CENA=VAL "10"+FN S(VAL "40")
            model.cena = 10 + fn_s(40)
            # 145 REM RANDOMIZE USR VAL "42675": GO SUB CLS
            screen.cls()
            # 150 GO SUB INFO
            info(screen, model)
            # 160 LET KRYS=NOT PI: LET POGIB=NOT PI: LET UMER=NOT PI: LET ROD=NOT PI
            model.krys = 0
            model.pogib = 0
            model.umer = 0
            model.rod = 0

            # 170 IF U=NOT PI THEN GO SUB TORG
            if model.u is None:
                barter(screen, model)

            # 180 IF U=NOT PI THEN GO SUB OHRANA
            if model.u is None:
                guard(screen, model)

            # 190 IF U=NOT PI THEN GO SUB KORM
            if model.u is None:
                feeding(screen, model)

            # 200 IF U=NOT PI THEN GO SUB POSEW
            if model.u is None:
                posev(screen, model)

            # 210 IF U=NOT PI THEN GO SUB HAMONY
            if model.u is None:
                hamony()

            # 220 IF U=NOT PI THEN GO SUB UBORKA
            if model.u is None:
                uborka()

            # 230 IF U=NOT PI THEN GO SUB NN
            if model.u is None:
                nn(model)

            # 240 IF U=NOT PI THEN GO SUB WAR
            if model.u is None:
                intervention()

            # 290 LET TIME=TIME+SGN PI:
            #   GO TO VAL "120"
            model.time += 1

        game_results(screen, model, model.u)
        break


if __name__ == "__main__":
    main(SimpleScreen())
