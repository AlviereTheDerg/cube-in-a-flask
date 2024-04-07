
import rubik_redux.model.constants as constants
from rubik_redux.model.cube import Cube

def solve(cube: Cube):
    motions = []
    motions.append(_bottom_cross(cube))
    motions.append(_bottom_layer(cube))
    motions.append(_bottom_two_layers(cube))
    motions.append(_top_cross(cube))
    motions.append(_top_layer(cube))
    return "".join(motions)

def _bottom_cross(cube: Cube):
    motions = []
    for target in [constants.DTM, constants.DML, constants.DMR, constants.DBM]:
        current_location = cube.where_is(target)
        if current_location == target:
            continue # if it is already in place, do nothing
        
        # if the piece is on the top/bottom layer, facing out, move it for next step
        match constants.FACE_OF[constants.OTHER_SIDE_OF[current_location]]:
            case 'd': # no need to worry about fixing the -BM
                motions.append(constants.FACE_OF[current_location])
                cube.rotate(constants.FACE_OF[current_location])
                current_location = cube.where_is(target)
            case 'u': # needs to fix the -BM
                motions.append(cube.move_algorithm('fLFl', constants.FACE_OF[current_location]))
                current_location = cube.where_is(target)
        
        # if a piece is ringing a (non-up/down) face other than the one it needs to go to
        target_face = constants.FACE_OF[constants.OTHER_SIDE_OF[target]] # side (non-top/bottom) of the cube the piece needs to be on
        if target_face != constants.FACE_OF[constants.OTHER_SIDE_OF[current_location]]: # if the piece isn't touching the correct face
            # move it to 'up' face
            lifting = cube.align_edge(current_location, 'u', 1)
            motions.append(lifting)
            current_location = cube.where_is(target)

            # rotate 'up' to move it into correct place
            motions.append(cube.align_edge(current_location, target_face))
            current_location = cube.where_is(target)

            # if the lifting could've messed with another bottom cross piece, fix it now that the target is out of the way
            # if len(lifting) = 0 then it was already on top, lift or its inverse would do nothing
            # if len(lifting) = 2 then it was on bottom, meaning there wasn't a proper bottom cross piece there to mess up
            if len(lifting) == 1:
                motions.append(lifting.swapcase())
                cube.rotate(lifting.swapcase())

        # drop the target into place
        motions.append(cube.align_edge(current_location, 'd', 1))
    return "".join(motions)

def _bottom_layer(cube: Cube):
    if not cube.match_pattern("....f..f.....r..r.....b..b.....l..l.....u.....d.ddd.d."):
        raise ValueError("Error: Solving stage \"bottom layer\": missing prerequisite")
    
    motions = []
    for target in [constants.DTL, constants.DTR, constants.DBR, constants.DBL]:
        current_location = cube.where_is(target)
        if target == current_location: # if the piece is already in location
            continue
        
        # raise the piece to the up layer without disturbing remainder of bottom layer
        if len(constants.ALL_SIDES_OF[current_location] & set(constants.UP[0])) == 0:
            piece = (constants.ALL_SIDES_OF[current_location] & set(constants.DOWN[0])).pop() # flatten to down-face corner
            face = constants.FACE_OF[constants.OTHER_SIDE_OF[piece][0]] # select face where the piece is the bottom-right
            motions.append(cube.move_algorithm("RUr", face)) # flick it up to the top-left of that face without disturbing rest of bottom layer
            current_location = cube.where_is(target) # piece moved so update current location
        
        # identify the corner piece 'above' the target, move the piece into that position
        piece = constants.OTHER_SIDE_OF[target][0]
        face = constants.FACE_OF[piece]
        piece = constants.CYCLE_OF[face][0][constants.CYCLE_OF[face][0].index(piece) - 1]
        motions.append(cube.align_corner(current_location, piece, 'u'))

        # if the piece is facing the up face, flick it around to face a side
        current_location = cube.where_is(target)
        if constants.FACE_OF[current_location] == 'u':
            motions.append(cube.move_algorithm("RurUU", face))
            current_location = cube.where_is(target)
        
        # flick the piece down into place
        if constants.FACE_OF[current_location] == face:
            motions.append(cube.move_algorithm("fuF", face))
        else:
            motions.append(cube.move_algorithm("RUr", face))
    return "".join(motions)

def _bottom_two_layers(cube: Cube):
    if not cube.match_pattern('....f.fff....r.rrr....b.bbb....l.lll....u....ddddddddd'):
        raise ValueError("Error: Solving stage \"bottom two layers\": missing prerequisite")
    
    motions = []
    targets = [constants.FMR, constants.RMR, constants.BMR, constants.LMR]
    for target in targets:
        current_location = cube.where_is(target)
        if target == current_location:
            continue

        # if the piece is in the middle layer (not in the top layer), push it out
        if len(constants.ALL_SIDES_OF[current_location] & set(constants.UP[1])) == 0:
            if current_location not in targets: # flip so it's the -MR piece
                current_location = constants.OTHER_SIDE_OF[current_location]
            motions.append(cube.move_algorithm("dLDufUFdUlDu", 'u', constants.FACE_OF[current_location]))
            current_location = cube.where_is(target)
        
        # line the piece up with the face it needs to fall into
        flag = False # whether the LHS or RHS insertion needs to be done
        if current_location in constants.UP[1]: # if it's on the up face, get the touching piece
            flag = True
            current_location = constants.OTHER_SIDE_OF[current_location]
        
        face = constants.FACE_OF[cube.where_does_piece_go(current_location)]
        motions.append(cube.align_edge(current_location, face, 1))

        if flag: # -ML piece, LHS insertion
            motions.append(cube.move_algorithm("fDrdUFufDuRdU", 'u', face))
        else:    # -MR piece, RHS insertion
            motions.append(cube.move_algorithm("FdLDufUFdUlDu", 'u', face))
    return "".join(motions)

def _top_cross(cube: Cube):
    if not cube.match_pattern('...ffffff...rrrrrr...bbbbbb...llllll....u....ddddddddd'):
        raise ValueError("Error: Solving stage \"top cross\": missing prerequisite")
    
    motions = []
    # flip pieces to make the top cross (colour-wise)
    while (pieces := [cube.cube_data[piece] != cube.colours['u'] for piece in constants.UP[1]]) != [False, False, False, False]:
        for index,here in enumerate(pieces):
            # check adjacent (empty center, L-shape)
            if here and pieces[index - 1]:
                motions.append(cube.move_algorithm("FURurf", constants.FACE_OF[constants.OTHER_SIDE_OF[constants.UP[1][index]]]))
                break

            # check opposites
            if here and pieces[index - 2]:
                motions.append(cube.move_algorithm("FRUruf", constants.FACE_OF[constants.OTHER_SIDE_OF[constants.UP[1][index]]]))
    
    # cycle pieces to make the top cross correct
    pieces = [constants.FTM, constants.RTM, constants.BTM, constants.LTM] # take the cycle of pieces FTM RTM BTM LTM
    pieces = [constants.FACE_OF[cube.where_does_piece_go(piece)] for piece in pieces] # decompose to the face they need to go on
    pieces = pieces[pieces.index('f'):] + pieces[:pieces.index('f')] # normalize list to start at should-be-front
    match "".join(pieces): # identify which state the pieces are in, and solve accordingly
        case "frbl": # solved
            moves = ""
        case "flbr": # l-r swap
            moves = "RUrURUUrFUfUFUUf"
        case "frlb": # l-b swap
            moves = "FUfUFUUf"
        case "fbrl": # r-b swap
            moves = "fuFufuuF"
        case "fblr": # CW rotation
            moves = "RUrURUUr"
        case "flrb": # CCW rotation
            moves = "luLuluuL"
        case _:
            raise ValueError("if this is ever reached then I am an idiot and unable to deduce all the possible states that the upper layer could be in at this stage")
    motions.append(cube.move_algorithm(moves, constants.FACE_OF[cube.where_is(constants.FTM)])) # enact moves
    motions.append(cube.align_edge(cube.where_is(constants.FTM), 'f', 1)) # align the top face
    return "".join(motions)

def _top_layer(cube: Cube):
    if not cube.match_pattern('.f.ffffff.r.rrrrrr.b.bbbbbb.l.llllll.u.uuu.u.ddddddddd'):
        raise ValueError("Error: Solving stage \"top layer\": missing prerequisite")
    
    motions = []
    # cycle the pieces around
    pieces = [cube.where_is(piece) for piece in constants.UP[0]] # same order as constants.UP[0] (face corners), location of
    pieces = [(constants.ALL_SIDES_OF[piece] & set(constants.UP[0])).pop() for piece in pieces] # flatten to the up face identifier
    pieces = [constants.UP[0].index(piece) for piece in pieces] # replace with IDs of position in constants.UP[0]
    # if there are no pieces in place (piece in place has index==entry): rotate CW as if anchored on FTR
    if all(index!=entry for index,entry in enumerate(pieces)):
        motions.append("lURuLUru")
        cube.rotate(motions[-1])

        # recalculate pieces
        pieces = [constants.UP[0].index((constants.ALL_SIDES_OF[cube.where_is(piece)] & set(constants.UP[0])).pop()) for piece in constants.UP[0]]
    
    # determine if rotation needs to be done
    if any(index!=entry for index,entry in enumerate(pieces)):
        # determine anchor piece
        anchor = constants.UP[0][next(piece for index,piece in enumerate(pieces) if index==piece)]

        # determine rotation direction
        loop = ((index,piece) for index,piece in enumerate(pieces) if index!=piece)
        first = next(loop)
        second = next(loop)
        
        # entry at index X is pointing at where the piece that should go there is
        if first[1] == second[0]: # first entry points to second index -> second index should move to first index, CCW
            motions.append(cube.move_algorithm("RulUruLU", constants.FACE_OF[constants.OTHER_SIDE_OF[anchor][0]]))
        elif second[1] == first[0]: # second entry points to first index -> first index should move to second index, CW
            motions.append(cube.move_algorithm("lURuLUru", constants.FACE_OF[constants.OTHER_SIDE_OF[anchor][1]]))
        else:
            raise ValueError("this should not be reachable but here's something to let me know I messed up")

    # rotate the pieces that aren't facing correctly
    pieces = [constants.UBR, constants.UTR, constants.UTL, constants.UBL] # the target pieces, CCW along top from FTR piece
    pieces = [([piece] + list(constants.OTHER_SIDE_OF[piece])) for piece in pieces] # turn each into a list of top - CW - CCW piece IDs
    pieces = [[cube.cube_data[piece] for piece in sub_list].index(cube.colours['u']) for sub_list in pieces] # convert to parity values (id of which side should be on top)
    last_rot = 0
    for rot_index,entry in enumerate(pieces):
        if entry == 0:
            continue # this piece doesn't need to be rotated

        motions.append(constants.ROTATION_TOKENS['u'][rot_index - last_rot])
        cube.rotate(motions[-1])
        last_rot = rot_index

        match entry:
            case 1:
                motions.append("rdRDrdRD")
                cube.rotate(motions[-1])
            case 2:
                motions.append("drDRdrDR")
                cube.rotate(motions[-1])
    motions.append(constants.ROTATION_TOKENS['u'][-last_rot % len(pieces)])
    cube.rotate(motions[-1])

    return "".join(motions)