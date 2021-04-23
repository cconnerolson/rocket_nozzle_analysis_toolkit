import numpy as np
import matplotlib.pyplot as plt

from isa import isa
import tools
import constants
import engines

# Plot thrust as a function of altitude #

alt = np.linspace(0, 47000, 50)

F1 = engines.Engine(name='F1', p_c=7000000, p_e=56000, T_c=3572, g=1.22, M=22.186, A_t=0.672, A_e=10.75, e_r=16, m_dot=2578)

thrust = []
for i in np.linspace(0, 47000, 50):
    p_atm = isa(i)
    thrust.append(tools.thrust(g=F1.g, p_a=p_atm, p_c=F1.p_c, p_e=F1.p_e, A_t=F1.A_t, T_c=F1.T_c, M=F1.M, A_e=F1.A_e))

print(thrust)
plt.plot(alt, thrust)
plt.show()
plt.close()
# Plot specific impulse as a function of altitude #
