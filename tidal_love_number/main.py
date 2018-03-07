"""
Main module.
"""
#!/usr/bin/python


import scipy.integrate as sio

import eos_loader as eos_loader
import constants_cgs as const
import diff_eqs_tidal as diffeqs

import numpy as np
import matplotlib.pyplot as plt

import diff_eqs_tidal as det



def main():
    """ Main function. """

    file_name = '../data/mit.bag.model.B_145.CGS.csv'
    central_energy_density = 3.54741E15*const.LIGHT_SPEED**2.


    # 3.15325E+015, 6.34907E+035, 1
    energy_density_test = 3.15325E+015*const.LIGHT_SPEED**2

    mit_eos = eos_loader.EoS(
        filename=file_name,
        central_energy_density=central_energy_density)

    print "Pressure({}) = {}".format(
        energy_density_test, mit_eos.pressure_from_energy(energy_density_test))



    U0 = [0, 0]
    xs = np.linspace(0, 10, 200)
    Us = sio.odeint(det.dU_dx, U0, xs)
    ys = Us[:,0]
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Damped harmonic oscillator")
    plt.plot(xs,ys);    plt.savefig('foo.png')



if __name__ == "__main__":
    main()
