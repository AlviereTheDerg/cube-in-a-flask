"""
Created on Feb 24 2024

@author: Alviere
"""
import unittest
from rubik_redux.model.cube import Cube

class CubeTest(unittest.TestCase):
    # Initializer tests
    def test_invalid_input_type_int(self):
        with self.assertRaises(TypeError) as result:
            Cube(3241)
        self.assertEqual(f"Error: Input type: Expected string but recieved {type(1)}", str(result.exception))

    def test_invalid_input_type_none(self):
        with self.assertRaises(TypeError) as result:
            Cube(None)
        self.assertEqual(f"Error: Input type: Expected string but recieved {type(None)}", str(result.exception))

    def test_invalid_character_count_low(self):
        with self.assertRaises(ValueError) as result:
            Cube("aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffff")
        self.assertEqual('Error: Cube string length: Expected 54 characters but recieved 53', str(result.exception))

    def test_invalid_character_count_high(self):
        with self.assertRaises(ValueError) as result:
            Cube("aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffff")
        self.assertEqual('Error: Cube string length: Expected 54 characters but recieved 55', str(result.exception))

    def test_invalid_characters_present(self):
        with self.assertRaises(ValueError) as result:
            Cube("=========---------!!!!!!!!!;;;;;;;;;/////////?????????")
        self.assertEqual('Error: Cube string contents: Please only use alphanumeric characters a-z, A-Z, 0-9', str(result.exception))

    def test_invalid_unique_centerpoints(self):
        with self.assertRaises(ValueError) as result:
            Cube("aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeefeeeffffeffff")
        self.assertEqual('Error: Cube string contents: Centerpoints contain duplicates', str(result.exception))

    def test_invalid_piece_match_centers(self):
        with self.assertRaises(ValueError) as result:
            Cube("aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffg")
        self.assertEqual('Error: Cube string contents: Non-center pieces need to match present centerpieces', str(result.exception))

    def test_invalid_piece_counts(self):
        with self.assertRaises(ValueError) as result:
            Cube("aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeeffffffffa")
        self.assertEqual('Error: Cube string contents: Require 9 pieces of each symbol', str(result.exception))

    def test_valid_cube_creation(self):
        cube_string = "bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy"
        cube = Cube(cube_string)
        self.assertTrue(isinstance(cube, Cube))
        self.assertEqual(cube_string, "".join(cube.cube_data))

if __name__ == '__main__':
    unittest.main()