# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:00:30 2019

@author: NinoK
"""

import numpy as np

fname = 'input.txt'
mass = np.loadtxt(fname)


def comp_fuel(mass):
    fuel = np.floor(mass / 3) - 2
    fuel[fuel < 0] = 0
    return fuel


# part 1
fuel = comp_fuel(mass)
sum_of_fuel = fuel.sum()
print(sum_of_fuel)

# part 2
while True:
    fuel = comp_fuel(fuel)
    sum_of_fuel += fuel.sum()
    if fuel.all() == 0:
        break
print(sum_of_fuel)
