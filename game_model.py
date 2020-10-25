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

        self.z = None  # number of defenders
        self.umer = 0  # dead from natural causes
        self.rod = 0  # born
        self.umergol = 0  # dead from starvation
        self.umervsego = 0  # dead total
        self.zahv = 0  # captured by enemies
        self.pogib = 0  # dead in battle

        self.proiz = 10  # basic productivity of a sower
        self.predel = 15  # maximum productivity of a sower

        # 100 LET WRAGI=FN S(VAL "10")+VAL "25":
        #   LET RASST=FN S(VAL "10")+VAL "25":
        #   LET CENA=FN S(VAL "10")+VAL "15":
        #   LET SBOR=VAL "2100"+FN S(VAL "600"):
        #   LET NAS=VAL "80"+FN S(VAL "20"):
        #   LET ZEML=VAL "900"+FN S(VAL "200")
        self.vragi = fn_s(10) + 25  # enemies
        self.rasst = fn_s(10) + 25  # distance to the enemies

        self.cena = fn_s(10) + 15  # price of an acre of land
        self.sbor = 2100 + fn_s(600)  # harvested grain
        self.nas = 80 + fn_s(20)  # population
        self.zeml = 900 + fn_s(200)  # land area

        # 110 LET UROV=INT (SBOR/ZEML):
        #   LET KRYS=150+FN S(VAL "200"):
        #   LET ZERNO=SBOR-KRYS:
        #   LET TIME=SGN PI:
        #   LET U=NOT PI:
        #   LET BEV=5+FN S(VAL "5"):
        #   LET AGENT=NOT PI:
        #   LET NBOG=CENA*ZEML+ZERNO:
        #   LET IST=NOT PI
        self.urozh = self.sbor // self.zeml  # yield of grain per acre of land
        self.krys = 150 + fn_s(200)  # rats (grain eaten by rats)
        self.zerno = self.sbor - self.krys  # grain left
        self.time = 1  # number of a year
        self.u = False
        self.bezh = 5 + fn_s(5)  # refugees income
        self.agent = 0  # enemy agent
        self.nbog = self.cena * self.zeml + self.zerno  # initial wealth
        self.ist = 0

        self.k = None  #
        self.ost = None  # unoccupied population
        self.zas = None  # sowed area
        self.oi = None
