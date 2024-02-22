import rubik.model.constants
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''  
    if (theCube.status('bottomlayer') or not theCube.status('bottomcross')):
        return '' # If the bottom layer is already solved, or the bottom cross is not solved, do nothing
    
    rotations = ''
    pieces = _findPiecesToMove(theCube)
    while (pieces != None):
        piece = pieces[0]
        slot = pieces[1]
        
        #If piece is in bottom layer, move it up
        newRotations = _movePieceToUp(piece)
        
        #Move piece above slot
        newRotations += Cube.alignCorner(Cube.whereWillXBe(newRotations, piece),
                                         'u' + Cube.facesTouching(slot), 'u')
        
        #Move piece into slot
        newRotations += _dropPieceIntoSlot(Cube.whereWillXBe(newRotations, piece))
        
        theCube.rotate(newRotations)
        rotations += newRotations
        pieces = _findPiecesToMove(theCube)
    
    return rotations

def _findPiecesToMove(theCube: Cube):
    colours = theCube.getColours()
    
    for piece in theCube.findPieces(rubik.model.constants.CORNERS, colours[5]):
        slot = theCube.whereDoesXGo(piece)
        if (piece == slot):
            continue # If it's already where it is supposed to go
        
        return [piece,slot]

def _movePieceToUp(piece):
    flag = None
    if ('d' == Cube.faceOf(piece)):
        flag = Cube.faceOf(Cube.otherPieceOf(piece, 1))
    elif ('d' == Cube.faceOf(Cube.otherPieceOf(piece, 0))):
        flag = Cube.faceOf(piece)
    elif ('d' == Cube.faceOf(Cube.otherPieceOf(piece, 1))):
        flag = Cube.faceOf(Cube.otherPieceOf(piece, 0))
    
    newRotations = ''
    if (flag != None):
        newRotations = Cube.moveAlgorithm('Fuf', flag)
    return newRotations

def _dropPieceIntoSlot(piece):
    newRotations = ''
    
    #If the piece is on top, move it to a side
    if ('u' == Cube.faceOf(piece)):
        newRotations = Cube.moveAlgorithm('lULUU', Cube.faceOf(Cube.otherPieceOf(piece, 0)))
        piece = Cube.whereWillXBe(newRotations, piece)
    
    if ('u' == Cube.faceOf(Cube.otherPieceOf(piece, 0))): #On the left
        newRotations += Cube.moveAlgorithm('luL', Cube.faceOf(Cube.otherPieceOf(piece, 1)))
    else: #On the right
        newRotations += Cube.moveAlgorithm('FUf', Cube.faceOf(piece))
    
    return newRotations
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    