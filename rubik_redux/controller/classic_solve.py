
import rubik_redux.model.constants as constants
from rubik_redux.model.cube import Cube

def solve(cube: Cube):
    pass

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
    pass