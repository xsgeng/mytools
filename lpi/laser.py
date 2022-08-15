from numpy import sqrt
from scipy.constants import mu_0, c, e, m_e, pi

def a0_from_E0(E0 : float, lambda0 : float = 0.8e-6) -> float:
    omega0 = 2*pi*c/lambda0
    return E0 * e / m_e / c / omega0

def E0_from_a0(a0 : float, lambda0 : float = 0.8e-6) -> float:
    omega0 = 2*pi*c/lambda0
    return a0 * m_e * c * omega0 / e

def I_from_E0(E0 : float) -> float:
    return 0.5 * E0**2 / mu_0 / c

def I_from_a0(a0 : float, lambda0 : float = 0.8e-6) -> float:
    E0 = E0_from_a0(a0, lambda0)
    return 0.5 * E0**2 / mu_0 / c

def power(a0: float, w0 : float, lambda0 : float = 0.8e-6) -> float:
    I = I_from_a0(a0, lambda0)
    return 0.5 * pi * w0**2 * I