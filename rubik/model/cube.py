from rubik.model.constants import *
import re
import math

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self.cube = list(encodedCube)
        
    def rotate(self, directions=None):
        
        if (directions == None or len(directions) == 0):
            return
        
        #Direction validation
        symbolValidation = re.compile(VALID_ROTATE_SYMBOLS)
        if (not re.fullmatch(symbolValidation, directions)):
            return 'invalid rotation'
        
        for index in range(len(directions)):
            self._turn(directions[index])
        
        return 'ok'
    
    def get(self):
        return ''.join(self.cube)
    
    def _turn(self, face):
        # Turning a single cube face results in each affected piece moving along one of five cycles
        # The constants used are those cycles, and the upper vs lowercase denotes which 'direction' they move
        # To move the pieces 'forwards', every piece from 2-4 in the cycle is swapped in succession with 1st
        #     Thus 1234 -> 2134 -> 3124 -> 4123
        # To move the pieces 'backwards', every piece from 2-4 is swapped with the previous
        #     Thus 1234 -> 2134 -> 2314 -> 2341
        
        if (len(face) > 1):
            return 'error: invalid input length'
        
        cycles = Cube.cycleOf(face)
        
        for cycle in cycles:
            for i in range(1, len(cycle)):
                if (face.isupper()):
                    buffer = cycle[0]
                    final = cycle[i]
                else:
                    buffer = cycle[i]
                    final = cycle[i - 1]
                
                self.cube[buffer],self.cube[final] = self.cube[final],self.cube[buffer]
    
    @staticmethod
    def makeCube(cubeString=None):
        
        #cubeString validation
        if (cubeString == None):
            return 'missing cube'
        
        if (len(cubeString) != PIECES_PER_FACE * FACES_PER_CUBE):
            return 'invalid cube length'
        
        symbolValidation = re.compile(VALID_CUBE_SYMBOLS)
        if (not re.fullmatch(symbolValidation, cubeString)):
            return 'invalid symbols used'
        
        counts = {}
        for face in CENTERS:
            counts[cubeString[face]] = 0;
        
        if (len(counts) != FACES_PER_CUBE):
            return 'invalid face centers'
        
        for index in range(PIECES_PER_FACE * FACES_PER_CUBE):
            if (cubeString[index] not in counts):
                return 'symbol matches no face'
            counts[cubeString[index]] = counts[cubeString[index]] + 1
        
        for colorCount in counts.values():
            if (colorCount == PIECES_PER_FACE):
                continue
            return 'invalid colour amounts'
        
        #cubeString passed the checks
        return Cube(cubeString)
    
    @staticmethod
    def faceOf(piece):
        match math.floor(piece / PIECES_PER_FACE):
            case 0:
                return 'f'
            case 1:
                return 'r'
            case 2:
                return 'b'
            case 3:
                return 'l'
            case 4:
                return 'u'
            case 5:
                return 'd'
    
    @staticmethod
    def facesTouching(piece):
        '''
        Does not return the face that a given piece currently occupies
        For corners, the order is most-CCW then most-CW faces from the face the piece occupies
        '''
        cycles = Cube.cycleOf(Cube.faceOf(piece))
        
        if (piece in cycles[1]):
            return Cube.faceOf(Cube.otherPieceOf(piece))
        
        if (piece in cycles[0]):
            return Cube.faceOf(Cube.otherPieceOf(piece,0)) + Cube.faceOf(Cube.otherPieceOf(piece,1))
        
        pass
    
    @staticmethod
    def alignPiece(piece, face, alt=0):
        '''
        USE FOR EDGES
        piece - the piece that one desires to move
        face - the face that one desires to have piece align with
        alt - achieve a specified functionality, default is 0, rotate a single face to move the piece between two faces
            alt = 0 - piece stays on the existing face
            alt = 1 - piece moves to the specified face
        '''
        if (alt == 1):
            return Cube.alignPiece(Cube.otherPieceOf(piece), face)
        
        cycle = Cube.cycleOf(Cube.faceOf(piece))
        
        cycle = cycle[1].copy()
        for index in range(len(cycle)):
            cycle[index] = Cube.facesTouching(cycle[index])
        offset = cycle.index(face) - cycle.index(Cube.facesTouching(piece))
        
        if (offset % len(cycle) == 0):
            return ''
        elif (offset % len(cycle) == 1):
            return Cube.faceOf(piece).upper()
        elif (offset % len(cycle) == 2):
            return 2 * Cube.faceOf(piece).upper()
        elif (offset % len(cycle) == 3):
            return Cube.faceOf(piece)
        return offset
    
    @staticmethod
    def cycleOf(face):
        match face.lower():
            case 'f':
                return FRONT
            case 'r':
                return RIGHT
            case 'b':
                return BACK
            case 'l':
                return LEFT
            case 'u':
                return UP
            case 'd':
                return DOWN
        return
    
    @staticmethod
    def otherPieceOf(piece, alt=None):
        '''
        Center pieces have 0 other pieces that move with them
            DO NOT USE THIS METHOD FOR CENTER PIECES
        Edge pieces have 1 other piece that moves with them
            DO NOT USE ALT FOR EDGE PIECES
        Corner pieces have 2 other pieces that move with them
            0 for the option most counterclockwise, 1 for the option most clockwise
        '''
        
        cycles = Cube.cycleOf(Cube.faceOf(piece))
        
        if (alt == None):
            position = cycles[1].index(piece)
            return cycles[3][position]
        
        if (alt == 0):
            position = cycles[0].index(piece)
            return cycles[4][(position - 1) % len(cycles[4])]
            
        if (alt == 1):
            position = cycles[0].index(piece)
            return cycles[2][position]
        
        pass
    
    def getColours(self):
        result = ''
        for piece in [FMM,RMM,BMM,LMM,UMM,DMM]:
            result += self.cube[piece]
        return result
    
    @staticmethod
    def centerOf(face):
        match face.lower():
            case 'f':
                return FMM
            case 'r':
                return RMM
            case 'b':
                return BMM
            case 'l':
                return LMM
            case 'u':
                return UMM
            case 'd':
                return DMM
        return
    
    def findFaceOf(self,colour):
        colours = self.getColours()
        
        if (colour not in colours):
            return None
        
        return FACES[colours.index(colour)]
    
    def findPieces(self,setsToSearch,colour,find=True):
        '''
        Sets to search - the subset of pieces on the cube to search for
        Colour - the colour to find
        Find - whether you are trying to find pieces that match the colour, or pieces that don't match the colour
            True - match the colour
            False - doesn't match the colour
        '''
        results = set()
        for piece in setsToSearch:
            if (find and colour == self.cube[piece]):
                results.add(piece)
            
            if (not find and colour != self.cube[piece]):
                results.add(piece)
        return results
    
    def status(self,state):
        '''
        raisedpetals, bottomcross, bottomlayer, middlelayer, topcross
        topsurface, topcorners, toplayer, solved, scrambled
        '''
        colours = self.getColours()
        
        pattern = r""
        match state:
            case 'raisedpetals':
                pattern += r".{36}" #side faces#
                pattern += r"." + re.escape(colours[5]) + r"." #top row
                pattern += re.escape(colours[5] + colours[4] + colours[5]) #middle row
                pattern += r"." + re.escape(colours[5]) + r"." #bottom row
                pattern += r".{9}" #bottom face
            case 'bottomcross':
                pattern += r".{7}" + re.escape(colours[0]) + r"." # front face
                pattern += r".{7}" + re.escape(colours[1]) + r"." # right face
                pattern += r".{7}" + re.escape(colours[2]) + r"." # back face
                pattern += r".{7}" + re.escape(colours[3]) + r"." # left face
                pattern += r".{9}" # top face
                pattern += r"." + re.escape(colours[5]) + r"." # bottom face, top row
                pattern += re.escape(colours[5]) + r"{3}" # bottom face, middle row
                pattern += r"." + re.escape(colours[5]) + r"." # bottom face, bottom row
            case 'bottomlayer':
                pattern += r".{6}" + re.escape(colours[0]) + r"{3}" # front face
                pattern += r".{6}" + re.escape(colours[1]) + r"{3}" # right face
                pattern += r".{6}" + re.escape(colours[2]) + r"{3}" # back face
                pattern += r".{6}" + re.escape(colours[3]) + r"{3}" # left face
                pattern += r".{9}" # top face
                pattern += re.escape(colours[5]) + r"{9}" # bottom face
                pass
            case 'middlelayer':
                pattern += r".{3}" + re.escape(colours[0]) + r"{6}" # front face
                pattern += r".{3}" + re.escape(colours[1]) + r"{6}" # right face
                pattern += r".{3}" + re.escape(colours[2]) + r"{6}" # back face
                pattern += r".{3}" + re.escape(colours[3]) + r"{6}" # left face
                pattern += r".{9}" # top face
                pattern += re.escape(colours[5]) + r"{9}" # bottom face
            case 'topcross':
                pattern += r".{3}" + re.escape(colours[0]) + r"{6}" # front face
                pattern += r".{3}" + re.escape(colours[1]) + r"{6}" # right face
                pattern += r".{3}" + re.escape(colours[2]) + r"{6}" # back face
                pattern += r".{3}" + re.escape(colours[3]) + r"{6}" # left face
                pattern += r"." + re.escape(colours[4]) + r"." # top face, top row
                pattern += re.escape(colours[4]) + r"{3}" #top face, middle row
                pattern += r"." + re.escape(colours[4]) + r"." #top face, bottom row
                pattern += re.escape(colours[5]) + r"{9}" # bottom face
            case 'topsurface':
                pattern += r".{3}" + re.escape(colours[0]) + r"{6}" # front face
                pattern += r".{3}" + re.escape(colours[1]) + r"{6}" # right face
                pattern += r".{3}" + re.escape(colours[2]) + r"{6}" # back face
                pattern += r".{3}" + re.escape(colours[3]) + r"{6}" # left face
                pattern += re.escape(colours[4]) + r"{9}" # top face
                pattern += re.escape(colours[5]) + r"{9}" # bottom face
            case 'topcorners':
                pattern += re.escape(colours[0]) + r"." + re.escape(colours[0]) + r"{7}" # front face
                pattern += re.escape(colours[1]) + r"." + re.escape(colours[1]) + r"{7}" # right face
                pattern += re.escape(colours[2]) + r"." + re.escape(colours[2]) + r"{7}" # back face
                pattern += re.escape(colours[3]) + r"." + re.escape(colours[3]) + r"{7}" # left face
                pattern += re.escape(colours[4]) + r"{9}" # top face
                pattern += re.escape(colours[5]) + r"{9}" # bottom face
            case 'toplayer' | 'solved':
                pattern += re.escape(colours[0]) + r"{9}"
                pattern += re.escape(colours[1]) + r"{9}"
                pattern += re.escape(colours[2]) + r"{9}"
                pattern += re.escape(colours[3]) + r"{9}"
                pattern += re.escape(colours[4]) + r"{9}"
                pattern += re.escape(colours[5]) + r"{9}"
            case 'scrambled':
                return not (self.status('raisedpetals') or self.status('bottomcross'))
                pass
        
        pattern = re.compile(pattern)
        return re.fullmatch(pattern, self.get())
    
    def whereDoesXGo(self, piece):
        cycle = Cube.cycleOf( self.findFaceOf( self.cube[piece] ) ) #The cycles of the face that the piece goes on
        variant = None
        
        if (piece in EDGES):
            cycle = cycle[1].copy()
        
        if (piece in CORNERS):
            cycle = cycle[0].copy()
            variant = 0
            
        pieceColour = self.cube[Cube.otherPieceOf(piece, variant)]
        for slot in cycle:
            slotFace = Cube.faceOf(Cube.otherPieceOf(slot, variant))
            slotColour = self.cube[Cube.centerOf(slotFace)]
            if (slotColour == pieceColour):
                return slot
        pass
    
    @staticmethod
    def alignCorner(piece, destination, faceToRotate):
        '''
        destination is a 3-character string
        '''
        #Input purification
        puredest = ''
        if ('u' in destination):
            puredest += 'u'
        if ('d' in destination):
            puredest += 'd'
        if ('f' in destination):
            puredest += 'f'
        if ('r' in destination):
            puredest += 'r'
        if ('b' in destination):
            puredest += 'b'
        if ('l' in destination):
            puredest += 'l'
        
        #Turn destination into a set of pieces
        destinations = {'ufr':{FTR,RTL,UBR},
                        'urb':{RTR,BTL,UTR},
                        'ubl':{BTR,LTL,UTL},
                        'ufl':{LTR,FTL,UBL},
                        'dfr':{FBR,RBL,DTR},
                        'drb':{RBR,BBL,DBR},
                        'dbl':{BBR,LBL,DBL},
                        'dfl':{LBR,FBL,DTL}}
        
        #Update destination to the set of possible pieces
        if (puredest not in destinations.keys()):
            return
        else:
            destination = destinations[puredest]
        
        #Turn the piece and destination into a numeric offset
        offset = -8
        for cycle in Cube.cycleOf(faceToRotate):
            if (piece not in cycle):
                continue
            destination.intersection_update(cycle)
            offset = cycle.index(list(destination)[0]) - cycle.index(piece)
            offset = offset % len(cycle)
            break
            
        if (offset == -8):
            return "Invalid" #If the piece cannot be moved by rotating the face
        
        if (offset == 0):
            return ''
        elif (offset == 1):
            return faceToRotate.upper()
        elif (offset == 2):
            return 2 * faceToRotate.upper()
        elif (offset == 3):
            return faceToRotate.lower()
        return offset
    
    @staticmethod
    def moveAlgorithm(algorithm, newFace):
        '''
        Write the algorithm as if it is being performed on the front face
        newFace will shift the algorithm as if it is being performed on the other face
        Up and down faces are not shifted
        '''
        algorithm = list(algorithm)
        for index in range(len(algorithm)):
            if (algorithm[index].lower() == 'u'):
                continue
            
            offset = FACES.index( newFace.lower() )
            offset += FACES.index( algorithm[index].lower() )
            offset %= len(FACES) - 2
            
            if (algorithm[index].isupper()):
                algorithm[index] = FACES[offset].upper()
            else:
                algorithm[index] = FACES[offset]
        
        return ''.join(algorithm)
    
    @staticmethod
    def whereWillXBe(algorithm, piece):
        algorithm = list(algorithm)
        
        #For each turn
        for index in range(len(algorithm)):
            #Find the specific subcycle it is a part of
            subcycle = []
            for cycle in Cube.cycleOf(algorithm[index].lower()):
                if (piece not in cycle):
                    continue
                subcycle = cycle.copy()
                break
            
            #If piece isn't moved by this cycle, skip shifting
            if (piece not in subcycle):
                continue
            
            #Shift the piece based on direction
            offset = subcycle.index(piece)
            if (algorithm[index].isupper()):
                offset += 1
            else:
                offset -= 1
            offset %= len(subcycle)
            piece = subcycle[offset]
        
        return piece