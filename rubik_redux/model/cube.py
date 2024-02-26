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