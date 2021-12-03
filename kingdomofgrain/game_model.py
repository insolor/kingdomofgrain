from dataclasses import dataclass, field
from random import randint
from typing import Optional


def fn_s(k):
    return randint(1, k)


@dataclass
class GameModel:
    defenders: int = 0

    # 100 LET WRAGI=FN S(VAL "10")+VAL "25":
    #   LET RASST=FN S(VAL "10")+VAL "25":
    #   LET CENA=FN S(VAL "10")+VAL "15":
    #   LET SBOR=VAL "2100"+FN S(VAL "600"):
    #   LET NAS=VAL "80"+FN S(VAL "20"):
    #   LET ZEML=VAL "900"+FN S(VAL "200")
    enemies: int = field(default_factory=lambda: fn_s(10) + 25)  # enemies
    distance_to_enemies: int = field(default_factory=lambda: fn_s(10) + 25)  # distance to the enemies

    land_price: int = field(default_factory=lambda: fn_s(10) + 15)  # price of an acre of land
    harvest: int = field(default_factory=lambda: 2100 + fn_s(600))  # harvested grain
    population: int = field(default_factory=lambda: 80 + fn_s(20))  # population
    land: int = field(default_factory=lambda: 900 + fn_s(200))  # land area

    # 110 LET UROV=INT (SBOR/ZEML):
    #   LET KRYS=150+FN S(VAL "200"):
    #   LET ZERNO=SBOR-KRYS:
    #   LET TIME=SGN PI:
    #   LET U=NOT PI:
    #   LET BEV=5+FN S(VAL "5"):
    #   LET AGENT=NOT PI:
    #   LET NBOG=CENA*ZEML+ZERNO:
    #   LET IST=NOT PI
    grain_yield: int = -1  # yield of grain per acre of land
    rats: int = field(default_factory=lambda: 150 + fn_s(200))  # rats (grain eaten by rats)
    grain: int = -1  # grain left
    time: int = 1  # current year

    refugees: int = field(default_factory=lambda: 5 + fn_s(5))  # refugees income
    agent: int = 0  # enemy agent flag  # FIXME: specify possible values
    ist: int = 0  # TODO: restore meaning of the field

    feeding_per_worker: Optional[int] = None  # Quantity of grain per worker to feed one
    ost: Optional[int] = None  # unoccupied population
    zas: Optional[int] = None  # sowed area
    initial_wealth: Optional[int] = 0

    # Fields where the game stats are stored

    #  90 LET UMER=NOT PI:
    #   LET ROD=NOT PI:
    #   LET UMERGOL=NOT PI:
    #   LET UMERWSEGO=NOT PI:
    #   LET ZAHW=NOT PI:
    #   LET POGIB=NOT PI:
    #   LET PROIZ=VAL "10":
    #   LET PREDEL=VAL "15"

    dead_natural_cases: int = 0
    born: int = 0
    dead_starvation: int = 0  # dead from starvation
    dead_total: int = 0  # dead total

    warriors: int = 0  # number of our warriors
    dead_in_battles: int = 0  # dead in battle

    sower_productivity: int = 10  # productivity of a sower (acres)
    max_sower_productivity: int = 15  # maximum productivity of a sower

    def __post__init__(self):
        self.initial_wealth = self.wealth()
        self.grain_yield = self.harvest // self.land
        self.grain = self.harvest - self.rats

    def wealth(self):
        return self.land_price * self.land + self.grain
