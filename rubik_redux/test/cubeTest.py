"""
Created on Feb 24 2024

@author: Alviere
"""
import unittest
from rubik_redux.model.cube import Cube
import rubik_redux.model.constants as constants
from rubik_redux.model.constants import *

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

    def valid_cube_test(self, cube_string):
        cube = Cube(cube_string)
        self.assertTrue(isinstance(cube, Cube))
        self.assertEqual(cube_string, "".join(cube.cube_data))
        self.assertEqual({'f':cube_string[constants.FMM], 'r':cube_string[constants.RMM], 
                          'b':cube_string[constants.BMM], 'l':cube_string[constants.LMM], 
                          'u':cube_string[constants.UMM], 'd':cube_string[constants.DMM]}, 
                          cube.colours)

    # TODO: add more valid cube creation tests
    def test_valid_cube_creation_1(self):
        self.valid_cube_test("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_valid_cube_creation_2(self):
        self.valid_cube_test("wyrybrbwggoyyooyywbowgggrwbbbgrrorryowrrwbobyogowygwbg")
    def test_valid_cube_creation_3(self):
        self.valid_cube_test("owoybbbgrgboyoygbowoyrgygowrgyorgbwrggbwwwbrwyrwoyrrby")
    def test_valid_cube_creation_4(self):
        self.valid_cube_test("ogroboogrwbbwowbbyowwrgrgrorbwyryggbbbwowrgwgyoyyyyygr")

    
    # Tests for unsolvable cubes
    def unsolvable_impossible_piece_test(self, cube_string):
        with self.assertRaises(ValueError) as result:
            Cube(cube_string)
        self.assertEqual('Error: Cube unsolvable: Impossible pieces', str(result.exception))
    
    def test_unsolvable_impossible_piece_1(self): # edges with same colour on both sides
        self.unsolvable_impossible_piece_test("bwbbbbbbbooooooooogggggggggrrrrrbrrrwwwrwwwwwyyyyyyyyy")
    def test_unsolvable_impossible_piece_2(self): # edges with colours of opposite cube sides
        self.unsolvable_impossible_piece_test("bbbobbbbbooogooooogggrgggggrrrbrrrrrwwwwwwwwwyyyyyyyyy")
    def test_unsolvable_impossible_piece_3(self): # corner with improper colour amounts
        self.unsolvable_impossible_piece_test("bbwbbbrbbooooooooogggggggggrrbrrrrrrwwwwwwbwwyyyyyyyyy")
    def test_unsolvable_impossible_piece_4(self): # corners with colours of opposite cube sides
        self.unsolvable_impossible_piece_test("obbbbbbbbgoooooooorggggggggbrrrrrrrrwwwwwwwwwyyyyyyyyy")


    def unsolvable_edge_parity_test(self, cube_string):
        with self.assertRaises(ValueError) as result:
            Cube(cube_string)
        self.assertEqual('Error: Cube unsolvable: Edge parity', str(result.exception))

    def test_unsolvable_edge_parity_1(self):
        self.unsolvable_edge_parity_test("bwbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwbwyyyyyyyyy")
    def test_unsolvable_edge_parity_2(self):
        self.unsolvable_edge_parity_test("wbrybrbwggoyyooyywbowgggrwbbbgrrorryowrrwboyyogowygwbg")
    def test_unsolvable_edge_parity_3(self):
        self.unsolvable_edge_parity_test("wyrybybwggoyrooyywbowgggrwbbbgrrorryowrrwbobyogowygwbg")
    
    def unsolvable_corner_parity_test(self, cube_string):
        with self.assertRaises(ValueError) as result:
            Cube(cube_string)
        self.assertEqual('Error: Cube unsolvable: Corner parity', str(result.exception))

    def test_unsolvable_corner_parity_1(self):
        self.unsolvable_corner_parity_test("bbobbbbbbwoooooooogggggggggrrrrrrrrrwwwwwwwwbyyyyyyyyy")
    def test_unsolvable_corner_parity_2(self):
        self.unsolvable_corner_parity_test("bbwbbbbbbboooooooogggggggggrrrrrrrrrwwwwwwwwoyyyyyyyyy")
    def test_unsolvable_corner_parity_3(self):
        self.unsolvable_corner_parity_test("wbobbbbbbwoooooooogggggggggrrbrrrrrrwwwwwwrwbyyyyyyyyy")
    def test_unsolvable_corner_parity_4(self):
        self.unsolvable_corner_parity_test("rbwbbbbbbboooooooogggggggggrrwrrrrrrwwwwwwbwoyyyyyyyyy")
    def test_unsolvable_corner_parity_5(self):
        self.unsolvable_corner_parity_test("owgybbbgrwboyoygbowoyrgygowrgyorgbwrggbwwwbroyrwoyrrby")
    def test_unsolvable_corner_parity_6(self):
        self.unsolvable_corner_parity_test("owwybbbgroboyoygbowoyrgygowrgyorgbwrggbwwwbrgyrwoyrrby")
    def test_unsolvable_corner_parity_7(self):
        self.unsolvable_corner_parity_test("bwgybbbgrwboyoygbowoyrgygowrgoorgbwrggbwwwyroyrwoyrrby")
    def test_unsolvable_corner_parity_8(self):
        self.unsolvable_corner_parity_test("ywwybbbgroboyoygbowoyrgygowrgborgbwrggbwwworgyrwoyrrby")
    

    def unsolvable_permutation_parity_test(self, cube_string):
        #with self.assertRaises(ValueError) as result:
        #    Cube(cube_string)
        #self.assertEqual('Error: Cube unsolvable: Permutation parity', str(result.exception))
        pass
    
    def test_unsolvable_permutation_parity_1(self): # swap edges 1x
        self.unsolvable_permutation_parity_test("bgbbbbbbbooooooooogbgggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_unsolvable_permutation_parity_2(self): # swap corners 1x
        self.unsolvable_permutation_parity_test("obrbbbbbbboooooooogggggggggrrbrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_unsolvable_permutation_parity_3(self): # swap 3x edges
        self.unsolvable_permutation_parity_test("brbbbbbbbobooooooogogggggggrgrrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_unsolvable_permutation_parity_4(self): # swap 2x edges 1x corners
        self.unsolvable_permutation_parity_test("oorbbbbbbbgooooooogbgggggggrrbrrrrrrwwwwwwwwwyyyyyyyyy")
    def test_unsolvable_permutation_parity_5(self): # swap edges 1x
        self.unsolvable_permutation_parity_test("obroboogrwbbwowbbyowwrgrgrorbwyryggbbgwowrgwgyoyyyyygr")
    def test_unsolvable_permutation_parity_6(self): # swap corners 1x
        self.unsolvable_permutation_parity_test("wgwoboogrobbwowbbyowwrgrgrorbryryggbbbwowrgwgyoyyyyygr")
    def test_unsolvable_permutation_parity_7(self): # swap 3x edges
        self.unsolvable_permutation_parity_test("obroboogrwgbwowbbyobwrgrgrorwwyryggbbrwbwwgogyoyyyyygr")
    def test_unsolvable_permutation_parity_8(self): # swap 2x edges 1x corners
        self.unsolvable_permutation_parity_test("wbwoboogrobbwowbbyowwrgrgrorbryryggbbgwrwogwgyoyyyyygr")


    # Test 'where does [piece] go'
    def test_where_does_piece_go_solved(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        for piece in constants.CENTERS | constants.EDGES | constants.CORNERS:
            self.assertEqual(piece, cube.where_does_piece_go(piece))
    
    def test_where_does_piece_go_scrambled(self):
        cube = Cube("bwgrbyggbwbbrogyybywgygowggrgrbrbywywoowwywrororbyooro")
        expected = {FTL:FTL, FTM:UML, FTR:BTL, FML:LMR, FMM:FMM, FMR:DML, FBL:BBR, FBM:BML, FBR:FBL,
                    RTL:UTR, RTM:FBM, RTR:FBR, RML:LBM, RMM:RMM, RMR:BBM, RBL:DTL, RBM:DMR, RBR:FTR,
                    BTL:DTR, BTM:UMR, BTR:BTR, BML:DBM, BMM:BMM, BMR:RML, BBL:UBR, BBM:BMR, BBR:BBL,
                    LTL:LTL, LTM:BTM, LTR:LTR, LML:FMR, LMM:LMM, LMR:FML, LBL:DBR, LBM:UBM, LBR:DBL,
                    UTL:UTL, UTM:RTM, UTR:RBL, UML:UTM, UMM:UMM, UMR:DTM, UBL:UBL, UBM:LTM, UBR:RTR,
                    DTL:LBL, DTM:RMR, DTR:LBR, DML:FTM, DMM:DMM, DMR:RBM, DBL:RBR, DBM:LML, DBR:RTL}
        self.assertEqual(expected, {piece:cube.where_does_piece_go(piece) for piece in constants.CENTERS | constants.EDGES | constants.CORNERS})
        
    
    # Test finding face from colour
    def test_find_face_from_colour_solved(self):
        cube = Cube("bbbbbbbbbooooooooogggggggggrrrrrrrrrwwwwwwwwwyyyyyyyyy")
        expected_map = {'b':'f', 'o':'r', 'g':'b', 'r':'l', 'w':'u', 'y':'d'}
        self.assertEqual("".join(expected_map[piece] for piece in cube.cube_data), "".join(cube.find_face_from_colour(piece) for piece in cube.cube_data))
    
    def test_find_face_from_colour_scrambled(self):
        cube = Cube("bwgrbyggbwbbrogyybywgygowggrgrbrbywywoowwywrororbyooro")
        expected_map = {'b':'f', 'o':'r', 'g':'b', 'r':'l', 'w':'u', 'y':'d'}
        self.assertEqual("".join(expected_map[piece] for piece in cube.cube_data), "".join(cube.find_face_from_colour(piece) for piece in cube.cube_data))


if __name__ == '__main__':
    unittest.main()