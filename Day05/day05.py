# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 07:36:32 2019

@author: Nino
"""

import numpy as np

fname = 'input.txt'
memory = np.loadtxt(fname, delimiter=',').astype(int)


def decode_instruction(instruction):
    str_inst = str(instruction)
    opcode = int(str_inst[-2:])
    modes = []
    for i in range(3):
        try:
            modes.append(int(str_inst[-3-i]))
        except:
            modes.append(0)
    return opcode, modes


def get_value(memory, mode, parameter):
    if mode == 0:
        return memory[parameter]
    else:
        return parameter


def diagnostic_program(memory, imput, part=1):
    br = 0
    while True:
        instruction = memory[br]
        opcode, (mod1, mod2, mod3) = decode_instruction(instruction)
        if opcode == 1:
            first_value = get_value(memory, mod1, memory[br+1])
            second_value = get_value(memory, mod2, memory[br+2])
            third_value = memory[br+3]
            memory[third_value] = first_value + second_value
            br += 4
        elif opcode == 2:
            first_value = get_value(memory, mod1, memory[br+1])
            second_value = get_value(memory, mod2, memory[br+2])
            third_value = memory[br+3]
            memory[third_value] = first_value * second_value
            br += 4
        elif opcode == 3:
            parameter = memory[br+1]
            memory[parameter] = imput
            br += 2
        elif opcode == 4:
            first_value = get_value(memory, mod1, memory[br+1])
            print(first_value)
            br += 2
        if part == 2:
            if opcode == 5:
                first_value = get_value(memory, mod1, memory[br+1])
                if first_value != 0:
                    second_value = get_value(memory, mod2, memory[br+2])
                    br = second_value
                else:
                    br += 3
            elif opcode == 6:
                first_value = get_value(memory, mod1, memory[br+1])
                if first_value == 0:
                    second_value = get_value(memory, mod2, memory[br+2])
                    br = second_value
                else:
                    br += 3
            elif opcode == 7:
                first_value = get_value(memory, mod1, memory[br+1])
                second_value = get_value(memory, mod2, memory[br+2])
                third_value = memory[br+3]
                if first_value < second_value:
                    memory[third_value] = 1
                else:
                    memory[third_value] = 0
                br += 4
            elif opcode == 8:
                first_value = get_value(memory, mod1, memory[br+1])
                second_value = get_value(memory, mod2, memory[br+2])
                third_value = memory[br+3]
                if first_value == second_value:
                    memory[third_value] = 1
                else:
                    memory[third_value] = 0
                br += 4
        if opcode == 99:
            return memory

# part 1
output = diagnostic_program(memory.copy(), 1, part=1)

# part 2
output = diagnostic_program(memory.copy(), 5, part=2)
