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

    # determine if the corner and edge are together or not
    targets = constants.ALL_SIDES_OF[where_is_target_corner] | constants.ALL_SIDES_OF[where_is_target_edge] # positions of our target pieces
    # clockwise around up face from TL to ML, zip the up face corners and edges then flatten, add TL again to simplify adjacency check (ML->TL)
    positions = [position for position_tuple in zip(constants.UP[0], constants.UP[1]) for position in position_tuple] + [constants.UP[0][0]]
    # identify the positions occupied by the target pieces and determine if they are consecutive values (together)
    together_flag = any(x+1==y for x,y in itertools.pairwise(index for index,position in enumerate(positions) if position in targets))
    
    motions = []

    alignment = constants.UP[2][ # selecting from UP face's corners
        (constants.UP[2].index(constants.CYCLE_OF_FACE_OF[target_corner][0][1]) # [0] -> face corners, [1] -> TR of same face as target corner piece
         + (0 if not together_flag else 1 if RHS_flag else -1) # relative top face offset (quarter turns) between pillar and corner to solve
         ) % len(constants.UP[2])] # wrap to within bounds
    motions.append(cube.align_corner(where_is_target_corner, alignment, 'u'))
    
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

def _reduce_2nd_case_to_easy(cube: Cube, where_is_target_corner, where_is_target_edge):
    motions = []
    flattened_corner = (constants.ALL_SIDES_OF[where_is_target_corner] & set(constants.DOWN[0])).pop()
    face_of_flattened = constants.FACE_OF[constants.OTHER_SIDE_OF[flattened_corner][0]]

    # read corner orientation: 0=>down, 1=>left, 2=>right
    # list version of ALL_SIDES_OF => index of where the down-face would be => orientation
    corner_orientation = ([flattened_corner] + list(constants.OTHER_SIDE_OF[flattened_corner])).index(constants.OTHER_SIDE_OF[where_is_target_corner][1])

    # LHS or RHS solve (which side the edge should go on)
    RHS = where_is_target_edge in constants.UP[1]

    # identify which face to align edge to
    cycle = [constants.FACE_OF[piece] for piece in constants.DOWN[3]] # construct 'loop' of faces
    alignment = cycle[(((2 if RHS else -1) if corner_orientation==0 else (1 if RHS else 0)) # offset
                        + cycle.index(face_of_flattened) # shift by corner location
                        ) % len(cycle)] # wrap to fit cycle
    
    motions.append(cube.align_edge(where_is_target_edge, alignment, variant=0 if RHS else 1))
    match corner_orientation, RHS:
        case 0, False:
            placement = "Rur"
        case 0, True:
            placement = "fUF"
        case 1, False:
            placement = "fuF"
        case 1, True:
            placement = "Rur"
        case 2, False:
            placement = "fUF"
        case 2, True:
            placement = "RUr"
    motions.append(cube.move_algorithm(placement, face_of_flattened))
    return motions

def _reduce_to_first_two_layers_easy_case(cube: Cube, target: int):
    target_corner = constants.OTHER_SIDE_OF[target][0] # target is on the bottom face, OTHER_SIDE_OF->[0] -> most-clockwise of the other faces
    target_edge = constants.CYCLE_OF_FACE_OF[target_corner][1][1] # [1] -> face edges, [1] -> MR of same face as target corner piece

    where_is_target_corner = cube.where_is(target_corner)
    where_is_target_edge = cube.where_is(target_edge)

    corner_in_top = len(constants.ALL_SIDES_OF[where_is_target_corner] & set(constants.UP[0])) != 0
    edge_in_top = len(constants.ALL_SIDES_OF[where_is_target_edge] & set(constants.UP[1])) != 0
    fourth_not_fifth = where_is_target_corner in constants.UP[0]

    match corner_in_top, edge_in_top, fourth_not_fifth:
        case False, True, _: # 2nd: corner in bottom, edge in top
            motions = _reduce_2nd_case_to_easy(cube, where_is_target_corner, where_is_target_edge)
        case True, False, _: # 3rd: corner in top, edge in middle
            motions = []
        case True, True, True: # 4th: corner 'pointing outwards', edge in top
            motions = []
        case True, True, False: # 5th: corner 'pointing upwards', edge in top
            motions = []
        case False, False, _: # 6th: corner in bottom, edge in middle (includes pillar solved but in incorrect corner)
            motions = []
    return "".join(motions)

def _first_two_layers(cube: Cube):
    # step 0: repeat following for each 'pillar' (corner of cube, bottom layer corner and middle layer edge)
    # step 1: locate desired pillar's pieces
    # step 2: reduce cube entropy:
    #      2a: pieces are already solved: skip to next pillar
    #      2b: one or both pieces are in top layer: do nothing for now
    #      2c: no piece is in top layer, both pieces are in same pillar: do nothing for now
    #      2d: no piece is in top layer, pieces are in different pillars: raise the edge to the top layer
    # step 3: reduce cube entropy to an easy-to-solve state
    # step 4: solve
    pass