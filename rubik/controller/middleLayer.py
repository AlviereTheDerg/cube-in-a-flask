from rubik.model.constants import FTM, FML, RTM, RML, BTM, BML, LTM, LML, UMM, UP, PIECES_PER_FACE
from rubik.model.cube import Cube

def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    '''
    result = ''
    
    if (theCube.status('middlelayer') or not theCube.status('bottomlayer')):
        return result
    
    pieces = _findMiddleEdges(theCube)
    cubestring = theCube.get()
    
    for piece in pieces:
        # If it's in the middle, move it up
        shiftpiece = Cube.whereWillXBe(result, piece)
        if (shiftpiece not in (UP[1] + UP[3])):
            # Do a left-trigger type to move it up, so find which face it's on
            if (shiftpiece % PIECES_PER_FACE == FML): # If left
                face = Cube.faceOf(shiftpiece)
            else:
                face = Cube.faceOf(Cube.otherPieceOf(shiftpiece))
            result += Cube.moveAlgorithm('luLUFUf', face)
        
        # Fix if the piece is on top rather than side
        shiftpiece = Cube.whereWillXBe(result, piece)
        if (shiftpiece in UP[1]):
            piece = Cube.otherPieceOf(piece)
            shiftpiece = Cube.otherPieceOf(shiftpiece)
        
        # Move the piece to the right face
        faceToPut = theCube.findFaceOf(cubestring[piece])
        result += Cube.alignPiece(shiftpiece, faceToPut, 1)
        
        # Find which side it goes into, do appropriate move
        if (theCube.whereDoesXGo(piece) % PIECES_PER_FACE == FML): # Left
            dropAlgo = 'uluLUFUf'
        else:
            dropAlgo = 'URUrufuF'
        result += Cube.moveAlgorithm(dropAlgo, faceToPut)
    
    theCube.rotate(result)
    return result

def _findMiddleEdges(theCube: Cube):
    cubestring = theCube.get()
    
    # Don't search every edge, just search enough
    searchset = {FTM, FML, RTM, RML, BTM, BML, LTM, LML}
    founds = set()
    for piece in searchset:
        # If this piece goes in the top face, skip it
        if (cubestring[piece] == cubestring[UMM]):
            continue
        if (cubestring[Cube.otherPieceOf(piece)] == cubestring[UMM]):
            continue
        
        # If this piece is already in place, skip it
        if (piece == theCube.whereDoesXGo(piece)):
            continue
        
        founds.add(piece)
    
    return founds






