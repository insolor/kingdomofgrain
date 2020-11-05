from random import random
from typing import Optional


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

        self.defenders = 0
        self.dead_natural_cases = 0
        self.born = 0
        self.dead_starvation = 0  # dead from starvation
        self.dead_total = 0  # dead total

        self.warriors = 0  # number of our warriors
        self.dead_in_battles = 0  # dead in battle

        self.sower_productivity = 10  # productivity of a sower (acres)
        self.max_sower_productivity = 15  # maximum productivity of a sower

        # 100 LET WRAGI=FN S(VAL "10")+VAL "25":
        #   LET RASST=FN S(VAL "10")+VAL "25":
        #   LET CENA=FN S(VAL "10")+VAL "15":
        #   LET SBOR=VAL "2100"+FN S(VAL "600"):
        #   LET NAS=VAL "80"+FN S(VAL "20"):
        #   LET ZEML=VAL "900"+FN S(VAL "200")
        self.enemies = fn_s(10) + 25  # enemies
        self.distance_to_enemies = fn_s(10) + 25  # distance to the enemies

        self.land_price = fn_s(10) + 15  # price of an acre of land
        self.harvest = 2100 + fn_s(600)  # harvested grain
        self.population = 80 + fn_s(20)  # population
        self.land = 900 + fn_s(200)  # land area

        # 110 LET UROV=INT (SBOR/ZEML):
        #   LET KRYS=150+FN S(VAL "200"):
        #   LET ZERNO=SBOR-KRYS:
        #   LET TIME=SGN PI:
        #   LET U=NOT PI:
        #   LET BEV=5+FN S(VAL "5"):
        #   LET AGENT=NOT PI:
        #   LET NBOG=CENA*ZEML+ZERNO:
        #   LET IST=NOT PI
        self.grain_yield = self.harvest // self.land  # yield of grain per acre of land
        self.rats = 150 + fn_s(200)  # rats (grain eaten by rats)
        self.grain = self.harvest - self.rats  # grain left
        self.time = 1  # number of a year

        self.refugees = 5 + fn_s(5)  # refugees income
        self.agent = 0  # enemy agent
        self.initial_wealth = self.wealth()  # initial wealth
        self.ist = 0

        self.feeding_per_worker = None  # Quantity of grain per worker to feed one
        self.ost = None  # unoccupied population
        self.zas = None  # sowed area

    def wealth(self):
        return self.land_price * self.land + self.grain
