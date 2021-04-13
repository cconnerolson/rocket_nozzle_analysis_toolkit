import numpy as np

import rocket_nozzle_analysis_toolkit.constants

R = rocket_nozzle_analysis_toolkit.constants.R
g = rocket_nozzle_analysis_toolkit.constants.g

def m_dot(A_t, p_c, T_c, g, M):
    """
    Calculates the mass flow rate through a chocked nozzle.
    :param A_t: Nozzle throat area [m]
    :param p_c: Combustion chamber stagnation pressure [Pa]
    :param T_c: Combustion chamber stagnation temperature [K]
    :param g: Gamma; ratio of specific heats
    :param M: Exhaust gas molar mass [kg mol^-1]
    :return: mass flow rate
    """
    return A_t * p_c * g * np.sqrt((2 / (g + 1)) ^ ((g + 1)/(g - 1))) / np.sqrt(g * R / M * T_c)

def thrust():
    """
    Calculates thrust
    :param A_t: Throat Area [m]

    :return:
    """
    pass


