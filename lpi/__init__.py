from scipy.constants import c, e, m_e, epsilon_0, pi
from numpy import sqrt
from . import laser, cmap, fbpic, epoch, smilei

def nc(lambda0 : float) -> float:
    omega0 = 2*pi*c/lambda0
    return epsilon_0 * m_e * omega0**2 / e**2

def Pc(ne : float, nc : float) -> float:
    return 17 * (nc/ne) * 1e9 # W

def matched_n0(lambda0 : float, a0 : float, w0 : float) -> float:
    nc_ = nc(lambda0)
    return 1/pi**2 * a0 * lambda0**2 / w0**2 * nc_