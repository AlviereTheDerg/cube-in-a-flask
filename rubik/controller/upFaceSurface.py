from rubik.model.constants import CORNERS, UP, UMM
from rubik.model.cube import Cube

def solveUpSurface(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the up face is solved.
        
        input:  an instance of the cube class with up-face cross solved
        output: the rotations required to solve the up surface  
    '''
    
    if (theCube.status('topsurface') or not theCube.status('topcross')):
        return ''
    
    topcolour = theCube.get()[UMM]
    pieces = theCube.findPieces(CORNERS, topcolour)
    result = ''
    
    #<3 not <4 in case of a bad cube
    while (len(pieces.intersection(UP[0])) < 3):
        newbit = ''
        
        #Fish formed, somewhere
        if (len(pieces.intersection(UP[0])) == 1):
            newbit = _getSolveFromFish(theCube, pieces.intersection(UP[0]).pop())
        
        #No fish, so try and fix it
        else:
            newbit = Cube.moveAlgorithm('RUrURUUr', Cube.faceOf(pieces.intersection(UP[4]).pop()))
        
        theCube.rotate(newbit)
        pieces = theCube.findPieces(CORNERS, topcolour)
        result += newbit
    
    #If 3 corners are solved, but the 4th isn't
    if (len(pieces.intersection(UP[0])) == 3):
        return "SOMETHING HAS GONE WRONG"
    
    return result

def _getSolveFromFish(theCube: Cube, fish):
    #Grab a top piece other than the fish
    piece = (set(UP[0]) - {fish}).pop()
    cubestring = theCube.get()
    
    #The other 3 pieces need to be rotated CCW
    if (cubestring[UMM] == cubestring[Cube.otherPieceOf(piece, 0)]):
        return Cube.moveAlgorithm('luLuluuL', Cube.faceOf(Cube.otherPieceOf(fish, 1)))
    
    #CW
    else:
        return Cube.moveAlgorithm('RUrURUUr', Cube.faceOf(Cube.otherPieceOf(fish, 0)))
    











