# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 07:36:32 2019

@author: Nino
"""

import numpy as np

fname = 'input.txt'

state = np.loadtxt(fname, delimiter=',').astype(int)


def gravity_assist(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb
    br = 0
    while True:
        opcode = memory[br]
        if opcode == 1:
            first, second, third = memory[br+1:br+4]
            memory[third] = memory[first] + memory[second]
            br += 4
        elif opcode == 2:
            first, second, third = memory[br+1:br+4]
            memory[third] = memory[first] * memory[second]
            br += 4
        elif opcode == 99:
            return memory
        else:
            print('Warning, wrong opcode')


# first part
initial_state = state.copy()
output = gravity_assist(initial_state, 12, 2)
print(output[0])


# second part
def search_inputs(state, noun_range, verb_range):
    for noun in range(noun_range):
        for verb in range(verb_range):
            initial_state = state.copy()
            output = gravity_assist(initial_state, noun, verb)
            if output[0] == 19690720:
                return output, noun, verb


output, noun, verb = search_inputs(state, 100, 100)
print(100 * noun + verb)
