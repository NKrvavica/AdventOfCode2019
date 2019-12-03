# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:18:46 2019

@author: Nino
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


fname = 'input.txt'
wires = pd.read_csv(fname, header=None, delimiter=',')


def get_manhatan(x1, y1, x2, y2):
    return np.abs(x1-x2) + np.abs(y1-y2)


def get_steps(x, y, value):
    return x.index(value) + y.index(value)


def move(pos, direction, length):
    if direction == 'R':
        new_pos = pos + length
        steps = list(x + pos.imag*1j for x in np.arange(pos.real+1,
                                                        new_pos.real+1))
    elif direction == 'U':
        new_pos = pos + length*1j
        steps = list(pos.real + y*1j for y in np.arange(pos.imag+1,
                                                        new_pos.imag+1))
    if direction == 'L':
        new_pos = pos - length
        steps = list(x + pos.imag*1j for x in np.arange(pos.real-1,
                                                        new_pos.real-1, -1))
    elif direction == 'D':
        new_pos = pos - length*1j
        steps = list(pos.real + y*1j for y in np.arange(pos.imag-1,
                                                        new_pos.imag-1, -1))
    return new_pos, steps


# Follow intructions
wire_steps = [[0j], [0j]]
for i, wire in wires.iterrows():
    position = 0j
    wire = wire.dropna()
    for j, path in wire.iteritems():
        direction, length = path[0], int(path[1:])
        position, steps = move(position, direction, length)
        wire_steps[i].extend(steps)

# Find intersections
intersections = set(wire_steps[0]).intersection(set(wire_steps[1]))
intersections.remove(0j)

# plot paths
plt.figure()
plt.plot(np.real(wire_steps[0]), np.imag(wire_steps[0]))
plt.plot(np.real(wire_steps[1]), np.imag(wire_steps[1]))

# part 1
min_distance = 1e6
for intersection in intersections:
    dist = get_manhatan(0, 0, intersection.real, intersection.imag)
    if dist < min_distance:
        min_distance = dist
print(min_distance)

# part 2
min_nr_steps = 1e6
for intersection in intersections:
    nr_steps = get_steps(wire_steps[0], wire_steps[1], intersection)
    if nr_steps < min_nr_steps:
        min_nr_steps = nr_steps
print(min_nr_steps)
