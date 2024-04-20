"""
Algorithms as specified in https://ruwix.com/the-rubiks-cube/advanced-cfop-fridrich/
(With minor modifications)
"""

import rubik_redux.model.constants as constants
from rubik_redux.model.cube import Cube

def solve(cube: Cube):
    pass

from rubik_redux.controller.classic_solve import _bottom_cross
# TODO: IDENTIFY OPTIMIZATIONS TO REDUCE AVERAGE NUMBER OF MOVES TO SOLVE BOTTOM CROSS

def _first_two_layers_easy_cases(cube: Cube, target: int):
    pass

def _first_two_layers(cube: Cube):
    # step 0: repeat following for each 'pillar' (corner of cube, bottom layer corner and middle layer edge)
    # step 1: locate desired pillar's pieces
    # step 2: reduce cube entropy:
    #      2a: pieces are already solved: skip to next pillar
    #      2b: one or both pieces are in top layer: do nothing for now
    #      2c: no piece is in top layer, both pieces are in same pillar: do nothing for now
    #      2d: no piece is in top layer, pieces are in different pillars: raise the corner to the top layer
    # step 3: reduce cube entropy to an easy-to-solve state
    # step 4: solve
    pass