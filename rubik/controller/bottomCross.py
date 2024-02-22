from rubik.model.constants import EDGES,FRONT,RIGHT,BACK,LEFT,UP,DOWN,FTM,FMR,FBM,FML
from rubik.model.cube import Cube
import re

def solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    '''
    
    colours = theCube.getColours()
    
    #If the bottom cross is already solved, don't do anything
    if (theCube.status('bottomcross')):
        return ''
    
    rotations = _raiseBottomFaces(theCube, colours)
    rotations += _dropBottomFaces(theCube, colours)
    return rotations

def _raiseBottomFaces(theCube: Cube, colours) -> str:
    
    rotations = ''
    while (not theCube.status('raisedpetals')):
        foundPair = _findPetalAndSlot(theCube, colours)
        newRotations = _raisePetal(foundPair[0], foundPair[1])
        
        theCube.rotate(newRotations)
        rotations += newRotations
    
    return rotations

def _dropBottomFaces(theCube: Cube, colours) -> str:
    rotations = ''
    while (not theCube.status('bottomcross')):
        pair = _findPetalToDrop(theCube, colours)
        newRotations = Cube.alignPiece(pair[0], pair[1])
        newRotations += 2 * pair[1].upper()
        
        rotations+= newRotations
        theCube.rotate(newRotations)
    return rotations

def _raisePetal(piece, slot) -> str:
    if (piece in UP[3]): #If the petal is in the top face, but 'flipped'
        newRotations = Cube.faceOf(piece) + 'U' + Cube.facesTouching(piece + (FML - FTM))
            #CCW front, CW top, CCW face to the left
        return newRotations
    
    if (piece in DOWN[3]): #If petal is in the bottom face, but 'flipped'
        newRotations = Cube.alignPiece(slot, Cube.faceOf(piece))
        newRotations += Cube.faceOf(piece) + 'u' + Cube.facesTouching(piece + (FMR - FBM)).upper()
            #CCW front, CCW top, CW face to the right
        return newRotations
    
    newRotations = Cube.alignPiece(slot, Cube.facesTouching(piece))
    newRotations += Cube.alignPiece(piece,'u',1)
    return newRotations

def _findPetalAndSlot(theCube: Cube, colours) -> [int,int]:
    '''
    Returns [piece, slot]
    '''
    slots = theCube.findPieces(set(UP[1]), colours[5], False)
        #Find edge pieces on the top face that don't match bottom colour
    
    petals = theCube.findPieces(EDGES - set(UP[1]), colours[5])
        #Find edge pieces not on the top face that match bottom colour
    
    #Optimization
    for slot in slots:
        #If the petal is already in place, just 'flipped'
        if (Cube.otherPieceOf(slot) in petals):
            return [Cube.otherPieceOf(slot), slot]
        
        #If a petal is on the same side as the slot
        face = Cube.facesTouching(slot)
        face = Cube.cycleOf(face)[3]
        face = set(face).intersection(petals)
        if (len(face) == 0):
            continue
        
        face = list(face)
        return [face[0], slot]
    
    slots = list(slots)
    for cycle in [FRONT[3],RIGHT[3],BACK[3],LEFT[3],DOWN[3]]:
        if (len(petals.intersection(set(cycle))) == 0):
            continue
        petals.intersection_update(set(cycle))
        petals = list(petals)
        return [petals[0], slots[0]]
    
    return

def _findPetalToDrop(theCube: Cube, colours) -> [int,str]:
    '''
    Returns [piece, face]
    '''
    
    cubeString = theCube.get()
    petals = theCube.findPieces(set(UP[1]), colours[5])
    
    #Optimization
    for petal in petals:
        if (cubeString[petal] != cubeString[ Cube.centerOf(Cube.faceOf(petal)) ]):
            #If this petal does not match the face it is currently on
            continue
        
        return [petal, Cube.faceOf(Cube.otherPieceOf(petal))]
    
    #find the face of the first petal available
    petals = list(petals)
    return [petals[0], theCube.findFaceOf( cubeString[ Cube.otherPieceOf(petals[0]) ] )]