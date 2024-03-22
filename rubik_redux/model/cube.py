"""
Created on Feb 24 2024

@author: Alviere
"""
import rubik_redux.model.constants as constants
import re

class Cube:
    '''
    Rubik's Cube representation object
    '''
    def __init__(self, cube_string: str):
        if not isinstance(cube_string, str):
            raise TypeError(f"Error: Input type: Expected string but recieved {type(cube_string)}")
        
        if len(cube_string) != constants.PIECES_PER_FACE * constants.FACES_PER_CUBE:
            raise ValueError(f"Error: Cube string length: Expected {constants.PIECES_PER_FACE * constants.FACES_PER_CUBE} characters but recieved {len(cube_string)}")

        if not re.fullmatch(re.compile(constants.VALID_CUBE_SYMBOLS), cube_string):
            raise ValueError("Error: Cube string contents: Please only use alphanumeric characters a-z, A-Z, 0-9")

        piece_mapping = {cube_string[index]:0 for index in constants.CENTERS}
        if len(piece_mapping) != len(constants.CENTERS):
            raise ValueError("Error: Cube string contents: Centerpoints contain duplicates")
        
        try:
            for char in cube_string:
                piece_mapping[char] += 1
        except KeyError:
            raise ValueError("Error: Cube string contents: Non-center pieces need to match present centerpieces")

        if any((count != constants.PIECES_PER_FACE for count in piece_mapping.values())):
            raise ValueError(f"Error: Cube string contents: Require {constants.PIECES_PER_FACE} pieces of each symbol")

        self.cube_data = [char for char in cube_string]
        self.colours = {face:self.cube_data[constants.CENTER_OF[face]] for face in constants.FACES}

        # Impossible pieces
        pieces = {frozenset(constants.ALL_SIDES_OF[piece]) for piece in (constants.CENTERS | set(constants.UP[0] + constants.UP[1] + constants.DOWN[0] + constants.DOWN[1] + [constants.FML, constants.FMR, constants.BML, constants.BMR]))}
        if ({frozenset(   self.colours[constants.FACE_OF[slot]] for slot in piece) for piece in pieces}   # Expected colours of the piece
            != {frozenset(self.cube_data[slot]                  for slot in piece) for piece in pieces}): # Actual colours of the piece
            raise ValueError('Error: Cube unsolvable: Impossible pieces')

        # Edge parity
        if sum(1 for piece in (constants.UP[1] + constants.DOWN[1] + [constants.FML, constants.FMR, constants.BML, constants.BMR]) if 
                (self.cube_data[piece] in {self.colours[face] for face in {'u','d'}}) or 
                ((self.cube_data[piece] in {self.colours[face] for face in {'l','r'}}) and 
                    (self.cube_data[constants.OTHER_SIDE_OF[piece]] not in {self.colours[face] for face in {'u','d'}}))
               ) % 2 != 0:
            raise ValueError('Error: Cube unsolvable: Edge parity')
        
        # Corner parity
        if (sum(0 for piece in (constants.UP[0] + constants.DOWN[0]) if self.cube_data[piece] in {self.colours[face] for face in {'u','d'}}) 
            + sum(1 for piece in (constants.UP[4] + constants.DOWN[4]) if self.cube_data[piece] in {self.colours[face] for face in {'u','d'}})
            + sum(2 for piece in (constants.UP[2] + constants.DOWN[2]) if self.cube_data[piece] in {self.colours[face] for face in {'u','d'}})) % 3 != 0:
            raise ValueError("Error: Cube unsolvable: Corner parity")
        
        # Permutation parity
        visited = set()
        swaps = 0
        while visited != pieces:
            cycle = [list(pieces - visited)[0]]
            next_position = self.where_does_piece_go(list(cycle[0])[0])
            while cycle[0] != constants.ALL_SIDES_OF[next_position]:
                cycle.append(frozenset(constants.ALL_SIDES_OF[next_position]))
                next_position = self.where_does_piece_go(next_position)
            visited.update(cycle)
            swaps += len(cycle) - 1
        if swaps % 2 != 0:
            raise ValueError("Error: Cube unsolvable: Permutation parity")


    def find_face_from_colour(self, piece):
        return {c:f for f,c in self.colours.items()}[piece]

    def where_does_piece_go(self, piece):
        if piece in constants.CENTERS:
            return piece
        cycle_subset = 1 if piece in constants.EDGES else 0
        here_colours = {self.cube_data[pos] for pos in constants.ALL_SIDES_OF[piece]}
        for slot in constants.CYCLE_OF[self.find_face_from_colour(self.cube_data[piece])][cycle_subset]:
            there_colours = {self.colours[constants.FACE_OF[pos]] for pos in constants.ALL_SIDES_OF[slot]}
            if here_colours == there_colours:
                return slot
    
    def rotation_validation(func):
        def rotation_validator(self, rotations, *args, **kwargs):
            if len(set(rotations) - constants.VALID_ROTATE_SYMBOLS) != 0:
                raise ValueError(f"Error: Invalid Cube turn: Expected char in \"FfRrBbLlUuDd\", recieved \"{rotations}\"")
            return func(self, rotations, *args, **kwargs)
        return rotation_validator
    
    @rotation_validation
    def rotate(self, rotations):
        """
        Performs a series of face rotations of the cube
        Accepts a string of face identifiers, character case determines rotation direction
        Uppercase -> CW rotation
        Lowercase -> CCW rotation
        """
        destinations = range(len(self.cube_data))
        for rotation in rotations:
            destinations = [constants.ROTATION_TRANSFERS.get(rotation).get(piece, piece) for piece in destinations]
        destinations = {piece:index for index,piece in enumerate(destinations)}

        self.cube_data = [self.cube_data[destinations.get(piece, piece)] for piece in range(len(self.cube_data))]

    def __repr__(self):
        return "".join(self.cube_data)
    
    def where_is(self, search_piece):
        if search_piece not in range(len(self.cube_data)):
            raise ValueError("Error: Attempting to locate an out of bounds piece")
        
        search_zone = (
            constants.CENTERS.copy() if search_piece in constants.CENTERS else 
            constants.EDGES.copy() if search_piece in constants.EDGES else
            constants.CORNERS.copy())
        search_zone &= {piece for piece in search_zone if self.cube_data[piece] == self.colours[constants.FACE_OF[search_piece]]}
        
        expected_piece = {self.colours[constants.FACE_OF[piece]] for piece in constants.ALL_SIDES_OF[search_piece]}
        
        for search_piece in search_zone:
            if {self.cube_data[piece] for piece in constants.ALL_SIDES_OF[search_piece]} == expected_piece:
                return search_piece
            
    def match_pattern(self, pattern):
        if not isinstance(pattern, str):
            raise ValueError(f"Error: Input type: Expected string but recieved {type(pattern)}")
        if len(pattern) != len(self.cube_data):
            raise ValueError(f"Error: Invalid pattern length: Expected {len(self.cube_data)} characters but recieved {len(pattern)}")
        if len(set(pattern) - set(constants.FACES) - set('.')) != 0:
            raise ValueError("Error: Invalid pattern contents: Only use face characters \"frblud\" and wildcard \".\"")
        
        for index,char in enumerate(pattern):
            if char != '.' and self.cube_data[index] != self.colours[char]:
                return False
        else:
            return True
        
    def align_edge(self, piece, face, variant=0):
        if (variant == 1):
            return self.align_edge(constants.OTHER_SIDE_OF[piece], face)
        
        cycle = [constants.FACE_OF[constants.OTHER_SIDE_OF[slot]] for slot in constants.CYCLE_OF_FACE_OF[piece][1]]
        offset = cycle.index(face) - cycle.index(constants.FACE_OF[constants.OTHER_SIDE_OF[piece]])
        
        match offset % len(cycle):
            case 0:
                result = ""
            case 1:
                result = constants.FACE_OF[piece].upper()
            case 2:
                result = 2 * constants.FACE_OF[piece].upper()
            case 3:
                result = constants.FACE_OF[piece]
        self.rotate(result)
        return result
    
    @rotation_validation
    def move_algorithm(self, algorithm, new_front, new_up='u'):
        if {new_front,new_up} in ({'f','b'},{'u','d'},{'l','r'}) or len({new_front,new_up}) == 1:
            raise ValueError("Error: Invalid faces specified: Cannot assign front and up to non-adjacent faces")
        
        static_middle = 'frbl'
        match new_up:
            case 'u':
                transform = {'u':'u', 'd':'d'}
                middle = 'frbl'
            case 'd':
                transform = {'u':'d', 'd':'u'}
                middle = 'lbrf'
            case 'f':
                transform = {'u':'f', 'd':'b'}
                middle = 'uldr'
            case 'b':
                transform = {'u':'b', 'd':'f'}
                middle = 'rdlu'
            case 'l':
                transform = {'u':'l', 'd':'r'}
                middle = 'fubd'
            case 'r':
                transform = {'u':'r', 'd':'l'}
                middle = 'dbuf'

        begin = middle.index(new_front)
        for index in range(len(middle)):
            transform[static_middle[index]] = middle[(index+begin)%len(middle)]
        
        transform |= {key.upper():value.upper() for key,value in transform.items()}

        algorithm = "".join(transform[step] for step in algorithm)
        self.rotate(algorithm)
        return algorithm