from kingdomofgrain.end_game_exception import EndGameException
from kingdomofgrain.game_model import GameModel
from kingdomofgrain.io_devices import AbstractIO


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