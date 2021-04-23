from dataclasses import dataclass, field
import tools
from constants import *

@dataclass
class Engine:
    name: str
    p_c: float = 0.0  # Combustion chamber stagnation pressure [Pa]
    T_c: float = 0.0  # Combustion chamber stagnation temperature [K]
    p_e: float = 0.0  # Nozzle exit pressure [Pa]
    g: float = 0.0  # Gamma; specific heat ratio []
    M: float = 0.0  # Exhaust gas molar mass [kg kg-mol^-1]
    A_t: float = 0.0  # Nozzle throat area [m^2]
    A_e: float = 0.0  # Nozzle exit area [m^2]
    e_r: float = 0.0  # Nozzle expansion ratio []
    m_dot: float = 0.0  # Nozzle mass flow rate [kg s^-1]

    def __post_init__(self):
        self.A_e = self.e_r * self.A_t
        # if self.A_t is not 0.0 and self.A_e is not 0.0:
        #    self.e_r = self.A_e / self.A_t

    def thrust(self):
        T = tools.thrust(self.g, self.p_a, self.p_c, self.p_e, self.A_t, self.T_c, self.M, self.A_e, e_r=None)
        return T


F1 = Engine(name='F1', p_c=7000000, T_c=3572, g=1.15, M=22.186, A_t=0.672, A_e=10.75, e_r=16, m_dot=2578)

print(F1)



