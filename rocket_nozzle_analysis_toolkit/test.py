import numpy as np
import matplotlib.pyplot as plt
from isa import isa
import tools
import engines


F1 = engines.Engine(name='F1', p_c=7000000, p_e=56000, T_c=3572, g=1.22, M=23.14, A_t=0.672, A_e=10.75, e_r=16, m_dot=2578)

#Thrust = tools.thrust(F1.g, p_a=101300, p_c=F1.p_c, p_e=F1.p_e, A_t=F1.A_t, T_c=F1.T_c, A_e=F1.A_e, M=F1.M)

ev = tools.exhaust_velocity(1.22, F1.T_c, F1.M, F1.p_e, F1.p_c)

print(ev)

