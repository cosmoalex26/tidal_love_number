"""Tidal differential equations module.

"""
import math
import numpy as np

from scipy.integrate import odeint

def dU_dx(U, x):
    return [U[1], -2*U[1] - 2*U[0] + np.cos(2*x)]

def d_phi_dr(radius, epsilon, pressure, dp_dr):
    """ dPhi_dr """
    return -dp_dr / (epsilon + pressure)

def d_pressure_dr(radius, epsilon, pressure, mass_r):
    """ d_pressure_dr """
    return -(epsilon + pressure) * \
        (mass_r + 4. * math.pi * radius**3. * pressure)/(radius*(radius - 2. * mass_r))

def d_mass_dr(radius, epsilon):
    """ d_mass_dr """
    return 4. * math.pi * radius**2. * epsilon

def d_h_dr(radius, beta):
    """ d_h_dr """
    return beta

def d_beta_dr(radius, beta):
    """ d_beta_dr """
    return beta

