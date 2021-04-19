import numpy as np

import rocket_nozzle_analysis_toolkit.constants

R = rocket_nozzle_analysis_toolkit.constants.R
g_0 = rocket_nozzle_analysis_toolkit.constants.g


def mass_flow_rate(A_t, p_c, T_c, g, M):
    """
    Calculates the mass flow rate through a chocked nozzle.
    :param A_t: Nozzle throat area [m]
    :param p_c: Combustion chamber stagnation pressure [Pa]
    :param T_c: Combustion chamber stagnation temperature [K]
    :param g: Gamma; specific heat ratio []
    :param M: Exhaust gas molar mass [kg mol^-1]
    :return m_dot: mass flow rate
    """
    m_dot = A_t * p_c * g * np.sqrt((2 / (g + 1))**((g + 1)/(g - 1))) \
        / np.sqrt(g * R / M * T_c)
    return m_dot


def thrust_coefficient(p_c, p_e, g, p_a=None, e_r=None):
    """
    Calculates the thrust coefficient of a choked nozzle.
    :param p_c: Combustion chamber stagnation pressure [Pa]
    :param p_e: Nozzle exit pressure [Pa]
    :param g: Gamma; specific heat ratio []
    :param p_a: Ambient pressure [Pa], if None, p_a = p_e
    :param e_r: Nozzle expansion ratio [], if None, p_a = p_e
    :return C_F: Nozzle thrust coefficient []
    """
    if (p_a is None and e_r is not None) or (p_a is not None and e_r is None):
        raise ValueError('Both p_a and er must be provided!')
    C_F = ((2 * g**2)/(g - 1)) * (2/(g + 1))**((g + 1)/(g - 1)) \
        * (1 - (p_e/p_c)**((g - 1)/g))**0.5
    if p_a is not None and e_r is not None:
        C_F += e_r * (p_e - p_a) / p_c
    return C_F


def exhaust_velocity(g, T_c, M, p_e, p_c):
    """
    Calculated the exhaust velocity out of a chocked nozzle.
    :param g: Gamma; specific heat ratio []
    :param T_c: Combustion chamber stagnation temperature [K]
    :param M: Molecular mass [kg kg-mol^-1]
    :param p_e: Nozzle exit pressure [Pa]
    :param p_c: Combustion chamber stagnation pressure [Pa]
    :return v_e: Exhaust exit velocity [m s^-1]
    """
    v_e = np.sqrt(((2 * g)/(g - 1)) * ((R * T_c)/M) * (1 - (p_e / p_c)**((g - 1)/g)))
    return v_e


def thrust(g, p_a, p_c, p_e, A_t, T_c=None, M=None, A_e=None, e_r=None):
    """
    Calculates the thrust force of an engine.
    :param g: Gamma; specific heat ratio []
    :param p_a: Ambient pressure [Pa]
    :param p_c: Combustion chamber stagnation pressure [Pa]
    :param p_e: Nozzle exit pressure [Pa]
    :param A_t: Nozzle throat area [m^2]
    :param T_c: Combustion chamber stagnation temperature [K]
    :param M: Molecular mass [kg kg-mol^-1]
    :param A_e: Nozzle exit area [m^2]
    :param e_r: Nozzle expansion ratio []
    :return T: Nozzle thrust force [N]
    """
    if (e_r is None) and (T_c is not None and M is not None and A_e is not None):
        T = mass_flow_rate(A_t, p_c, T_c, g, M) * exhaust_velocity(g, T_c, M, p_e, p_c) \
            + (p_e - p_a) * A_e
    elif e_r is not None or A_e is not None:
        if e_r is None:
            e_r = A_e / A_t
        T = A_t * p_c * thrust_coefficient(p_c, p_e, g, p_a, e_r)
    else:
        raise ValueError('e_r or T_c, M, and A_e must be provided!')
    return T


def specific_impulse(A_t, p_c, T_c, g, M, T=None, p_e=None, p_a=None, A_e=None, e_r=None):
    """
    Calculates the specific impulse of an engine.
    :param A_t: Nozzle throat area [m^2]
    :param p_c: Combustion chamber stagnation pressure [Pa]
    :param T_c: Combustion chamber stagnation temperature [K]
    :param g: Gamma; specific heat ratio []
    :param M: Molecular mass [kg kg-mol^-1]
    :param T: Thrust [N]
    :param p_e: Nozzle exit pressure [Pa]
    :param p_a: Ambient pressure [Pa]
    :param A_e: Nozzle exit area [m^2]
    :param e_r: Nozzle expansion ratio []
    :return I_sp:
    """
    m_dot = mass_flow_rate(A_t, p_c, T_c, g, M)
    if T is not None:
        I_sp = T / (m_dot * g_0)
    else:
        I_sp = thrust(g, p_a, p_c, p_e, A_t, T_c, M, A_e, e_r) / (m_dot * g_0)
    return I_sp


def nozzle_throat_area(m_dot, p_c, T_c, g, M):
    """
    Calculates nozzle throat area for choked flow.
    :param m_dot: Mass flow rate through the nozzle [kg s^-1]
    :param p_c: Combustion chamber stagnation pressure [Pa]
    :param T_c: Combustion chamber stagnation temperature [K]
    :param g: Gamma, specific heat ratio []
    :param M: Exhaust gas molar mass [kg mol^-1]
    :return A_t: Nozzle throat area [m^2]
    """
    A_t = m_dot / p_c * np.sqrt((R / M * T_c)/(g * (2/(g + 1))**((g + 1)/(g - 1))))
    return A_t
