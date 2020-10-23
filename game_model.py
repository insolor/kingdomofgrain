from random import random


def fn_s(k):
    return int(random() * k - 0.0000001) + 1


class GameModel:
    def __init__(self):
        #  90 LET UMER=NOT PI:
        #   LET ROD=NOT PI:
        #   LET UMERGOL=NOT PI:
        #   LET UMERWSEGO=NOT PI:
        #   LET ZAHW=NOT PI:
        #   LET POGIB=NOT PI:
        #   LET PROIZ=VAL "10":
        #   LET PREDEL=VAL "15"

        self.umer = 0
        self.rod = 0
        self.umergol = 0
        self.umervsego = 0
        self.zahv = 0
        self.pogib = 0
        self.proiz = 10
        self.predel = 15

        # 100 LET WRAGI=FN S(VAL "10")+VAL "25":
        #   LET RASST=FN S(VAL "10")+VAL "25":
        #   LET CENA=FN S(VAL "10")+VAL "15":
        #   LET SBOR=VAL "2100"+FN S(VAL "600"):
        #   LET NAS=VAL "80"+FN S(VAL "20"):
        #   LET ZEML=VAL "900"+FN S(VAL "200")
        self.vragi = fn_s(10) + 25
        self.rasst = fn_s(10) + 25
        self.cena = fn_s(10) + 15
        self.sbor = 2100 + fn_s(600)
        self.nas = 80 + fn_s(20)
        self.zeml = 900 + fn_s(200)

        # 110 LET UROV=INT (SBOR/ZEML):
        #   LET KRYS=150+FN S(VAL "200"):
        #   LET ZERNO=SBOR-KRYS:
        #   LET TIME=SGN PI:
        #   LET U=NOT PI:
        #   LET BEV=5+FN S(VAL "5"):
        #   LET AGENT=NOT PI:
        #   LET NBOG=CENA*ZEML+ZERNO:
        #   LET IST=NOT PI
        self.urozh = self.sbor // self.zeml
        self.krys = 150 + fn_s(200)
        self.zerno = self.sbor - self.krys
        self.time = 1
        self.u = None
        self.bezh = 5 + fn_s(5)
        self.agent = 0
        self.nbog = self.cena * self.zeml + self.zerno
        self.ist = 0
