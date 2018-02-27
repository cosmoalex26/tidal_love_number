"""
Main module.
"""
#!/usr/bin/python


import eos

def main():
    """ Main function. """

    file_name = '../data/mit.bag.model.B_145.CGS.csv'

    mit_eos = eos.EoS(
        filename=file_name,
        central_energy_density=1)

    print "Pressure({}) = {}".format(1, mit_eos.pressure_from_energy(1))

if __name__ == "__main__":
    main()
