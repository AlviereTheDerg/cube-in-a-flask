
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