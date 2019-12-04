# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 06:23:14 2019

@author: Nino
"""

import numpy as np
from collections import Counter

puzzle_input = '178416-676461'
lower, upper = (puzzle_input.split('-'))
lower = int(lower)
upper = int(upper)

# part 1
nr = 0
for num in range(lower, upper+1):
    digits = [int(d) for d in str(num)]
    diff = np.diff(digits)
    if (diff >= 0).all() and (diff == 0).any():
        nr += 1
print(nr)

# part 2
nr = 0
for num in range(lower, upper+1):
    digits = [int(d) for d in str(num)]
    diff = np.diff(digits)
    if (diff >= 0).all() and 2 in Counter(digits).values():
        nr += 1
print(nr)
