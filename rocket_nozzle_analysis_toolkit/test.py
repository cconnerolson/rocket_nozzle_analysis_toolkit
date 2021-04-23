import numpy as np
import matplotlib.pyplot as plt
from isa import isa
import tools
import engines

F1 = engines.Engine(name='F1', p_c=7000000, T_c=3572, g=1.33, M=22.186, A_t=0.672, A_e=10.75, m_dot=2578)

m_dot = tools.mass_flow_rate(0.672, 7000000, 3572, 1.147, 22.186)

print(m_dot)

