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