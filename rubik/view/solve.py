from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
import hashlib
import random

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
     
    encodedCube = parms.get('cube')
    theCube = Cube.makeCube(encodedCube)
    if (isinstance(theCube, str)):
        result['status'] = 'error: ' + theCube
        return result
    
    if (len(parms.keys()) > 1):
        result['status'] = 'error: no extraneous keys allowed'
        return result
    
    rotations = ""
    rotations += solveBottomCross(theCube)      #iteration 2
    rotations += solveBottomLayer(theCube)      #iteration 3
    rotations += solveMiddleLayer(theCube)      #iteration 4
    rotations += solveUpCross(theCube)          #iteration 5
    rotations += solveUpSurface(theCube)        #iteration 5
    rotations += solveUpperLayer(theCube)       #iteration 6
    
    result['solution'] = rotations
    result['status'] = 'ok'    
    result['integrity'] = _generateSignature(encodedCube, rotations)  #iteration 3
                     
    return result

def _generateSignature(encodedCube, solution):
    itemToTokenize = encodedCube + solution + "arg0070"
    sha256Hash = hashlib.sha256()
    sha256Hash.update(itemToTokenize.encode())
    fullToken = sha256Hash.hexdigest()
    
    selection = random.randrange(0, len(fullToken) - 8 + 1)
    return fullToken[selection : selection + 8]