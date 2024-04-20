"""
Algorithms as specified in https://ruwix.com/the-rubiks-cube/advanced-cfop-fridrich/
(With minor modifications)
"""

import rubik_redux.model.constants as constants
from rubik_redux.model.cube import Cube
import itertools

def solve(cube: Cube):
    pass

from rubik_redux.controller.classic_solve import _bottom_cross
# TODO: IDENTIFY OPTIMIZATIONS TO REDUCE AVERAGE NUMBER OF MOVES TO SOLVE BOTTOM CROSS

def _first_two_layers_easy_cases(cube: Cube, target: int):
    target_corner = constants.OTHER_SIDE_OF[target][0] # target is on the bottom face, OTHER_SIDE_OF->[0] -> most-clockwise of the other faces
    target_edge = constants.CYCLE_OF_FACE_OF[target_corner][1][1] # [1] -> face edges, [1] -> MR of same face as target corner piece

    where_is_target_corner = cube.where_is(target_corner)
    where_is_target_edge = cube.where_is(target_edge)
    
    # if the target edge is on the up face, it is a RHS solve
    RHS_flag = constants.FACE_OF[where_is_target_edge] == 'u'

    # 'unwrap' the top face to determine if the corner and edge are together or not
    # construct check set outside of loop to reduce where_is calls
    targets = constants.ALL_SIDES_OF[where_is_target_corner] | constants.ALL_SIDES_OF[where_is_target_edge]
    # clockwise around up face from TL to ML
    positions = list(itertools.chain(*list(zip(constants.UP[0], constants.UP[1]))))
    # identify the positions occupied by the target pieces
    presence = [index for index,position in enumerate(positions) if position in targets]
    # determine if they are consecutive values (together)
    together_flag = presence[0] + 1 == presence[1] or (presence[1] + 1) % len(positions) == presence[0]
    
    motions = []
    # if pieces are apart, align corner with pillar
    # if pieces are together: align corner 1 quarter turn from pillar, CW if RHS, CCW if LHS
    offset = 0 if not together_flag else 1 if RHS_flag else -1
    alignment = constants.CYCLE_OF_FACE_OF[target_corner][0][1] # [0] -> face corners, [1] -> TR of same face as target corner piece
    alignment = constants.UP[2].index(alignment)
    alignment += offset
    alignment %= len(constants.UP[2])
    motions.append(cube.align_corner(where_is_target_corner, constants.UP[2][alignment], 'u'))
    
    match RHS_flag, together_flag:
        case True, True:    # RHS together
            motions.append(cube.move_algorithm("Rur", constants.FACE_OF[target_corner]))
        case True, False:   # RHS apart
            motions.append(cube.move_algorithm("RUr", constants.FACE_OF[target_corner]))
        case False, True:   # LHS together
            motions.append(cube.move_algorithm("fUF", constants.FACE_OF[target_corner]))
        case False, False:  # LHS apart
            motions.append(cube.move_algorithm("fuF", constants.FACE_OF[target_corner]))
    return "".join(motions)

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