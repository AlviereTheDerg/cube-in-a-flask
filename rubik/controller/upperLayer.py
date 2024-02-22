from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
    '''  
    
    result = _solveCorners(theCube)
    result += _solveEdges(theCube)
    return result

def _solveCorners(theCube):
    if (theCube.status('topcorners') or not theCube.status('topsurface')):
        return ''
    
    result = ''
    while (swapface := _findCornersToSwap(theCube.get())):
        newbit = Cube.moveAlgorithm('FUfufLFFufuFUfl', swapface)
        result += newbit
        theCube.rotate(newbit)
    
    rotateface = theCube.findFaceOf(theCube.get()[FTL])
    newbit = Cube.alignPiece(UBM, rotateface)
    if (newbit != ''):
        result += newbit
        theCube.rotate(newbit)
    return result

def _findCornersToSwap(cubestring):
    #If all the corners are solved, just not rotated right
    for index in range(len(UP[0])):
        if (cubestring[UP[2][index]] != cubestring[UP[4][index]]):
            break
        if (index == (len(UP[0]) - 1)):
            return
    
    #Prioritize corners that are already matching
    for index in range(len(UP[0])):
        if (cubestring[UP[2][index]] == cubestring[UP[4][index]]):
            return ['f','l','b','r'][index]
        
    #If no matching corners on their same face, then find faces on opposite pairs
    for index in range(len(UP[0])):
        if (cubestring[UP[2][index]] == cubestring[UP[4][(index + 2) % len(UP[0])]]):
            return FACES[(index - 1) % len(UP[0])]

def _solveEdges(theCube):
    if (theCube.status('toplayer') or not theCube.status('topcorners')):
        return ''
    
    result = ''
    offsets = [0] * 3
    while (solvedface := _findSolvedEdge(theCube)):
        offsets[0] = ['b','r','f','l'].index(solvedface)
        offsets[1] = (offsets[0] + 1) % len(UP[1])
        offsets[2] = (offsets[0] + 2) % len(UP[1])
        newbit = ''
        
        #See if it needs to be rotated clockwise
        if (theCube.whereDoesXGo(UP[1][offsets[1]]) == UP[1][offsets[2]]):
            newbit = Cube.moveAlgorithm('BBUlRBBLrUBB', solvedface)
        else:
            newbit = Cube.moveAlgorithm('BBulRBBLruBB', solvedface)
        
        result += newbit
        theCube.rotate(newbit)
    
    return result

def _findSolvedEdge(theCube):
    if (theCube.status('solved')):
        return
    for piece in UP[1]:
        if (piece == theCube.whereDoesXGo(piece)):
            return Cube.facesTouching(piece)
    return 'f'