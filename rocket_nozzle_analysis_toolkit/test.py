from rocket_nozzle_analysis_toolkit.tools import alt2press
import numpy as np
import matplotlib.pyplot as plt
from isa import isa
import tools
import engines

F1 = engines.Engine(name='F1', p_c=7000000, T_c=3572, g=1.33, M=22.186, A_t=0.672, A_e=10.75, m_dot=2578)

p_atm=101300
thrust = tools.thrust(g=F1.g, p_a=p_atm, p_c=F1.p_c, p_e=F1.p_e, A_t=F1.A_t, m_dot=F1.m_dot, T_c=F1.T_c, M=F1.M, e_r=F1.e_r, A_e=F1.A_e)

print(thrust)