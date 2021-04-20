from dataclasses import dataclass, field
from tools import *
from constants import *

@dataclass
class Engine:
    name: str
    p_c: float = 0.0
    T_c: float = 0.0
    p_e: float = 0.0
    g: float = 0.0
    M: float = 0.0
    A_t: float = 0.0
    A_e: float = 0.0
    e_r: float = 0.0
    m_dot: float = 0.0

    def __post_init__(self):
        if self.e_r is not 0.0:
            if self.A_t is 0.0 and self.m_dot is not 0.0:
                self.A_t = nozzle_throat_area(self.m_dot, self.p_c, self.T_c, self.g, self.M)
            self.A_e = self.e_r * self.A_t
        # if self.A_t is not 0.0 and self.A_e is not 0.0:
        #    self.e_r = self.A_e / self.A_t


F1 = Engine(name='F1', p_c=7000000, T_c=3572, g=1.15, M=22.186, e_r=16, m_dot=2578)

print(F1)



