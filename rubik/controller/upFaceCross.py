from rubik.model.constants import UMM,UBM,UTM,UMR,UML
from rubik.model.cube import Cube

def solveUpCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the up-face cross configuration.
        
        input:  an instance of the cube class with the middle layer solved
        output: the rotations required to solve the up-face cross  
    '''
    
    if (theCube.status('topcross')):
        return '' # If the top cross is already solved, or the middle layer is not solved, do nothing
    if (not theCube.status('middlelayer')):
        return ''
    
    cubestring = theCube.get()
    
    #If none of the pieces are correct, parity means only need to check 3
    if (cubestring[UMM] not in {cubestring[UBM], cubestring[UMR], cubestring[UTM]}):
        result = Cube.moveAlgorithm('FRUrufBULulb', Cube.faceOf(Cube.otherPieceOf(UBM)))
        theCube.rotate(result)
        return result
    
    #Check for the various 2-solved cases
    result = ''
    pieces = [UBM, UMR, UTM, UML]
    for index in range(len(pieces)):
        
        #If this piece is correct, skip it, other checks can safely assume current piece isn't correct
        if (cubestring[UMM] == cubestring[pieces[index]]):
            continue
        
        #If the opposite is the only other one incorrect
        if (cubestring[UMM] != cubestring[pieces[(index + 2) % len(pieces)]]):
            result = Cube.moveAlgorithm('FRUruf', Cube.faceOf(Cube.otherPieceOf(pieces[index])))
            break
        
        #If the piece counterclockwise is incorrect, correct it and this one
        elif (cubestring[pieces[(index + 1) % len(pieces)]] != cubestring[UMM]):
            result = Cube.moveAlgorithm('FURurf', Cube.faceOf(Cube.otherPieceOf(pieces[index])))
            break
        
        #If the piece clockwise is incorrect, only happens if left and front are the incorrect ones
        else:
            result = Cube.moveAlgorithm('FURurf', 'l')
            break
        
        pass
    
    theCube.rotate(result)
    return result