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

# construct list of positions around top face of cube
TOP_RING = [position for position_tuple in zip(constants.UP[0], constants.UP[1]) for position in position_tuple]

def _first_two_layers_easy_cases(cube: Cube, target_corner: int):
    target_edge = constants.CYCLE_OF_FACE_OF[target_corner][1][1]

    where_is_target_corner = cube.where_is(target_corner)
    where_is_target_edge = cube.where_is(target_edge)

    # reorient positions list around corner position = 0
    corner_index = next(index for index,position in enumerate(TOP_RING) if position in constants.ALL_SIDES_OF[where_is_target_corner])
    # identify edge index
    edge_index = next(index for index,position in enumerate(TOP_RING[corner_index:] + TOP_RING[:corner_index]) 
                      if position in constants.ALL_SIDES_OF[where_is_target_edge])
    
    motions = []
    alignment = constants.UP[2][ # selecting from UP face's corners
        (constants.UP[2].index(constants.CYCLE_OF_FACE_OF[target_corner][0][1]) # [0] -> face corners, [1] -> TR of same face as target corner piece
         + {1:-1,3:0,5:0,7:1}[edge_index] # relative top face offset (quarter turns) between pillar and corner to solve
         ) % len(constants.UP[2])] # wrap to within bounds
    motions.append(cube.align_corner(where_is_target_corner, alignment, 'u'))
    
    # solve pillar into place
    solves = {1:"fUF",3:"fuF",5:"RUr",7:"Rur"}
    motions.append(cube.move_algorithm(solves[edge_index], constants.FACE_OF[target_corner]))
    return "".join(motions)

def _reduce_2nd_case_to_easy(cube: Cube, where_is_target_corner: int, where_is_target_edge: int, corner_orientation: int):
    motions = []
    flattened_corner = (constants.ALL_SIDES_OF[where_is_target_corner] & set(constants.DOWN[0])).pop()
    face_of_flattened = constants.FACE_OF[constants.OTHER_SIDE_OF[flattened_corner][0]]

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

def _reduce_3rd_case_to_easy(cube: Cube, where_is_target_corner: int, where_is_target_edge: int, corner_orientation: int):
    flip = (where_is_target_edge % constants.PIECES_PER_FACE) == constants.FML

    # identify which corner to slot the target corner into
    match corner_orientation, flip:
        case 0, False: # facing up
            alignment = where_is_target_edge - constants.FMR + constants.FTR
        case 0, True:
            alignment = where_is_target_edge - constants.FML + constants.FTL
        case 1, False: # facing right
            alignment = where_is_target_edge - constants.FMR + constants.FTL
        case 1, True:
            alignment = constants.OTHER_SIDE_OF[where_is_target_edge] - constants.FMR + constants.FTL
        case 2, False: # facing left
            alignment = constants.OTHER_SIDE_OF[where_is_target_edge] - constants.FML + constants.FTR
        case 2, True:
            alignment = where_is_target_edge - constants.FML + constants.FTR
    motions = [cube.align_corner(where_is_target_corner, alignment, 'u')]
    
    # reduce
    match corner_orientation, flip:
        case 0, False: # facing up
            placement = "RUruRUr"
        case 0, True:
            placement = "Rur"
        case 1, False: # facing right
            placement = "fUF"
        case 1, True:
            placement = "fuF"
        case 2, False: # facing left
            placement = "Rur"
        case 2, True:
            placement = "RUr"
    motions.append(cube.move_algorithm(placement, (constants.FACE_OF[constants.OTHER_SIDE_OF[where_is_target_edge]] if flip else constants.FACE_OF[where_is_target_edge])))
    return motions

_4th_5th_case_solutions = {(0,1,False): ( 0, "fUUF"), # corner up
                           (0,3,False): (-1, "fUUF"),
                           (0,5,False): ( 2, "fuF"),
                           (0,7,False): ( 0, "fuFUUfuF"),
                           (0,1,True):  ( 0, "RUruuRUr"),
                           (0,3,True):  ( 2, "RUr"),
                           (0,5,True):  ( 1, "RUUr"),
                           (0,7,True):  ( 0, "RUUr"),
                           (1,3,False): ( 1, "fuF"), # corner right
                           (1,5,False): ( 1, "fUUF"),
                           (1,7,False): ( 0, "Rur"),
                           (1,1,True):  ( 1, "fUUF"),
                           (1,3,True):  (-1, "RUr"),
                           (1,7,True):  (-1, "Rur"),
                           (2,1,False): ( 1, "fUF"), # corner left
                           (2,5,False): ( 1, "fuF"),
                           (2,7,False): (-1, "RUUr"),
                           (2,1,True):  ( 0, "fUF"),
                           (2,3,True):  (-1, "RUUr"),
                           (2,5,True):  (-1, "RUr")}

def _reduce_4th_5th_case_to_easy(cube: Cube, target_corner, where_is_target_corner: int, where_is_target_edge: int, corner_orientation: int):
    # reorient positions list around corner position = 0
    corner_index = next(index for index,position in enumerate(TOP_RING) if position in constants.ALL_SIDES_OF[where_is_target_corner])
    # identify edge index
    edge_index = next(index for index,position in enumerate(TOP_RING[corner_index:] + TOP_RING[:corner_index]) 
                      if position in constants.ALL_SIDES_OF[where_is_target_edge])
    # identify edge flip
    flip = constants.FACE_OF[where_is_target_edge] == 'u'
    # extract solving algorithm and relative orientation
    key = (corner_orientation, edge_index, flip)
    if key not in _4th_5th_case_solutions:
        return ""
    offset, algorithm = _4th_5th_case_solutions.get(key)

    motions = []
    # align the corner
    alignment = constants.UP[2][ # selecting from UP face's corners
        (constants.UP[2].index(constants.CYCLE_OF_FACE_OF[target_corner][0][1]) # [0] -> face corners, [1] -> TR of same face as target corner piece
         + offset # relative top face offset (quarter turns) between pillar and corner to solve
         ) % len(constants.UP[2])] # wrap to within bounds
    motions.append(cube.align_corner(where_is_target_corner, alignment, 'u'))
    # perform algorithm
    motions.append(cube.move_algorithm(algorithm, constants.FACE_OF[target_corner]))
    return "".join(motions)

_6th_case_solutions = {(0, False):  "RUr",
                       (0, True):   "RurUfUUF",
                       (1, False):  "RuruRUr",
                       (1, True):   "RurUfuF",
                       (2, False):  "RurURUUr",
                       (2, True):   "RUruRur"}

def _reduce_6th_case_to_easy(cube: Cube, where_is_target_edge: int, corner_orientation: int, flattened_corner: int):
    flip = (where_is_target_edge % constants.PIECES_PER_FACE) == constants.FML
    return [cube.move_algorithm(_6th_case_solutions[(corner_orientation, flip)], constants.FACE_OF[constants.OTHER_SIDE_OF[flattened_corner][0]])]

def _reduce_to_first_two_layers_easy_case(cube: Cube, target_corner, where_is_target_corner: int, where_is_target_edge: int):
    corner_in_top = len(constants.ALL_SIDES_OF[where_is_target_corner] & set(constants.UP[0])) != 0
    edge_in_top = len(constants.ALL_SIDES_OF[where_is_target_edge] & set(constants.UP[1])) != 0

    # flatten corner to up/down face, then ID orientation: 0=>on face, 1=>CW around, 2=>CCW around
    flattened_corner = (constants.ALL_SIDES_OF[where_is_target_corner] & set(constants.UP[0] + constants.DOWN[0])).pop()
    corner_orientation = ([flattened_corner] + list(constants.OTHER_SIDE_OF[flattened_corner])).index(constants.OTHER_SIDE_OF[where_is_target_corner][1])

    match corner_in_top, edge_in_top:
        case False, True: # 2nd: corner in bottom, edge in top
            motions = _reduce_2nd_case_to_easy(cube, where_is_target_corner, where_is_target_edge, corner_orientation)
        case True, False: # 3rd: corner in top, edge in middle
            motions = _reduce_3rd_case_to_easy(cube, where_is_target_corner, where_is_target_edge, corner_orientation)
        case True, True: # 4th and 5th cases: both corner and edge in top
            motions = _reduce_4th_5th_case_to_easy(cube, target_corner, where_is_target_corner, where_is_target_edge, corner_orientation)
        case False, False: # 6th: corner in bottom, edge in middle (includes pillar solved but in incorrect corner)
            motions = _reduce_6th_case_to_easy(cube, where_is_target_edge, corner_orientation, flattened_corner)
    return "".join(motions)

def _first_two_layers(cube: Cube):
    if not cube.match_pattern("....f..f.....r..r.....b..b.....l..l.....u.....d.ddd.d."):
        raise ValueError("Error: Solving stage \"first two layers\": missing prerequisite")
    
    # step 0: repeat following for each 'pillar' (corner of cube, bottom layer corner and middle layer edge)
    # step 1: locate desired pillar's pieces
    # step 2: reduce cube entropy:
    #      2a: pieces are already solved: skip to next pillar
    #      2b: one or both pieces are in top layer: do nothing for now
    #      2c: no piece is in top layer, both pieces are in same pillar: do nothing for now
    #      2d: no piece is in top layer, pieces are in different pillars: raise the edge to the top layer
    # step 3: reduce cube entropy to an easy-to-solve state
    # step 4: solve

    motions = []
    for target in constants.DOWN[0]:
        target_corner = constants.OTHER_SIDE_OF[target][0]
        target_edge = constants.CYCLE_OF_FACE_OF[target_corner][1][1]

        where_is_target_corner = cube.where_is(target_corner)
        where_is_target_edge = cube.where_is(target_edge)

        if target_corner == where_is_target_corner and target_edge == where_is_target_edge:
            continue

        corner_in_top = len(constants.ALL_SIDES_OF[where_is_target_corner] & set(constants.UP[0])) != 0
        edge_in_top = len(constants.ALL_SIDES_OF[where_is_target_edge] & set(constants.UP[1])) != 0

        if not (corner_in_top or edge_in_top):
            flattened_corner = (constants.ALL_SIDES_OF[where_is_target_corner] & set(constants.DOWN[0])).pop()
            where_is_target_edge = where_is_target_edge if (where_is_target_edge % constants.PIECES_PER_FACE) == constants.FMR else constants.OTHER_SIDE_OF[where_is_target_edge]

            if constants.FACE_OF[constants.OTHER_SIDE_OF[flattened_corner][0]] != constants.FACE_OF[where_is_target_edge]:
                motions.append(cube.move_algorithm("RUr", constants.FACE_OF[where_is_target_edge]))
                where_is_target_corner = cube.where_is(target_corner)
                where_is_target_edge = cube.where_is(target_edge)
        
        motions.append(_reduce_to_first_two_layers_easy_case(cube, target_corner, where_is_target_corner, where_is_target_edge))
        motions.append(_first_two_layers_easy_cases(cube, target_corner))
    return "".join(motions)

OLL_solutions = {"11211121":"RUbRBRRurFRf", # DOTS
                 "11212111":"rFRfUUrFRFFUUF",
                 "21212101":"lRRBrBLUUlBLr",
                 "11011111":"rUUrFRfufuFuR",
                 "01110121":"RUrUrFRfUUrFRf",
                 "01010101":"LrFFlRUULrFlRUULrFFlR",
                 "01011121":"rUUFRUruFFUUFR",
                 "21110101":"FRUrUfUUfLFl",
                 
                 "20211011":"rufUfLFlFR", # LINES
                 "10211021":"RuBBDbUUBdBBUr",
                 "21201110":"FURurURurf",
                 "11201120":"lbLurURurURlBL",
                 
                 "20201010":"LurUlURUrUR", # CROSSES
                 "10201020":"RUrURurURUUr",
                 "10100010":"lURuLUr",
                 "20200020":"rUURUrUR",
                 "00102000":"rfLFRflF",
                 "00002010":"RRDrUURdrUUr",
                 "00100020":"rflFRfLF",
                 
                 "01010000":"LrflRUULrflR", # 4 CORNERS 
                 "01000100":"lRUruLrFRf",
                 
                 "20212100":"LFrFRFFl", # _|
                 "00210110":"FrfRURur",
                 "10110110":"ruRFrfUFRf",
                 "11010020":"RUUruRuRRfuFUR",
                 "10112120":"FRUruRUruf",
                 "20112110":"LflFUULLBLbL",
                 "10010120":"rUURUrURRBUbur", # |_
                 "10001111":"LFFrfRfl",
                 "20001101":"rUURRbrBrUUR",
                 "20201111":"fluLUluLUF",
                 "10102121":"rFrfRRUUbRBr",
                 "20102111":"rFRfUURRbrBr",
                 "21012020":"RUrbRBubrB", # ¯|
                 "01111010":"lbLurURlBL",
                 "00101111":"LRRfRfrFFRflR",
                 "01011020":"bRbRRURUruRBB",
                 "11102021":"LufUUfUFuFUUFul", # |¯
                 "20012120":"rLLFlFLFFlFlR",
                 "01001021":"RRUrbRuRRURBr",
                 "21200021":"lBBRBrBL",
                 
                 "00211001":"RURbrBur", # C
                 "11200100":"RUrubrFRfB",
                 
                 "11100110":"rFRUrfRFuf", # L
                 "21202100":"LfluLFlfUF",
                 "21200120":"lbLruRUlBL",
                 "11101100":"RBrLUluRbr",
                 
                 "00211100":"FURurf", # P
                 "20000111":"ruFURurfR",
                 "00112100":"LUfulULFl",
                 "10000121":"fulULF",
                 
                 "11000120":"FRUruf", # T
                 "21000110":"RUrurFRf",
                 
                 "11002001":"LUlULululBLb", # W
                 "01210010":"ruRurURURbrB",
                 
                 "01100120":"rFRUrufUR", # Z
                 "21001100":"LfluLUFul",

                 "00000000":"" # solved
}

def _orient_last_layer(cube: Cube):
    if not cube.match_pattern("...ffffff...rrrrrr...bbbbbb...llllll....u....ddddddddd"):
        raise ValueError("Error: Solving stage \"orient last layer\": missing prerequisite")
    
    # step 0: construct dict of all possible states -> associated algorithm to solve
    # step 1: decompose top layer into circle of parity indicators (0|1|2)
    # step 2: create list of 4 possible orientations [abcdefgh, cdefghab, efghabcd, ghabcdef]
    # step 3: union previous list with dict keys to extract case
    # step 4: index case within orientations to determine face to perform algorithm

    position_lists = [([position] + list(constants.OTHER_SIDE_OF[position])) 
                        if position in constants.CORNERS else 
                      [position, constants.OTHER_SIDE_OF[position]] 

                      for position in TOP_RING]
    parities = [[cube.cube_data[piece] for piece in position_tuple].index(cube.colours['u']) for position_tuple in position_lists]
    
    base_offsets = range(0, 8, 2)
    parity_strings = ["".join(str(parity) for parity in (parities[offset:] + parities[:offset])) for offset in base_offsets]
    parity_string = (OLL_solutions.keys() & set(parity_strings)).pop()
    return cube.move_algorithm(OLL_solutions[parity_string], "flbr"[parity_strings.index(parity_string)])

PLL_solutions = {"01234567":"",
                 "21430567":"rFrBBRfrBBRR",
                 "01632547":"RbRFFrBRFFRR",
                 "01254763":"RRURUrururUr",
                 "01274365":"RuRURURuruRR",
                 "05274163":"LLRRDLLRRUULLRRDLLRR",
                 "01472563":"RUrurFRRuruRUrf",
                 "27034561":"rUlUURurUURL",
                 "01452367":"RUrfRUrurFRRur",
                 "21034765":"LUUlUULfluLULFLL",
                 "21054367":"rUURUUrFRUrurfRR",
                 "43210567":"rUrubrBBubUbRBR",
                 "27614503":"RRDbUbuBdRRfUF",
                 "65230741":"ruRBBDlULuLdBB",
                 "61250743":"RRdFuFUfDRRBub",
                 "27634105":"RUrFFdLulUlDFF",
                 "01276543":"rUUrubrBBubUbRBuR",
                 "07254361":"LLRRDLLRRULrFFLLRRBBLr",
                 "47230561":"FRuruRUrfRUrurFRf",
                 "45230167":"LuRUUlUrLuRUUlUr",
                 "05634127":"rUlUURuLrUlUURuL",
                 "61432507":"RbrFRBrFFlBLFlbL"}

def _permute_last_layer(cube: Cube):
    if not cube.match_pattern("...ffffff...rrrrrr...bbbbbb...lllllluuuuuuuuuddddddddd"):
        raise ValueError("Error: Solving stage \"permute last layer\": missing prerequisite")

    # step 0: construct dict of primary (correctly aligned) states -> associated algorithm to solve
    # step 1: identify where each top face piece wants to go
    # step 2: for each possible top face rotation:
    #      2a: translate step 1 into circle of values 0-7inc for given rotation
    #      2b: determine if given orientation is present in solved states
    #      2c: apply if so, otherwise check next state
    # step 3: rotate top layer to solved state

    wants_to_go = {piece:cube.where_does_piece_go(piece) for piece in TOP_RING}

    motions = []
    for face,offset in zip("flbr", range(0,8,2)):
        flattened = "".join(str(TOP_RING.index(wants_to_go[piece])) 
                            for piece in (TOP_RING[offset:] + TOP_RING[:offset]))
        if flattened in PLL_solutions:
            motions.append(cube.move_algorithm(PLL_solutions[flattened], face))
            break
    motions.append(cube.align_edge(cube.where_is(constants.FTM), 'f', 1))
    return "".join(motions)