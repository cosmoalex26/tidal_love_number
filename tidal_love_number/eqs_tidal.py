"""Tidal equations module.

This module has all equations used to calculate the tidal Love
number k_2.


Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension


.. _Google Python Style Guide:   
http://google.github.io/styleguide/pyguide.html

"""


def print_func( par ):
   print ("Hello : ", par)
   return

def k_2_politrope(n, ratio_M_R):
   
	return (3./2.)*(-0.41 + (0.56/n**(0.33)))*ratio_M_R**(-0.003)
   
   
   
   
   
   
   
   
   
   
