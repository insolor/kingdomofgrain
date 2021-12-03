from kingdomofgrain.game_model import GameModel
from kingdomofgrain.io_devices import AbstractIO
from kingdomofgrain.utils import sub_input, empty_lines


def sowing(device: AbstractIO, model: GameModel):
    # 840 REM \#017\#001POSEW\#017\#000
    # 850 LET ZAS=-1:
    #   LET UROV=NOT PI:
    #   LET SBOR=NOT PI

    model.grain_yield = 0
    model.harvest = 0

    # 860 IF (OST>NOT PI) AND (ZERNO>NOT PI) THEN
    #   GO TO VAL "880"
    # 870 RETURN
    if not (model.ost > 0 and model.grain > 0):
        return

    # 880 PRINT AT VAL "18",SGN PI;"u NAS ";ZEML;" AKROW ZEMLI":
    #   PRINT AT VAL "19",BIN ;"l\@DI MOGUT ZASEQTX ";PROIZ*OST;" AKROW":
    #   PRINT AT VAL "20",VAL "2";"zERNA HWATIT NA ";ZERNO*2;" AKROW"
    device.at(18, 1).print(f"У нас {model.land} акров земли")
    device.at(19, 0).print(f"Люди могут засеять {model.sower_productivity * model.ost} акров")
    device.at(20, 2).print(f"Зерна хватит на {int(model.grain / 0.5)} акров")

    while True:
        # 890 PRINT AT VAL "21",VAL "7";"sKOLXKO ZASEEM?"
        device.at(21, 7).print("Сколько засеем?")

        # 900 GO SUB INPUT: LET ZAS=VAL F$:
        #   PRINT AT VAL "18",BIN ;S$:
        #   GO SUB PUS:
        #   IF ZAS<BIN THEN
        #       GO TO VAL "890"
        try:
            model.zas = int(sub_input(device, model))
        except ValueError:
            model.zas = -1

        device.at(18, 0).print(64 * " ")
        empty_lines(device)
        if model.zas < 0:
            continue

        # 910 IF ZAS>ZEML THEN
        #   PRINT AT VAL "20",VAL "5";"u NAS MALO ZEMLI!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   LET ZAS=-1:
        #   GO TO VAL "890"
        if model.zas > model.land:
            device.at(20, 5).print("У нас мало земли!!!")
            device.wait_key()
            empty_lines(device)
            continue

        # 920 IF ZAS/VAL "2">ZERNO THEN
        #   PRINT AT VAL "20",VAL "4";"u NAS NE HWATIT ZERNA!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   LET ZAS=-1:
        #   GO TO VAL "890"
        if model.zas * 0.5 > model.grain:
            device.at(20, 4).print("У нас не хватит зерна!!!")
            device.wait_key()
            empty_lines(device)
            continue

        # 930 IF INT (ZAS/PROIZ)>OST THEN
        #   PRINT AT VAL "20",VAL "5";"u NAS MALO L\@DEJ!!!":
        #   GO SUB KEY:
        #   GO SUB PUS:
        #   LET ZAS=-1:
        #   GO TO VAL "890"
        if model.zas / model.sower_productivity > model.ost:
            device.at(20, 5).print("У нас мало людей!")
            device.wait_key()
            empty_lines(device)
            continue

        # 940 LET ZERNO=ZERNO-INT (ZAS/VAL "2"):
        #   LET OST=OST-INT (ZAS/PROIZ)
        model.grain -= int(model.zas * 0.5)
        model.ost -= model.zas // model.sower_productivity

        # 950 RETURN
        return
