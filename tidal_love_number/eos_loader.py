"""Equation of state module.

"""


import collections as cols
import csv
import enum as enum
import numpy as np

from scipy import interpolate

import constants_cgs as const

class Columns(enum.IntEnum):
    """ EoS file columns. """
    ENERGY_DENSITY = 0
    MASS_DENSITY = 0
    PRESSURE = 1
    BARYONIC_NUMBER = 2


class EoSValue(cols.namedtuple('EoSValue', 'energy pressure baryonic_number')):
    """
    Named tuple that represents an EoS value
    """
    pass


class EoS(object):
    """ Self explanatory. """

    def __init__(self, filename, central_energy_density):

        self.__filename = filename

        self.__central_energy_density = central_energy_density

        loader = EoSLoader(self.__filename, central_energy_density)

        loader.load_eos_file()

        interp = EoSInterpolation(loader.get_eos_list())

        self.__energy_from_pressure_function = interp.spline_energy_from_pressure()

        self.__pressure_from_energy_function = interp.spline_pressure_from_energy()

    def energy_from_pressure(self, pressure):
        """ Self explanatory. """
        # print("energy_from_pressure(%f)" % (pressure))

        return self.__energy_from_pressure_function(pressure)

    def pressure_from_energy(self, energy):
        """ Self explanatory. """

        # print("pressure_from_energy(%f)" % (energy))

        return self.__pressure_from_energy_function(energy)


class EoSLoader(object):
    """ EoS Loader. """

    __eos_list = []

    def __init__(self, filename, central_energy_density=1):

        self.__filename = filename
        self.__central_energy_density = central_energy_density

        # print("self.__central_energy_density = {}".format(self.__central_energy_density))

    def get_eos_list(self):
        """ Get eos list"""
        return self.__eos_list

    def load_eos_file(self):
        """ 
        Load eos file
        The file must be composed of 3 columns, namely
            mass density,  pressure ,  baryonic_density 
        """

        with open(self.__filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row[0].startswith('#'):
                    eos_value = EoSValue(float(
                        row[Columns.MASS_DENSITY])*const.LIGHT_SPEED**2.,
                        float(row[Columns.PRESSURE]),
                        float(row[Columns.BARYONIC_NUMBER]))

                    self.__eos_list.append(eos_value)

        # print(self.__eosList)

        # firstColumn = [row[0] for row in self.__eosList]

        # print(firstColumn)


class EoSInterpolation(object):
    """ EoS Interpolation. """

    def __init__(self, eos_list):

        self.__eos_list = eos_list

        self.__energy_values = np.asarray(
            [row[Columns.MASS_DENSITY] for row in self.__eos_list], dtype=np.float32)

        self.__pressure_values = np.asarray(
            [row[Columns.PRESSURE] for row in self.__eos_list], dtype=np.float32)

        self.__baryonic_number_values = np.asarray(
            [row[Columns.BARYONIC_NUMBER] for row in self.__eos_list], dtype=np.float32)

    def spline_energy_from_pressure(self):
        """ Self explanatory. """

        interpolated_function = interpolate.interp1d(
            self.__pressure_values[::-1], self.__energy_values[::-1])

        return interpolated_function

    def spline_pressure_from_energy(self):
        """ Self explanatory. """

        interpolated_function = interpolate.interp1d(
            self.__energy_values[::-1], self.__pressure_values[::-1])

        return interpolated_function
